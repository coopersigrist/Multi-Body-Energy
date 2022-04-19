import matplotlib
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

data = np.load('phoh_train_idx.npy')

print(data.shape)

data = np.load('train_idx.npy')

print(data.shape)


data = np.load('../abs_pos_phoh.npy')

print(data.shape)
print(data[0][0:14].T)
mol = data[0][0:14].T

ax.scatter(mol[0], mol[1], mol[2])

plt.show()

data = np.load('../y_phoh.npy')

print(data.shape)