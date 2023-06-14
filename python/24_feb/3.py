# 3. Add a week (7 days) and 12 hours to a given date.

import datetime

year = int(input("Enter Your Year : "))
month = int(input("Enter Your month : "))
date = int(input("Enter Your date : "))
hours = int(input("Enter Your hours : "))

a = datetime.datetime(year,month,date,hours) + datetime.timedelta(days=7)
print("After the Seven days the Date and Time is: ",a)