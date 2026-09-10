import sqlglot

class SQLValidationService:
    def validate_sql(self, sql_query: str) -> str:
        # Attempt to parse the SQL query using sqlglot
        parsed = sqlglot.parse_one(sql_query, dialect="postgres")
        if not parsed:
            raise ValueError("Invalid SQL query")
        return sql_query

sql_validation_service = SQLValidationService()