"""Tests for tom_swift.py."""
import pytest

import tom_swift


@pytest.mark.parametrize("text,expected", [
    (
        "I wish I may I wish I might",
        {
            ("I", "wish"): ["I", "I"],
            ("wish", "I"): ["may", "might"],
            ("may", "I"): ["wish"],
            ("I", "may"): ["I"],
        },
    )
])
def test_read_trigrams(text, expected):
    """Assert read_trigrams(text) reads the proper trigram."""
    assert tom_swift.read_trigrams(text) == expected
