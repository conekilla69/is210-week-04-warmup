#!usr/bi/env python
# -*- coding: utf-8 -*-
"""Using Booleans and integers to determine amount of catfood"""


def too_many_kittens(kittens, litterboxes, catfood=bool):
    """Finding out if there is enough catfood.

    Args:
        kittens (int): Arg gives the number of kittens.
        litterboxes (int): Arg tells the number of available litterboxes.
        catfood (bool): Arg represents whether or not any catfood exists.

    Returns:
        bool: Argument returns if there is enough catfood.

    Examples:
    >>> too_many_kittens(5, 12, False)
    True
    >>> too_many_kittens(4, 6, True)
    False
     """
    return not (litterboxes >= kittens and catfood)
