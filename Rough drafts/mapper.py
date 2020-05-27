#!/usr/bin/env python 
"""mapper.py"""
import sys

#The LOCATION constant stores the Location ID for the location we want to extract.
LOCATION = "UK000056225"

#We go through each line of the input file.
for line in sys.stdin:    
    #These lines strip the line of any unnecessary whitespace and then splits it up into the words array.
    line = line.strip()    
    words = line.split(",")
    #First I check that the line has at least one value. This checks that the input line isn't blank. This check isn't completely necessary, however I thought it's good to be thorough.
    if(len(words) > 1):
        #I then assign the different word elements to variables.
        locationID = words[0]
        date = words[1]
        elementType = words[2]
        value = words[3]
        #I want to check that the line I'm checking is the correct type of measurement: TMIN or TMAX. 
        if(elementType == "TMIN" or elementType == "TMAX"):
            #I then want to check that the line is for the location we're looking for.
            if(locationID == LOCATION):
                #This line checks for a quality flag. If it is non-empty, then it is a failed measurement.
                if(words[5] != ""):
                    #For failed measurements I add 'fail' to the key. 
                    key = date + "fail"
                else:
                    key = date
                #This line outputs the key (usually just the date) and the value. 
                print('%s\t%s' %(key,value))
