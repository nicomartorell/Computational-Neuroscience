import numpy as np
import matplotlib.pyplot as plt

# 1. Creo mi eje r de 0 a 20
# 2. Creo para cada r un valor de acuerdo a una gaussiana.
#       Esto lo hago dos veces, una con u=5, s=0.5, otra u=7 s=1.
# 3. Divido la segunda por la primera y guardo eso en una nueva lista.
# 4. Paso por todos los tuples (r, f(r)) y el primero que sea mayor o
#       igual a 2 lo imprimo. Ese es el valor que estoy buscando.

"""def gaussian(x, mu, sig):
    return 1./(np.sqrt(2.*np.pi)*sig)*np.exp(-np.power((x - mu)/sig, 2.)/2)

r = np.arange(0, 20, 0.01)

g1 = [gaussian(ri, 5, 0.5) for ri in r]
g2 = [gaussian(ri, 7, 1) for ri in r]
ratio = [gaussian(ri, 5, 0.5)/gaussian(ri, 7, 1) for ri in r]

myr = 0

for x in ratio:
    if x >= 2:
        print("r is", myr, "and the ratio is", x)
        break
    else:
        myr += 0.01

fig, ax = plt.subplots()
ax.plot(r, g1)
ax.set(xlabel="r", ylabel="p", title="Gaussian 1")
fig.savefig("g1.png")
plt.show()

fig, ax = plt.subplots()
ax.plot(r, g2)
ax.set(xlabel="r", ylabel="p", title="Gaussian 2")
fig.savefig("g2.png")
plt.show()

fig, ax = plt.subplots()
ax.plot(r, ratio)
ax.set(xlabel="r", ylabel="p", title="Ratio")
fig.savefig("ratio.png")
plt.show()"""

thresholds = np.arange(0, 10, 0.01)
p = np.zeros(thresholds.shape)

total = 500
size = 10000

samples1 = np.random.normal(5, 0.5, size)
samples2 = np.random.normal(7, 1, size)

i = 0

for threshold in thresholds:
    start = int(np.random.rand()*(size-2*total) + total)
    count = 0
    for x in range(start, start + total):
        r = np.random.rand()
        t = 0
        if r < 0.5:
            t = samples1[x]
        else:
            t = samples2[x]
        if (t < threshold and r < 0.5) or (t > threshold and r > 0.5):
            count += 1
    
    pi = count / total
    p[i] = pi
    i+=1
    print("finished i:",i)
    #print("For threshold", threshold, "the proportion of right answers is", p)

fig, ax = plt.subplots()
ax.plot(thresholds, p)
ax.set(xlabel="thresholds", ylabel="p", title="Threshold effectivness")
fig.savefig("thresholds.png")
plt.show()
