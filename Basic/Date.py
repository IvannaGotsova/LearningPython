import datetime as dt

datetimeNow = dt.datetime.now()
print(datetimeNow)

print(datetimeNow.strftime("%A"))
print(datetimeNow.strftime("%B"))
print(datetimeNow.strftime("%Y"))
print(datetimeNow.strftime("%H"))
print(datetimeNow.strftime("%M"))
print(datetimeNow.strftime("%S"))