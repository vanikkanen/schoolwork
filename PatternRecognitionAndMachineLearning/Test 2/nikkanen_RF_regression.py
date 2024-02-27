import numpy as np

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

print("Computing RF regression results")
y_mean = np.mean(Y_train)
y_predict = np.full(Y_test.shape, y_mean)
MAE = mean_absolute_error(Y_test, y_predict)
print(f" Baseline accuracy (MAE): {round(MAE, 3)}")

RF = RandomForestRegressor()
RF.fit(X_train, Y_train)
y_predict = RF.predict(X_test)
MAE_rf = mean_absolute_error(Y_test, y_predict)
print(f" RF regr. accuracy (MAE): {round(MAE_rf, 3)}")
