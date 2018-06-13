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

#avx = totalx / n
#avy = totaly / n

for j in range(5):
    
    avx = np.random.rand()*4 - 2
    avy = np.random.rand()*4 - 2
    
    print("random x is:",avx)
    print("random y is:",avy)
    
    newvalues = []
    
    for x,y in values:
        x = x - avx
        y = y - avy
        newvalues.append([x,y])
    
    #print(newvalues)
    
    final = np.array(newvalues)
    
    
    w = np.random.rand(2)
    print("w at first is",w)
    
    #ws = [w]
    
    for i in range(100000):
        u = final[i%len(final)]
        v = np.dot(u, w) 
        w = w + 0.01*(v*u - v*v*w)
        #ws.append(w)
    
    print("w converges at",w)
    
    fig, ax = plt.subplots()
    ax.scatter(final[:,0],final[:,1])
    plt.show()
    
    fig, ax = plt.subplots()
    ax.scatter(w[0],w[1])
    plt.show()
