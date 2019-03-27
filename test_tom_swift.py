"""Tests for tom_swift.py."""
import pytest

from tom_swift import main


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
def test_main(text, expected):
    """Assert main() reads the proper trigram."""
    assert main(text) == expected
