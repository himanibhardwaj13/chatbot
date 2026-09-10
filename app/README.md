
| File                         | Responsibility              |
| ---------------------------- | --------------------------- |
| `main.py`                    | Start FastAPI               |
| `chat.py`                    | API endpoint                |
| `state.py`                   | LangGraph shared state      |
| `graph.py`                   | Connect nodes/workflow      |
| `vanna_node.py`              | Retrieve schema/examples    |
| `gemini_node.py`             | Generate SQL                |
| `sql_validation_node.py`     | Validate SQL                |
| `database_node.py`           | Execute SQL                 |
| `response_formatter_node.py` | Convert rows → UI JSON      |
| `vanna_service.py`           | Vanna configuration/client  |
| `gemini_service.py`          | Gemini configuration/client |
| `database_service.py`        | PostgreSQL connection       |
| `examples.json`              | Question → SQL examples     |
| `schema.sql`                 | Database tables             |
| `seed.sql`                   | Sample data                 |

main.py
   ↓
api/chat.py
   ↓
graph/graph.py
   ↓
┌──────────────────────┐
│ Vanna Node           │
├──────────────────────┤
│ Gemini Node          │
├──────────────────────┤
│ SQL Validation Node  │
├──────────────────────┤
│ Database Node        │
├──────────────────────┤
│ Response Formatter   │
└──────────────────────┘
   ↓
JSON response
