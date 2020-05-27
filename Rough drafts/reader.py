#!/usr/bin/env python
"""reader.py"""

file = open("../2018.csv","r")
lines = file.readlines()
for line in lines:
    print(line)