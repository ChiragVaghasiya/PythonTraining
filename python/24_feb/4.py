# 4. Calculate the date 4 months from the current date.

import datetime
from dateutil.relativedelta import relativedelta

print("Current date is:",datetime.date.today() ,"and after the six mounth date is:", datetime.date.today() + relativedelta(months=+6))