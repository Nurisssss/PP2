from datetime import datetime
def diff(date1: str, date2: str, date_format: str = "%Y-%m-%d %H:%M:%S") -> int:
    dt1 = datetime.strptime(date1, date_format)
    dt2 = datetime.strptime(date2, date_format)
    return abs(int((dt2 - dt1).total_seconds()))

date1 = "2024-02-14 12:01:00"
date2 = "2023-02-15 14:50:00"
print(diff(date1, date2))
            
