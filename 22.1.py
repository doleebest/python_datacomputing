import pandas
from operator import itemgetter

df = pandas.read_csv('ewhadorm.csv')
d = df[['Comments', 'Like Count']].values.tolist()
d.sort(key=itemgetter(1),reverse=True)

print(d[0])
print(d[9])

for (a,b) in d[:10]+d[-5:] :
    print(b,a)
    
