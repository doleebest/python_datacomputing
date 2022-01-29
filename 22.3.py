import pandas_datareader.data as web

samsung = web.DataReader("005930.KS","yahoo")

date = samsung.index.tolist()
value = samsung['Close'].values.tolist()

                         
