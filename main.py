import time_calculator as a
a.add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

a.add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

a.add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

a.add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

a.add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

a.add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)