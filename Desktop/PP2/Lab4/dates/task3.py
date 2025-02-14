from datetime import datetime
curr = datetime.now()
#curr.microsecond = 0
print(curr.strftime('%d.%m.%Y %H:%M:%S'))
