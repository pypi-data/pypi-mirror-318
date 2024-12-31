#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
# Meta-info

Author: nbro

Created: 08/08/2015

Updated: 19/01/2017

# Description

Converts a number in a certain base in the range [2, 36] to a decimal number.
Bases greater than 10 take in order as digits the letters of the English
alphabet. For example, a number system with base 11, would take 'a' as the 11th
digit.
"""

from string import ascii_lowercase, digits

__all__ = ["make_decimal", "ALPHA_NUMERIC_ALPHABET"]


def _build_alpha_numeric_alphabet() -> dict:
    """Returns a dictionary whose keys are all nine digits from 0 to 9 and the
    26 letters of the English alphabet.

    The values of the numbers are the numbers themselves. The values of the
    letters are 10 for 'a', 11 for 'b', and so on until 36 for 'z'."""
    alphabet = {}
    for i, char in enumerate(ascii_lowercase):
        # Letters of the alphabet start after digit 9.
        alphabet[char] = i + 10
    for i, char in enumerate(digits):
        alphabet[char] = i
    return alphabet


ALPHA_NUMERIC_ALPHABET = _build_alpha_numeric_alphabet()


def _make_decimal(n: str, b: int, pos: int) -> int:
    """Suppose we have a number n=xyz (represented as string) in base b.

    The algorithm of converting it to a decimal representation is as follows.

        b⁰ * decimal_value(z) + b¹ * decimal_value(y) + b² * decimal_value(x),

    where decimal_value(z) is the decimal value of the digit z.

    For example, suppose "ef2" is an hexadecimal number that we want to convert
    to decimal, which should yield 3826.

        16⁰ * decimal_value(2) +
        16¹ * decimal_value(f) +
        16² * decimal_value(e) =
        1 * 2 + 16 * 15 + 256 * 14 =
        2 + 240 + 3584 =
        3826

    Note: in any number n=xyz in any base b, z is in the "ones" position (has
    the smaller "value"), y is in the "tens" position and x is in the "hundreds"
    position (has the greatest "value").

    See: http://www.math.com/school/subject1/lessons/S1U1L1GL.html."""
    if len(n) == 0:
        return 0
    last = b**pos * ALPHA_NUMERIC_ALPHABET[n[-1]]
    return _make_decimal(n[:-1], b, pos + 1) + last


def make_decimal(n: str, base: int) -> int:
    """n is a number in any base in the range [2, 36]. base is the base in which
    n is currently represented.

    Assumes n only contains digits in the range 0..9 and letters of the English
    alphabet.

    Returns the decimal representation of n (as a int)."""
    if not n:
        raise ValueError("n cannot be an empty string or None")
    if base > 36 or base < 2:
        raise ValueError("not base >= 2 and base <= 36")
    return _make_decimal(n, base, 0)
