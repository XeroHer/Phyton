import datetime
a=datetime.datetime.now()
print(a)
print(a.year)
print(a.strftime("%A"))  # Output: Current day of the week
x = datetime.datetime(2020, 5, 17)
print(x)
print(x.strftime("%Y-%m-%d"))  # Output: 2020-05-17
print(x.strftime("%B"))  # Output: May
print(x.strftime("%d"))  # Output: 17