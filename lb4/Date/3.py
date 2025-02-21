from datetime import datetime
now=datetime.now()
new_time=now.replace(microsecond=0)
print(now)
print("------------")
print(new_time)