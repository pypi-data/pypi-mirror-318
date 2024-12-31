#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 04/08/2015

Updated: 19/09/2017

# Description

A very simple example of how to count the number occurrences of a certain object
o in a list ls.

You should not use recursion in general for doing this task: for example, in
Python the stack limit is quite small: 1000.
"""

__all__ = ["count"]


def _count(elem: object, ls, index: int) -> int:
    if index < len(ls):
        if ls[index] == elem:
            return 1 + _count(elem, ls, index + 1)
        return _count(elem, ls, index + 1)
    return 0


def count(elem: object, ls) -> int:
    """Counts how many times elem appears in the list or tuple ls."""
    return _count(elem, ls, 0)
