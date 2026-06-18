def build_messages(user_question: str, search_context: str, history_messages):
    """
    history_messages: iterable of Message model instances (ordered oldest->newest).
    """
    messages = [
        {
            "role": "system",
            "content": (
                "You are an expert software developer in Java, Python, and Angular. "
                "You answer with clear, beginner-friendly explanations and short, focused code examples. "
                "Prefer practical examples (APIs, backend, architecture) over theory."
            ),
        },
        {
            "role": "system",
            "content": (
                "You are also given web search results. "
                "Use them as the primary factual context. "
                "If they do not contain enough information, say so explicitly and avoid inventing details. "
                "At the end of your answer, list 2–4 of the most relevant source URLs from the search results."
            ),
        },
    ]

    # History from DB
    for m in history_messages:
        messages.append({"role": m.role, "content": m.content})

    # Current question + search context
    search_block = (
        "Web Search Results:\n"
        f"{search_context}\n\n"
        "Now answer the user's question using these results as your main reference. "
        "If the results are not sufficient, clearly say what is missing."
    )

    messages.append({
        "role": "user",
        "content": f"{search_block}\n\nUser question:\n{user_question}",
    })

    return messages
