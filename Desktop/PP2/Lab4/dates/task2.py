from datetime import datetime
from calendar import monthrange as days
curr = datetime.now()
year = curr.year
month = curr.month
day = curr.day - 1
if day <= 0:
    month -= 1
    if month == 0:
        month = 12
        year -= 1
        day += days(year, month)[1]
new = datetime(year, month, day)
print("Yesterday: ", new.strftime('%d.%m.%Y'))
print("Today: ", curr.strftime('%d.%m.%Y'))

year = curr.year
month = curr.month
day = curr.day + 1
if day >= days(year, month)[1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1
new = datetime(year, month, day)
print("Tomorrow: ", new.strftime('%d.%m.%Y'))
