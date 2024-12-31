#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 20/07/2015

Updated: 19/09/2017

# Description

Bubble-sort is an algorithm which is used to sort N elements that are given in a
memory. For example, an array or list with N number of elements. Bubble-sort
compares all the element one by one and sort them based on their values.

It is called bubble-sort, because with each iteration the smaller element in the
list bubbles up towards the first place, just like a water bubble rises up to
the water surface.

Sorting takes place by stepping through all the data items one-by-one in pairs
and comparing adjacent data items and swapping each pair that is out of order.

# TODO

- Add ASCII animation of a sorting example using bubble-sort.

# References

- http://www.studytonight.com/data-structures/bubble-sort
- http://en.wikipedia.org/wiki/Bubble_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheBubbleSort.html
- http://stackoverflow.com/questions/29555839/how-to-calculate-bubble-sort-time-complexity
"""

__all__ = ["bubble_sort"]


def bubble_sort(ls: list) -> None:
    """Bubble-sort in-place sorting algorithm.

    Time complexity

    +------+----------+----------+
    | Best |  Average |  Worst   |
    +------+----------+----------+
    | O(n) |   O(n²)  |   O(n²)  |
    +------+----------+----------+

    Note: best case is O(n) when ls is already sorted, and thus no swap occurs.

    Space complexity: O(1).

    Note: space complexity is O(1), but not considering memory for original
    list ls."""
    assert isinstance(ls, list)
    for i in range(len(ls) - 1):
        for j in range(len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
