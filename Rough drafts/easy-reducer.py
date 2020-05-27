#!/usr/bin/env python
"""easy-reducer.py"""

from operator import itemgetter
import sys

for line in sys.stdin:
    # remove leading and trailing whitespace    
    line = line.strip()

    # parse the input we got from mapper.py    
    key, value = line.split('\t', 1)

    # convert count (currently a string) to int
    try:        
        value = int(value)
    except ValueError:
        # count was not a number, so silently        
        # ignore/discard this line
        continue

    print("%s\t%s" % (key, value))