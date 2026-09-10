from langgraph.graph import StateGraph, START, END
from app.graph.state import SQLState
from app.nodes.vanna_node import vanna_node
from app.nodes.gemini_node import gemini_node
from app.nodes.database_node import database_node
from app.nodes.response_formater_node import response_formatter_node as response_node

builder = StateGraph(SQLState)

# add nodes to the graph
builder.add_node("vanna", vanna_node)
builder.add_node("gemini", gemini_node)
builder.add_node("database", database_node)
builder.add_node("response_format", response_node)

# define execution flow
builder.add_edge(START, "vanna")
builder.add_edge("vanna", "gemini")
builder.add_edge("gemini", "database")
builder.add_edge("database", "response_format")
builder.add_edge("response_format", END)

graph_builder = builder.compile()
