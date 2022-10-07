import datetime

def findDay(wanted_date):
    year = int(wanted_date[:4])
    month = int(wanted_date[4:6])
    day = int(wanted_date[6:])
    return datetime.datetime(year, month, day).weekday()

time = "20221009"
day = findDay(time)
print(day)

