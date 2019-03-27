"""Trigrams application to mutate text into new, surreal, forms.

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
"""
from collections import defaultdict


def generate_trigrams(items):
    """Iterate through text and yield keys & values for trigrams."""
    if len(items) >= 3:
        first, second, third, *rest = items
        yield (items[0], items[1]), items[2]
        yield from generate_trigrams(items[1:])


def main(text="I wish I may I wish I might"):
    """Execute the trigram."""
    # Read Trigram from text
    trigrams = defaultdict(list)

    split_text = text.split(" ")
    for key, value in generate_trigrams(split_text):
        trigrams[key].append(value)

    return trigrams


if __name__ == "__main__":
    main()
