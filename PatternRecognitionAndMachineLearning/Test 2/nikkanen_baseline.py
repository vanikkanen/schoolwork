import numpy as np
from sklearn.metrics import mean_absolute_error

print("Reading data...", end=" ")
X_train = np.loadtxt("X_train.dat")
Y_train = np.loadtxt("y_train.dat")
X_test = np.loadtxt("X_test.dat")
Y_test = np.loadtxt("y_test.dat")
print("Done!")

print("Computing baseline regression.")
y_mean = np.mean(Y_train)
y_predict = np.full(Y_test.shape, y_mean)

MAE = mean_absolute_error(Y_test, y_predict)
print(f" Baseline accuracy (MAE): {round(MAE, 3)}")
