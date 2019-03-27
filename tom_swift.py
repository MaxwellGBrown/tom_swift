"""Trigrams application to mutate text into new, surreal, forms.

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
"""
from collections import defaultdict


def read_trigrams(text):
    """Return a trigrams dictionary from text."""
    trigrams = defaultdict(list)

    split_text = text.split(" ")
    while len(split_text) >= 3:
        first, second, third, *rest = split_text
        trigrams[(first, second)].append(third)
        split_text = split_text[1:]

    return trigrams


def main(text="I wish I may I wish I might"):
    """Execute the trigram."""
    trigrams = read_trigrams(text)
    print(trigrams)


if __name__ == "__main__":
    main()
