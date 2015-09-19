#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""
#Global scope
numwink = 2


def know_what_i_mean(wink, nudges='nudge'):
    """Does some math and returns a string.

    Args:
        wink (mixed): Arg to be repeated by global variable.
        nudges (mixed): Arg to be repeated by global variable.
    
    Returns:
        str: All arguments concatenated with a coma.

    Examples
       >>> know_what_i_mean(2, 6)
       'Know what I mean? 4, nudge nudge '
    """
    winks = (wink * numwink)
    nudges = ('nudge ' * numwink)
    return 'Know what I mean? {}, {}'.format(winks, nudges)

