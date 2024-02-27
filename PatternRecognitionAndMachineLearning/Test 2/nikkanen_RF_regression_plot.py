import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor

print("Reading data...", end=" ")
X_train = np.loadtxt("X_train.dat")
Y_train = np.loadtxt("y_train.dat")
X_test = np.loadtxt("X_test.dat")
Y_test = np.loadtxt("y_test.dat")
print("Done!")

X_train_shape = X_train.shape
print(f"Shape of training data {X_train_shape}")

MAE_mean = np.zeros(12)
MAE_std = np.zeros(12)

for i in range(1, 13):
    MAE_var = np.zeros(10)
    for j in range(10):
        RF = RandomForestRegressor(max_depth=i)
        RF.fit(X_train, Y_train)
        y_predict = RF.predict(X_test)
        MAE_rf = mean_absolute_error(Y_test, y_predict)
        MAE_var[j] = MAE_rf

    MAE_mean[i-1] = np.mean(MAE_var)
    MAE_std[i-1] = np.std(MAE_var)

plt.errorbar(range(1, 13), MAE_mean, yerr=MAE_std)
plt.xlabel("Max Depth")
plt.ylabel("MAE")
print("Plots ready.")
plt.show()
