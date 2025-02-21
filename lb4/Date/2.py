from datetime import datetime , timedelta 
today=datetime.now()
yerstoday=today-timedelta(1)
tomorow=today+timedelta(1)
print(today.strftime("%Y-%m-%d"))
print(yerstoday.strftime("%Y-%m-%d"))
print(tomorow.strftime("%Y-%m-%d"))