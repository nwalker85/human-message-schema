#!/usr/bin/env python3
"""Reference parser and conformance suite for Human Message Schema v0.0.1."""

from typing import Tuple


def parse_message(raw: str) -> Tuple[str, str]:
    """Parse a message according to Human Message Schema v0.0.1.

    Returns a tuple of (role, content) where role is 'human' or 'agent'.
    """
    stripped = raw.strip()
    if stripped.startswith("(") and stripped.endswith(")"):
        depth = 0
        is_enclosed = True
        for i, char in enumerate(stripped):
            if char == "(":
                depth += 1
            elif char == ")":
                depth -= 1
                if depth == 0 and i < len(stripped) - 1:
                    is_enclosed = False
                    break
        if depth == 0 and is_enclosed:
            return ("human", stripped[1:-1])

    return ("agent", raw)


def test_conformance():
    assert parse_message("(hello world)") == ("human", "hello world")
    assert parse_message("The meeting has been scheduled.") == (
        "agent",
        "The meeting has been scheduled.",
    )
    assert parse_message("(my cheeks hurt from grinning, thank you)") == (
        "human",
        "my cheeks hurt from grinning, thank you",
    )
    assert parse_message("(nested (parens) are supported)") == (
        "human",
        "nested (parens) are supported",
    )
    assert parse_message("(part 1) and (part 2)") == (
        "agent",
        "(part 1) and (part 2)",
    )
    print("All v0.0.1 conformance tests passed.")


if __name__ == "__main__":
    test_conformance()
