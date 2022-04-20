import matplotlib
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

data = np.load('phoh_train_idx.npy')

print(data.shape)

data = np.load('train_idx.npy')

print(data.shape)


data = np.load('../data/phoh/abs_pos_phoh.npy')

print(data.shape)
print(data[0][:39].T)
mol = data[0][:39].T

points = list(range(39))

structure = 'HCCHCHCOHCHCH'

# Oxygen is 9th datapoint

ax.scatter(mol[0], mol[1], mol[2])

for i, txt in enumerate(points):
    ax.text(mol[0][i], mol[1][i], mol[2][i], structure[i%13])

plt.show()

data = np.load('../y_phoh.npy')

print(data.shape)
