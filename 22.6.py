import pandas_datareader.data as web
import matplotlib.pyplot as plt

samsung = web.DataReader("005930.KS","yahoo")

date = samsung.index.tolist()
value = samsung['Close'].values.tolist()

d=[]
v=[]

for i in range(len(value)-1) :
    if value[i+1]>value[i]*1.05 :
        d.append(date[i])
        v.append(value[i])

for i in range(len(value)-1) :
    if value[i+1]*1.05<value[i]:
        d.append(date[i])
        v.append(value[i])

        
        
plt.plot(date,value)
plt.plot(d,v,'ro')

plt.show()


