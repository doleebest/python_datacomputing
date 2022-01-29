import pandas
import matplotlib.pyplot as plt

df = pandas.read_csv('match.csv')
ply = df['player'].values.tolist()
x1 = df['X_1'].values.tolist()
y1 = df['Y_1'].values.tolist()
x2 = df['X_2'].values.tolist()
y2 = df['Y_2'].values.tolist()
act = df['Activity'].values.tolist()
R = df['Result'].values.tolist()

plt.figure(figsize=(7,10))
plt.axis([0,70,100,0])

im = plt.imread("ground.jpg")
plt.imshow(im,extent=[0,70,0,100])

for i in range(len(x1)) :
    plt.plot([x1[i],x2[i]],[y1[i],y2[i]], 'silver')

plt.tight_layout()
plt.show()
