import numpy as np
import pickle
import matplotlib.pyplot as plt

with open('unit7.pickle', 'rb') as f:
    data = pickle.load(f)

#q = [[0.2, 0.1],[0.1, 0.15]]
#values, vectors = np.linalg.eig(q)

#print(values)
#print(vectors)

values = data['c10p1']

n = len(values)
totalx = 0
totaly = 0

for x,y in values:
    #print(x)
    #print(y)
    totalx += x
    totaly += y

avx = totalx / n
avy = totaly / n

print(avx)
print(avy)

newvalues = []

for x,y in values:
    x = x - avx
    y = y - avy
    newvalues.append([x,y])

#print(newvalues)

final = np.array(newvalues)

w = np.random.rand(2)
print(w)

ws = [w]

for i in range(100000):
    u = newvalues[i%len(newvalues)]
    u = np.array(u)
    v = np.dot(u, w) 
    w = w + 0.01*(v*u)
    ws.append(w)

print(w)

#fig, ax = plt.subplots()
#ax.scatter(final[:,0],final[:,1])
#fig.savefig("scatter2.png")
#plt.show()
