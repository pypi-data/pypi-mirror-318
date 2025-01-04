from typing import Iterable


def onlyone(iterable: Iterable):
    """Return the only element in an iterable, or raise an error if there is not exactly one element."""
    it = iter(iterable)
    try:
        result = next(it)
    except StopIteration:
        raise ValueError("iterable is empty") from None
    try:
        next(it)
        raise ValueError("iterable has more than one element")
    except StopIteration:
        return result
