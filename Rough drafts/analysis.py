#!/usr/bin/env python
"""analysis.py"""

file = open("E:\\Documents\\Uni work\\C - Final Year\\Cloud Computing\\2018.csv", "r")
lines = file.readlines()

location1 = "UK000056225"
location2 = "UK000003377"

loc1tmax = []
loc1tmaxfail = []
loc1tmin = []
loc1tminfail = []
loc2tmax = []
loc2tmaxfail = []
loc2tmin = []
loc2tminfail = []

for line in lines:
    line = line.strip()
    words = line.split(",")
    if(words[0] == location1):
        if(words[2] == "TMAX"):
            loc1tmax.append(words[1])
            if(words[5] != ""):
                loc1tmaxfail.append(words[1])

        if(words[2] == "TMIN"):
            loc1tmin.append(words[1])
            if(words[5] != ""):
                loc1tminfail.append(words[1])
    if(words[0] == location2):
        if(words[2] == "TMAX"):
            loc2tmax.append(words[1])
            if(words[5] != ""):
                loc2tmaxfail.append(words[1])
        if(words[2] == "TMIN"):
            loc2tmin.append(words[1])
            if(words[5] != ""):
                loc2tminfail.append(words[1])

for day in loc2tmax:
    print(loc2tmin.count(day))


print(len(loc1tmax))
print(len(loc1tmaxfail))
print(len(loc1tmin))
print(len(loc1tminfail))
print(len(loc2tmax))
print(len(loc2tmaxfail))
print(len(loc2tmin))
print(len(loc2tminfail))
