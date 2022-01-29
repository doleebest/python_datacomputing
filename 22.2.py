import pandas
from datetime import datetime
import matplotlib.pyplot as plt

df = pandas.read_csv('ewhadorm.csv')
d=df['Updated At'].values.tolist()
d.sort()

print(d[:2])

dt=[]
for a in d :
    dt.append(datetime.strptime(a,'%Y-%m-%dT%H:%M:%SZ'))

print(dt[:2])

plt.plot(dt,range(len(dt)))
plt.show()
