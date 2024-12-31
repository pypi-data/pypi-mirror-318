#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 23/08/2015

Updated: 18/09/2017

# Description

Finding the maximum (or minimum) of a list of numbers (or, in general,
comparable objects) using the "divide and conquer" strategy.
"""

__all__ = [
    "find_extremum_not_in_place",
    "find_extremum_in_place",
    "find_max",
    "find_min",
]


def find_extremum_not_in_place(ls: list, _find_max: bool = True) -> object:
    """Finds (not in-place) the maximum (or minimum) element in the list ls.

    It finds the maximum if _find_max is set to true, it finds the minimum
    otherwise."""
    if len(ls) == 0:
        return
    if len(ls) == 1:
        return ls[0]
    if len(ls) == 2:
        if _find_max:
            return ls[0] if ls[0] > ls[1] else ls[1]
        return ls[0] if ls[0] < ls[1] else ls[1]

    mid = len(ls) // 2
    m1 = find_extremum_not_in_place(ls[0:mid], _find_max)
    m2 = find_extremum_not_in_place(ls[mid:], _find_max)

    if _find_max:
        return m1 if m1 > m2 else m2
    return m1 if m1 < m2 else m2


def _find_extremum_in_place(
    ls: list, start: int, end: int, _find_max: bool = True
) -> object:
    if (end - start) < 0:
        return
    if (end - start) == 0:
        return ls[start]
    if (end - start) == 1:
        if _find_max:
            return ls[start] if ls[start] > ls[end] else ls[end]
        return ls[start] if ls[start] < ls[end] else ls[end]  # find min

    mid = (start + end) // 2
    assert start <= mid <= end
    m1 = _find_extremum_in_place(ls, start, mid - 1, _find_max)
    m2 = _find_extremum_in_place(ls, mid, end, _find_max)

    if _find_max:
        return m1 if m1 > m2 else m2
    return m1 if m1 < m2 else m2  # find min


def find_extremum_in_place(ls: list, _find_max: bool = True) -> object:
    """Finds (in place) the maximum (or minimum) element in the list ls.

    It finds the maximum if _find_max is set to true, it finds the minimum
    otherwise."""
    return _find_extremum_in_place(ls, 0, len(ls) - 1, _find_max)


def find_max(ls: list) -> object:
    """
    Find the maximum element in ls using a divide-and-conquer strategy.
    """
    m = find_extremum_in_place(ls)
    assert m == find_extremum_not_in_place(ls)
    return m


def find_min(ls: list) -> object:
    """
    Find the minimum element in ls using a divide-and-conquer strategy.
    """
    m = find_extremum_in_place(ls, False)
    assert m == find_extremum_not_in_place(ls, False)
    return m
