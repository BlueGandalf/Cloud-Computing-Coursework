#!/usr/bin/env python
#cat io/in/2018.csv | python3 mapper | sort -k1,1 | python3 reducer >> io/out/201856225

"""mapper.py"""
import sys

## PREFERENCES ##
#UK000056225
#UK000003377
area_code='UK000003377'

# list of all dates in 2018. refers here to check for dates with no value
dates = ['20180101', '20180102', '20180103', '20180104', '20180105', '20180106', '20180107', '20180108', '20180109', '20180110', '20180111', '20180112', '20180113', '20180114', '20180115', '20180116', '20180117', '20180118', '20180119', $
# counter for currently searching date
current_date_idx = 0
previous_input_date = None

# for every line in the data set
for line in sys.stdin:
  # remove the garbage from the input line
  line = line.strip()

  # convert the input line from csv to a python list
  row = line.split(',')

  # only process the specified area code
  if row[0] == area_code:

    # only capture values labeled as TMAX or TMIN
    if row[2] == 'TMAX' or row[2] == 'TMIN':

      # move to the next date if the input has move to the next date BUT ONLY if it is not the first input (otherwise it wil skip 20180101)
      if row[1] != previous_input_date and previous_input_date != None:
        current_date_idx = current_date_idx + 1

      # if the input has jumped dates, go through all the dates it has missed and output a value of nothing to that date
      while row[1] != dates[current_date_idx]:
        print ("%s-%s\t%s" % (area_code, dates[current_date_idx], "0"))
        current_date_idx = current_date_idx + 1
        

      # after all of the above, we have caught up to the right date, now output the value of the input date
      print ("%s-%s\t%s" % (row[0], row[1], int(row[3])))

      # save the current inputed day so the next iteration knows if the input date has changed
      previous_input_date = row[1]

