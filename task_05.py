#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Assigning default values and returning a logical comparison."""

def defaults(my_required, my_optional='true'):
    """Determines if required is the same as optional.

    Args:
        my_required (mixed): Arg has a defined value.
        My_optional (str, optional): Optional str.  Default = 'true'

    Returns:
        mixed: All arguments will return an int or bool combination.

    Examples:
        >>> defaults(4)
            False
        >>> defaults(False)
            False
        >>> defaults(3, 6)
            False
    
    """
    return my_optional is my_required
