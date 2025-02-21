from datetime import datetime , timedelta
now=datetime.now()
second=now-timedelta(seconds=10)
diference=now-second
seconds_difference=diference.total_seconds()
print("first date:",now)
print("second date:",second)
print("diffence:", seconds_difference)

print("----------------------------------------")
dt1 = datetime(2025, 2, 17, 12, 0, 0)
dt2 = datetime(2025, 2, 19, 14, 30, 0)
difference2 = dt2 - dt1
seconds_difference2= difference2.total_seconds()
print("First Date:  ", dt1)
print("Second Date: ", dt2)
print("Difference in seconds:", seconds_difference2)
