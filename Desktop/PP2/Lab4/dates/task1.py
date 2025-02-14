from datetime import datetime
curr = datetime.now()
print("Current date: ", curr.strftime('%d.%m.%Y'))
year = curr.year
month = curr.month
day = curr.day - 5
if day <= 0:
    month -= 1
    if month == 0:
        month = 12
        year -= 1
        from calendar import monthrange as days
        day += days(year, month)[1]
new = datetime(year, month, day)
print("New date: ", new.strftime('%d.%m.%Y'))
