import numpy as np
import matplotlib.pyplot as plt

import pickle

FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)

stim = data['rho']

spike_count = 0

for n in stim[149:]:
    spike_count += n

print(spike_count)
    
