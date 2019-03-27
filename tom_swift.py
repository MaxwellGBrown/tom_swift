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


def _same_order(trigram):
    """Yield items in the same order they were read from.

    This should create a result equal to the original text.
    """
    keys = [k for k in trigram.keys()]  # keys are ordered since 3.6
    seed = [*keys[0]]

    yield from (item for item in seed)

    while any(v for v in trigram.values()):
        value = trigram[(seed[-2], seed[-1])].pop(0)
        yield value
        seed = [seed[-1], value]


def compose_text(trigram, algorithm=_same_order):
    """Compose text given a trigram."""
    items = [i for i in algorithm(trigram)]
    return " ".join(items)


def main(text="I wish I may I wish I might"):
    """Execute the trigram."""
    trigrams = read_trigrams(text)
    print(compose_text(trigrams))


if __name__ == "__main__":
    main()
