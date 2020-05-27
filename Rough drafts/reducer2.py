#!/usr/bin/env python
"""reducer.py"""
from __future__ import division
from operator import itemgetter
from datetime import timedelta, date, datetime
import sys

#This is initialising valriables to the correct variable type.
key = None
counter = 0
lines = []

#This establishes the date range we're looking at - which we know is the whole of 2018.
startDate = date(2018, 1, 1)
endDate = date(2019, 1, 1)

#This is a function we use to iterate through the entirety of the specified date range.
def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#We load the output of the mapper into an array, so that we can iterate through it multiple times
for line in sys.stdin:
    lines.append(line)

#We then iterate through our defined date range
for day in daterange(startDate, endDate):
    
    #For each day we initialise the default values of these variables to 0.
    counter = 0 # This counts the number of entries are from this day. We are looking for two.
    currentValue = 0 # This is the variable we use to calculate the temperature difference.

    #For each day, we then iterate through our input
    for line in lines:
        #The next few lines strip the line of any unnecessary whitespace and then splits it into the key and the value.
        line.strip()
        key,value = line.split("\t", 1)

        #This makes the value variable an integer, so we can perform arithmetic on it.
        try:        
            value = int(value)
        except ValueError:
            continue

        # This if statement checks whether the line of input is for the current day we're checking.
        if(day.strftime("%Y%m%d") == key):
            #We count that there was an entry for the day.
            counter += 1
            #We take the absolute difference of the currentValue with the value. Done twice, this gives us the positive difference between the two values.
            currentValue = abs(currentValue - value)

    #After iterating through the entire input, we check our counter. If this is less than 2, we know we have received incomplete data about this day, and so we output a blank line. Else, we output the difference we've calculated.
    if(counter == 0):
        print("")
    elif(counter == 1):
        print("")
    else:
        print(currentValue / 10) # We divide this by 10 in order to give degrees celsius rather than tenths of degrees celsius.