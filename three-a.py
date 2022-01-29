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

for i in range(37,43) :
    if R[i] == 'O' and R[i-1] != 'O' :
        plt.plot(x1[i],y1[i],'co')
    elif act[i] == 'S' :
        plt.plot(x1[i], y1[i], 'ro')
        
    if act[i]=='P' :
        plt.plot([x1[i],x2[i]],[y1[i],y2[i]],'silver')
    elif act[i] =='C' :
        plt.plot([x1[i],x2[i]],[y1[i],y2[i]],'tan')
    elif act[i] == 'S' :
        plt.plot([x1[i], x2[i]], [y1[i], y2[i]], 'r')
    elif act[i] == 'K' :
        plt.plot([x1[i],x2[i]], [y1[i],y2[i]], 'b')
        
plt.tight_layout()
plt.show()

