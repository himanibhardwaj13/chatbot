import os

import psycopg
from dotenv import load_dotenv

load_dotenv()

class DatabaseService:
    def __init__(self):
        self.client = psycopg.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=os.getenv("DB_PORT", 5432),
            dbname=os.getenv("DB_NAME", "mydatabase"),
            user=os.getenv("DB_USER", "postgres"),
            password=os.getenv("DB_PASSWORD", "your_password")
        )

    def execute(self, sql:str):
        """
        Executes the given SQL query and returns the result.

        Args:
            sql (str): The SQL query to be executed.
        """
        with self.client.cursor() as cursor:
            cursor.execute(sql)
            if cursor.description:
                # Check if the query returns any rows
                return []
            columns = [column.name for column in cursor.description]
            result = cursor.fetchall()
            return [ dict(zip(columns, row)) for row in result ]

database_service = DatabaseService()  # Replace 'db=None' with your actual database connection