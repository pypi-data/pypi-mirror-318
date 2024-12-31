#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 22/02/2016

Updated: 19/09/2017

# Description

The Ackermann function is the simplest example of a well defined total function.
Total function means that it's defined for all possible inputs. The function is
computable, but not primitive recursive. A primitive recursive function is a
function that can be implemented using only "for" loops, i.e. loops that have a
fixed number of iterations. A computable function is a function that can be
implemented using "while" loops. Note: "do" loops are a particular case of while
loops.

It grows faster than an exponential function, or even a multiple exponential
function.

# References

- http://mathworld.wolfram.com/AckermannFunction.html
- http://math.stackexchange.com/questions/75296/
  what-is-the-difference-between-total-recursive-and-primitive-recursive-functions
- https://en.wikipedia.org/wiki/Ackermann_function
"""

__all__ = ["ackermann"]


def ackermann(m: int, n: int) -> int:
    """
    Compute the Ackermann function.

    The Ackermann function is a total computable function that is not primitive recursive.

    See

    - https://en.wikipedia.org/wiki/Computable_function
    - https://en.wikipedia.org/wiki/Primitive_recursive_function
    """
    assert m >= 0 and n >= 0
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))
