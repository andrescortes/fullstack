import logging
import requests

logger = logging.getLogger('drf_logger')

LLAMA_SERVER_URL = "http://localhost:8080/v1/chat/completions"


def call_llm(messages: list) -> str:
    """
    Call llm and return a message
    """
    payload = {
        "messages": messages,
    }
    resp = requests.post(LLAMA_SERVER_URL, json=payload, timeout=120)
    resp.raise_for_status()
    data = resp.json()
    logger.debug(f"LLM response: {data}")

    try:
        choice = data["choices"][0]
        msg = choice.get("message", {})
        content = msg.get("content", "")

        reasoning = msg.get("reasoning_content")
        if reasoning:
            content = f"{content}\n\n[Reasoning]\n{reasoning}"

        return content

    except (KeyError, IndexError, TypeError) as e:
        raise RuntimeError(f"Unexpected LLM response format: {data}") from e


def llama_stream(messages: list):
    """
    Generator that yields raw SSE lines from llama-server.
    """
    payload = {
        "messages": messages,
        "stream": True,
    }

    # Important: stream=True
    with requests.post(
            LLAMA_SERVER_URL,
            json=payload,
            stream=True,
            headers={"Accept": "text/event-stream", "Accept-Encoding": "identity"},
    ) as resp:
        resp.raise_for_status()
        for line in resp.iter_lines(decode_unicode=True):
            if not line:
                continue
            yield line
