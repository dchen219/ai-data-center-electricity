"""JSON parsing utilities for LLM output processing."""

import json
import re
from typing import Any, Dict, List, Union


def extract_json_from_text(text: Any) -> str:
    """
    Extract JSON from LLM output text that may contain markdown code blocks.

    The function handles:
    - Plain JSON strings
    - JSON wrapped in ```json ... ``` code blocks
    - JSON wrapped in ``` ... ``` code blocks
    - Text with JSON embedded after prose

    Args:
        text: The text containing JSON (or already parsed JSON)

    Returns:
        Cleaned JSON string ready for parsing
    """
    if not isinstance(text, str):
        return text

    # Remove markdown code block markers
    text = re.sub(r"^```(json)?|```$", "", text.strip(), flags=re.MULTILINE).strip()

    # Find the start of JSON (either object or array)
    brace_pos = text.find("{")
    bracket_pos = text.find("[")

    positions = [pos for pos in [brace_pos, bracket_pos] if pos != -1]

    if not positions:
        return text

    start = min(positions)
    return text[start:]


def safe_parse_json(text: str) -> Union[Dict, List, str]:
    """
    Safely parse JSON from text, returning the original text on failure.

    Args:
        text: Text to parse as JSON

    Returns:
        Parsed JSON object/array, or original text if parsing fails
    """
    try:
        cleaned = extract_json_from_text(text)
        return json.loads(cleaned)
    except (json.JSONDecodeError, TypeError):
        return text


def format_json_output(data: Any, indent: int = 2) -> str:
    """
    Format data as pretty-printed JSON string.

    Args:
        data: Data to format
        indent: Indentation level

    Returns:
        Formatted JSON string
    """
    return json.dumps(data, indent=indent, ensure_ascii=False)
