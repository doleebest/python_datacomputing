import matplotlib.pyplot as plt
import pandas_datareader.data as web

samsung = web.DataReader("005930.KS","yahoo")

date = samsung.index.tolist()
value = samsung['Close'].values.tolist()

plt.plot(date,value)

for i in range(len(value)-1) :
    if value[i+1]>value[i]*1.05 :
        print(date[i], value[i])
