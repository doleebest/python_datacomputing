import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('match.csv')
ply = df['player'].values.tolist()
x1 = df['X_1'].values.tolist()
y1 = df['Y_1'].values.tolist()
x2 = df['X_2'].values.tolist()
y2 = df['Y_2'].values.tolist()
act = df['Activity'].values.tolist()

P =set(ply)

print('# of plyer', len(P))

for p in P :
    print(p,ply.count(p))
