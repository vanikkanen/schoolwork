import numpy as np

print("Reading data...")
X_train = np.loadtxt("X_train.dat")
Y_train = np.loadtxt("y_train.dat")
X_test = np.loadtxt("X_test.dat")
Y_test = np.loadtxt("y_test.dat")

print("Done!")
print("Computing baseline")
baseline = np.average(Y_train)
print("Baseline accuracy (MAE)")
mae = np.mean(np.abs(Y_test - baseline))
print(mae)



