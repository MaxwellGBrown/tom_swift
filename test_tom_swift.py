"""Tests for tom_swift.py."""
import pytest

import tom_swift


trigram_cases = [
    (
        "I wish I may I wish I might",
        {
            ("I", "wish"): ["I", "I"],
            ("wish", "I"): ["may", "might"],
            ("may", "I"): ["wish"],
            ("I", "may"): ["I"],
        },
    )
]


@pytest.mark.parametrize("text,expected", trigram_cases)
def test_read_trigrams(text, expected):
    """Assert read_trigrams(text) reads the proper trigram."""
    assert tom_swift.read_trigrams(text) == expected


@pytest.mark.parametrize("expected,trigram", trigram_cases)
def test_compose_text(trigram, expected):
    """Assert compose_text(trigram) write a valid text from trigram."""
    assert tom_swift.compose_text(trigram) == expected
