"""Module for computing power sets."""

from typing import Any


def power(x: list[Any]) -> list[list[Any]]:
    """
    Compute the power-set of x.

    Returns the power-set of x as a list of lists.

    >>> power([])
    [[]]
    >>> power([1])
    [[], [1]]
    >>> power([1, 2])
    [[], [2], [1], [1, 2]]
    """
    n = len(x)
    numbers = list(range(2**n))
    bits = [format(i, "b").zfill(len(x)) for i in numbers]
    power_set = list()
    for index in bits:
        subset = [x[i] for i, v in enumerate(index) if v == '1']
        power_set.append(subset)
    return power_set
