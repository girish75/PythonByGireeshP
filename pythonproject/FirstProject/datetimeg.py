import datetime

print(datetime.MAXYEAR)
print(datetime.MINYEAR)
x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

print(datetime.timezone)
'''
Creating Date Objects
To create a date, we can use the datetime() class (constructor) of the datetime module.
The datetime() class requires three parameters to create a date: year, month, day.
'''
x = datetime.datetime(2020, 5, 17)

 Get Current Date

#GEt current date
date_object = datetime.date.today()
print(date_object)
#Date object to represent a date
d=datetime.date(2019, 4, 13)
print(d)
today = date.today()
print("Current date =", today)
# date object of today's date

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
