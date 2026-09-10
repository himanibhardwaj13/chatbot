# chatbot
Backend AI chatbot using FastAPI, LangGraph, Vanna, Gemini, PostgreSQL, and SQLGlot. It converts natural-language questions into validated SQL, retrieves relevant schema/examples, executes queries against the database, and transforms raw results into structured JSON responses for UI consumption.


### AI Text-to-SQL Chatbot

A backend-focused AI chatbot that allows users to ask questions about security and vulnerability data using natural language. The application converts user questions into SQL queries, validates the generated SQL, executes it against a PostgreSQL database, and transforms the database results into a structured response suitable for a frontend application.

The project demonstrates the fundamentals of building an LLM-powered application using **FastAPI, LangGraph, Vanna, Gemini, PostgreSQL, and SQLGlot**.

### Key Technologies

* **FastAPI** — REST API layer for receiving user questions
* **LangGraph** — workflow orchestration and state management
* **Vanna** — retrieval of relevant database schema and question-SQL examples
* **Google Gemini** — natural-language-to-SQL generation
* **SQLGlot** — SQL parsing and validation before execution
* **PostgreSQL** — sample security/vulnerability database
* **Python** — backend implementation

### Application Flow

User question → FastAPI → LangGraph → Vanna → Gemini → SQL Validation → PostgreSQL → Response Formatter → Structured JSON

The response formatter converts raw database records into a predictable JSON structure containing only the information required by the UI, such as entity names, identifiers, and navigation URLs.

### Example

A user can ask:

> "Show me the top 5 assets with critical vulnerabilities."

The system retrieves relevant schema and SQL examples, generates an appropriate SQL query, validates it, executes it against PostgreSQL, and returns a structured response such as:

```json
{
  "type": "list",
  "items": [
    {
      "name": "server-01",
      "url": "/assets/101"
    },
    {
      "name": "server-02",
      "url": "/assets/102"
    }
  ]
}
```

The project is intentionally designed as a **small backend MVP** to demonstrate practical understanding of **LLM application architecture, Text-to-SQL, retrieval, workflow orchestration, SQL validation, database integration, and structured AI responses** without the complexity of a production-scale platform.


                    ┌─────────────────┐
                    │   API Request   │
                    │    FastAPI      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │    LangGraph    │
                    │   Orchestrator  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Vanna Node    │
                    │                 │
                    │ schema/examples │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │   Gemini Node   │
                    │                 │
                    │ Natural Language│
                    │      ↓          │
                    │      SQL        │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ SQL Validation  │
                    │    SQLGlot      │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │  PostgreSQL DB  │
                    │                 │
                    │  Execute SQL    │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Response        │
                    │ Formatter Node  │
                    └────────┬────────┘
                             │
                             ▼
                    ┌─────────────────┐
                    │ Structured JSON │
                    └─────────────────┘
