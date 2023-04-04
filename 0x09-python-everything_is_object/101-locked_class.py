#!/usr/bin/python3
"""
Locked Class
Prevents dynamic creation of new instance attributes
"""


class LockedClass:
    __slots__ = ["first_name"]
