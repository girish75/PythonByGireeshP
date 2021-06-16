import datetime
"""https://docs.python.org/3/library/datetime.html#module-datetime"""
# syntax: class datetime.time(hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
print(datetime.time(13, 57, 0)) # integers as input of this function
print(datetime.date.today()) # print todays date.
#display the current date and time both:
x = datetime.datetime.now() #The date contains year, month, day, hour, minute, second, and microsecond.
print(x)
print(x.ctime())
print(x.today())
print(x.astimezone())

print(x.date())
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)

x = datetime.datetime(2020, 5, 17)
print(x)

#The strftime() Method
print(x.strftime("%B")) #https://www.w3schools.com/python/python_datetime.asp





