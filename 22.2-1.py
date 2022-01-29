from datetime import datetime, timedelta
now = datetime.now()

print(now)
print(now.year,'년',now.month,'월')

d1 = datetime(2021,1,1)

delta = now-d1
print(delta)

d2=now+timedelta(1)
print(d2)

d3 = now+timedelta(hours=12)
print(d3)
