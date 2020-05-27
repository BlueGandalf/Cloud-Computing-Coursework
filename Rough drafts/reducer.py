#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys

current_key = None
current_count = 0
key = None

for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t', 1)

    try:        
        value = int(value)
    except ValueError:
        continue
        
    if(current_key == key):
        current_count = abs(current_count - value)
    else:
        if(current_key is None):
            current_key = key
            current_count = value
        else:
            print("%s\t%s" % (current_key, current_count))
            current_count = value
            current_key = key

if current_key == key:
    print("%s\t%s" % (current_key, current_count))