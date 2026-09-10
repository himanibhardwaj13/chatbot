
@router.post("/chat")
async def chat(request: ChatRequest):

    result = await text_to_sql_graph.ainvoke({
        "question": request.question
    })

    return result["response"]
