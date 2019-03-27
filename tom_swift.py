"""Trigrams application to mutate text into new, surreal, forms.

http://codekata.com/kata/kata14-tom-swift-under-the-milkwood/
"""
from collections import defaultdict
import random


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


def _random(trigram):
    """Compose a trigram in the random order."""
    keys = [k for k in trigram.keys()]  # keys are ordered since 3.6
    seed = [*random.choice(keys)]

    yield from (item for item in seed)

    while any(v for v in trigram.values()):
        key = (seed[-2], seed[-1])
        upper_bound = len(trigram[key])
        if upper_bound < 1:
            break
        elif upper_bound == 1:
            index = 0
        else:
            index = random.randint(0, upper_bound - 1)

        value = trigram[key].pop(index)
        yield value
        seed = [seed[-1], value]


def compose_text(trigram, algorithm=_random):
    """Compose text given a trigram."""
    items = [i for i in algorithm(trigram)]

    return " ".join(items)


def main(text="I wish I may I wish I might"):
    """Execute the trigram."""
    trigrams = read_trigrams(text)
    print(compose_text(trigrams))


if __name__ == "__main__":
    main()
