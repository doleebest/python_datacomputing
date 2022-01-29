import pandas_datareader.data as web
import matplotlib.pyplot as plt

samsung = web.DataReader("005930.KS", "yahoo")

date = samsung.index.tolist()
value = samsung['Close'].values.tolist()

d=[]
v=[]

for i in range(len(value)-1) :
    if value[i]>50000 :
        print(date[i],value[i])
        break

when5 = date[i]
value5 = value[i]

print("Goes over 50000 when ", when5)

for k in range [date[i]:]:
    if value[k] *0.8 > value[k+1] :
        print(date[k], value[k])
        break
when2 = date[k]
value2 = value[k]

print("Goes down 20% when ", when2)
