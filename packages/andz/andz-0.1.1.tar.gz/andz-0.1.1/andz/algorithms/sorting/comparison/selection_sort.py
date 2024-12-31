#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 09/09/2015

Updated: 07/03/2018

# Description

Selection sorting is conceptually probably the simplest sorting algorithm.

This algorithm first finds the smallest element in the list and exchanges it
with the element in the first position, then find the second smallest element
and exchange it with the element in the second position, and continues in this
way until the entire list is sorted.

# References

- http://www.studytonight.com/data-structures/selection-sorting
- http://en.wikipedia.org/wiki/Selection_sort
- http://interactivepython.org/runestone/static/pythonds/SortSearch/TheSelectionSort.html
"""

__all__ = ["selection_sort"]


def selection_sort(ls: list) -> None:
    """Selection-sort in-place sorting algorithm.

    Time complexity

    +-------+----------+----------+
    | Best  |  Average |  Worst   |
    +-------+----------+----------+
    | O(n²) |   O(n²)  |   O(n²)  |
    +-------+----------+----------+

    Space complexity: O(n)."""
    for i in range(len(ls) - 1):
        k = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[k]:
                ls[k], ls[j] = ls[j], ls[k]
