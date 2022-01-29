import pandas_datareader.data as web
import matplotlib.pyplot as plt

samsung = web.DataReader("005930.KS","yahoo")

date = samsung.index.tolist()
value = samsung['Close'].values.tolist()

for i in range(len(value)) :
    if value[i] > 50000 :
        print(date[i], value[i])
        break

when5 = date[i]
value5=value[i]


print("Goes over 50000 when ",when5)
