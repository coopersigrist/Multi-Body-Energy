import numpy as np
import matplotlib.pyplot as plt


results = np.loadtxt("result--14.txt", skiprows=1)

E_loss = results.T[4]
V_loss = results.T[5]

plt.plot(E_loss, label="validation Loss")
plt.plot(V_loss, label="Test Loss")
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.title("MAE val/test loss for Energy and Potential combined on < 14 atom QM9")
plt.ylim(0,2)
plt.show()

# Finds the mean error in the test data vv

import pandas as pd

arr = pd.read_csv("prediction--7.txt", sep="\t", index_col=None)

conv_arr = arr.drop(arr.columns[[0]], axis=1)

print(arr)

np_arr = conv_arr.to_numpy(dtype=np.float32)

print(np_arr)

err = np_arr.T[2]


sev_test = err.mean()

ft_test = 0.8386515974998474

plt.bar(0.2, sev_test, 0.5, label="< 7 atoms")
plt.bar(0.8, ft_test, 0.5, label="< 14 atoms")
plt.title("Test MAE of model trained on QM9 < 7 atoms")
plt.ylabel("ERROR (MAE)")
plt.show()
