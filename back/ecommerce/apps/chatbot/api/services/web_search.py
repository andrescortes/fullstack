from ddgs import DDGS


def web_search(query: str, max_results: int = 4):
    """Return a text block with title, snippet and URL per result"""

    lines = []
    with DDGS() as ddg:
        results = ddg.text(query, max_results=max_results)
        for r in results:
            title = r.get("title", "")
            body = r.get("body", "")
            href = r.get("href", "")
            lines.append(f"- {title}\n Summary: {body}\n URL: {href}")
    if not lines:
        return "No results found for this query"
    return "\n".join(lines)
