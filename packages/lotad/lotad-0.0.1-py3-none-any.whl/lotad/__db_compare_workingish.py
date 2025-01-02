import logging
import os
from typing import Optional

import duckdb

from lotad.data_analysis import DriftAnalysis
from lotad.utils import get_row_hash

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
CPU_COUNT = os.cpu_count()


class DatabaseComparator:

    def __init__(self, db1_path: str, db2_path: str):
        """Initialize connections to both DuckDB databases."""
        self.db1_path = str(db1_path)
        self.db1 = duckdb.connect(self.db1_path, read_only=True)
        self.db1.create_function("get_row_hash", get_row_hash)

        self.db2_path = str(db2_path)
        self.db2 = duckdb.connect(self.db2_path, read_only=True)
        self.db2.create_function("get_row_hash", get_row_hash)

        self.drift_analysis = DriftAnalysis()

    def get_tables(self, connection: duckdb.DuckDBPyConnection) -> list[str]:
        """Get list of all tables in a database."""
        return connection.execute(
            "SELECT table_name FROM information_schema.tables WHERE table_schema = 'main'"
        ).fetchall()

    def get_schema(self, connection: duckdb.DuckDBPyConnection, table: str) -> dict:
        """Get schema information for a table."""
        columns = connection.execute(f"""
            SELECT column_name, data_type
            FROM information_schema.columns
            WHERE table_name = '{table}'
            AND table_schema = 'main'
            AND data_type NOT LIKE 'TIMESTAMP%'
            AND data_type NOT LIKE 'DATE'
            ORDER BY ordinal_position
        """).fetchall()
        return {col[0]: col[1] for col in columns}

    def compare_table_schemas(self, table: str) -> dict:
        """Compare schemas between databases for a given table."""
        schema1 = self.get_schema(self.db1, table)
        schema2 = self.get_schema(self.db2, table)

        return {
            'missing_in_db2': set(schema1.keys()) - set(schema2.keys()),
            'missing_in_db1': set(schema2.keys()) - set(schema1.keys()),
            'type_mismatches': {
                col: (schema1[col], schema2[col])
                for col in set(schema1.keys()) & set(schema2.keys())
                if schema1[col] != schema2[col]
            }
        }

    def compare_table_data(self, table: str) -> dict:
        # Load data from both databases
        from datetime import datetime
        start_time = datetime.now()
        logger.info(f"Getting table data for {table} on df1")
        df1 = self.db1.execute(
            f"SELECT get_row_hash(ROW_TO_JSON(t)::VARCHAR) AS row_hash, * FROM {table} t"
        ).df()
        # df1 = self.db1.execute(
        #     f"SELECT get_row_hash(ROW_TO_JSON(t)::VARCHAR) AS row_hash, * FROM {table} t"
        # ).df()
        logger.info(f"Finished table data for {table} on df1 in {datetime.now() - start_time}")
        return {}

        logger.info(f"Getting table data for {table} on df2")
        df2 = self.db2.execute(
            f"SELECT get_row_hash(ROW_TO_JSON(t)::VARCHAR) AS row_hash, * FROM {table} t"
        ).df()

        # Compare row counts
        row_diff = len(df1) - len(df2)

        # Find differences using hash comparison
        print(f"Diff check for {table}")
        only_in_db1 = df1[~df1['row_hash'].isin(df2['row_hash'])]
        only_in_db2 = df2[~df2['row_hash'].isin(df1['row_hash'])]

        print(f"Data drift add db1 for {table}")
        self.drift_analysis.add_data_drift(
            only_in_db1,
            table,
            self.db1_path
        )

        print(f"Data drift add db2 for {table}")
        self.drift_analysis.add_data_drift(
            only_in_db2,
            table,
            self.db2_path
        )
        print(f"Done with {table}\n\n")

        return {
            'row_count_diff': row_diff,
            'only_in_db1': only_in_db1,
            'only_in_db2': only_in_db2
        }

    def compare_all(
        self,
        ignore_tables: Optional[list[str]] = None,
        tables: Optional[list[str]] = None,

    ) -> dict:
        """Compare all tables between the two databases."""
        tables1 = set(table[0] for table in self.get_tables(self.db1))
        tables2 = set(table[0] for table in self.get_tables(self.db2))

        results = {
            'missing_tables': {
                'in_db2': tables1 - tables2,
                'in_db1': tables2 - tables1
            },
            'common_tables': {}
        }

        for table in sorted(tables1 & tables2):
            table_name = table.lower()
            if ignore_tables and table_name in ignore_tables:
                continue

            if tables and table.lower() not in tables:
                continue
            print(f"Comparing table {table}")
            self.compare_table_data(table)

            # logger.info(f"Comparing table: {table}")
            # results['common_tables'][table] = {
            #     'schema_differences': self.compare_table_schemas(table),
            #     'data_differences': self.compare_table_data(table)
            # }

        return results

    def close(self):
        self.db1.close()
        self.db2.close()


def generate_comparison_report(results: dict, output_path: str = "comparison_report.txt"):
    """Generate a detailed comparison report."""
    with open(output_path, 'w') as f:
        f.write("Database Comparison Report\n")
        f.write("=========================\n\n")

        # Report missing tables
        if results['missing_tables']['in_db2']:
            f.write("Tables missing in second database:\n")
            for table in results['missing_tables']['in_db2']:
                f.write(f"- {table}\n")
            f.write("\n")

        if results['missing_tables']['in_db1']:
            f.write("Tables missing in first database:\n")
            for table in results['missing_tables']['in_db1']:
                f.write(f"- {table}\n")
            f.write("\n")

        # Report differences in common tables
        f.write("Common Tables Analysis:\n")
        for table, differences in results['common_tables'].items():
            f.write(f"\nTable: {table}\n")
            f.write("-" * (len(table) + 7) + "\n")

            schema_diff = differences['schema_differences']
            if any(schema_diff.values()):
                f.write("Schema differences:\n")
                if schema_diff['missing_in_db2']:
                    f.write(f"  Columns missing in DB2: {', '.join(schema_diff['missing_in_db2'])}\n")
                if schema_diff['missing_in_db1']:
                    f.write(f"  Columns missing in DB1: {', '.join(schema_diff['missing_in_db1'])}\n")
                if schema_diff['type_mismatches']:
                    f.write("  Type mismatches:\n")
                    for col, (type1, type2) in schema_diff['type_mismatches'].items():
                        f.write(f"    {col}: DB1={type1}, DB2={type2}\n")
                f.write("\n")

            data_diff = differences['data_differences']
            f.write(f"Data differences:\n")
            f.write(f"  Row count difference: {data_diff['row_count_diff']}\n")
            f.write(f"  Rows only in DB1: {len(data_diff['only_in_db1'])}\n")
            f.write(f"  Rows only in DB2: {len(data_diff['only_in_db2'])}\n")
            f.write("\n")
