import os

from dotenv import load_dotenv
from google import genai
from app.graph.state import SQLState

load_dotenv()

class GeminiService:
    def __init__(self):
        self.model = "gemini-3.6-flash"
        self.client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    def generate_sql(self, question: str, examples: list, schema: list) -> str:
        """
        This function generates SQL based on the provided question, examples, and schema.

        Args:
            question (str): The question to generate SQL for.
            examples (list): A list of relevant examples.
            schema (list): A list of relevant schema.
        """
        prompt = self.build_prompt(question, examples, schema)
        sql = self.call_gemini_api(prompt)
        return sql

    def build_prompt(self, question: str, examples: list, schema: list) -> str:
        """
        This function builds a prompt for the Gemini API based on the provided question, examples, and schema.

        Args:
            question (str): The question to generate SQL for.
            examples (list): A list of relevant examples.
            schema (list): A list of relevant schema.
        """
        prompt = f"""
        Generate PostgreSQL SQL.

        Question: {question}
        Relevant schema: {schema}
        Similar examples: {examples}
        """

        return prompt

    def call_gemini_api(self, prompt: str) -> str:
        """
        This function calls the Gemini API with the provided prompt and returns the generated SQL.

        Args:
            prompt (str): The prompt to send to the Gemini API.
        """
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt
        )
        return response.text

gemini_service = GeminiService()
