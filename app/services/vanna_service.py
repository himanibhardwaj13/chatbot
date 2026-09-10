import json
from pathlib import Path
from typing import Any


class VannaService:
    """
    Responsible for:
    Initializing Vanna,
    Loading database schema
    Loading SQL examples
    Storing/indexing Vanna knowledge
    Retrieving relevant context for a user question
    """

    def __init__(self, 
                 examples_path: str = "training/examples.json",
                 schema_path: str = "sql/schema.sql"):
        self.examples_path = Path(examples_path)
        self.schema_path = Path(schema_path)
        
        self.examples = self._load_examples()
        self.schema = self._load_schema()

    def _initialize_vanna(self):
        raise NotImplementedError

    def _load_examples(self) -> list[dict[str, Any]]:
        with self.examples_path.open("r", encoding="utf-8") as file:
            return json.load(file)
        
    def _load_schema(self) -> str:
        return self.schema_path.read_text(encoding="utf-8")
    
    def train_examples(self) -> None:
        for example in self.examples:
            question = example["question"]
            sql = example["sql"]
            self._add_example_to_vanna(question=question, sql=sql)

    def train_schema(self) -> None:
        """
        Add database schema knowledge to Vanna.
        """
        # Exact Vanna 2.0.2 schema/knowledge operation goes here.
        self._add_schema_to_vanna(self.schema)

    def _add_example_to_vanna(
        self,
        question: str,
        sql: str,
    ) -> None:
        """
        Store one question → SQL example in Vanna.
        """
        raise NotImplementedError

    def _add_schema_to_vanna(self, schema: str) -> None:
        """
        Store schema information in Vanna.
        """
        raise NotImplementedError

    def retrieve(self, question: str) -> dict[str, Any]:
        """
        Retrieve relevant examples/schema for a user question.
        """

        # Exact Vanna 2.0.2 retrieval operation goes here.
        if not question or not question.strip():
            raise ValueError("Question must be a non-empty string.")
        relevant_examples = self.find_relevant_examples(question)

        return {
            "relevant_examples": relevant_examples,
            "relevant_schema": self.schema
        }

    def find_relevant_examples(self, question: str, limit: int = 5) -> list[dict[str, Any]]:
        """
        Find relevant examples for a user question.
        """
        # Exact Vanna 2.0.2 retrieval operation goes here.
        # For now, return all examples as a placeholder.
        question_words = set(question.lower().replace("?", "").replace(",", "").split())
        scored_examples = []

        for example in self.examples:
            example_questions = example.get("question", "")
            example_words = set(example_questions.lower().replace("?", "").replace(",", "").split())
            score = len(question_words.intersection(example_words))
            if score > 0:
                scored_examples.append((score, example))
            scored_examples.sort(key=lambda x: x[0], reverse=True)

        return [example for _,example in scored_examples[:limit]]

# Application-wide service instance
vanna_service = VannaService()
