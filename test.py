# -*- coding: utf-8 -*-
"""This is just an example for the virtual simulation lab."""
from __future__ import print_function


values = [i**2 for i in range(10)]

values.append(10 * 10)
values.append(2**3)

for val in values:
    print(val)
