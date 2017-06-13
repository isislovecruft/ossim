#!/usr/bin/python
# This is distributed under cc0. See the LICENCE file distributed along with
# this code.

"""Stupid simulated global time code."""

_time = 0

def now():
    """Return the current simulated time."""
    return _time

def advanceTime(n):
    """Advance the current simulated time by X seconds."""
    global _time
    assert n >= 0
    _time += n
