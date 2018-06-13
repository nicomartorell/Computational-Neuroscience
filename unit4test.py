import pickle
import numpy as np
import matplotlib.pyplot as plt 

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)

with open('pop_coding_3.4.pickle', 'rb') as g:
    data2 = pickle.load(g)

stim = data['stim']
neuron1 = data['neuron1']
neuron2 = data['neuron2']
neuron3 = data['neuron3']
neuron4 = data['neuron4']

r1 = data2['r1']
r2 = data2['r2']
r3 = data2['r3']
r4 = data2['r4']

c1 = data2['c1']
c2 = data2['c2']
c3 = data2['c3']
c4 = data2['c4']

max1 = 32.6
max2 = 21.9

resp1 = np.average(r1)
resp2 = np.average(r2)

sc1 = resp1 / max1
sc2 = resp2 / max2

el1 = sc1 * c1
el2 = sc2 * c2

popv = el1 + el2

angle = np.arctan((-popv[1])/popv[0])

angle = np.degrees(angle)

print(angle)

'''average = np.zeros(stim.shape)
variance = np.zeros(stim.shape)

for i in range(len(stim)):
    col = neuron4[:,i]
    a = np.average(col)
    v = np.var(col)
    average[i] = a
    variance[i] = v

fig, ax = plt.subplots()
ax.scatter(average, variance)

fig.savefig("neuron4-poisson.png")
plt.show()'''
