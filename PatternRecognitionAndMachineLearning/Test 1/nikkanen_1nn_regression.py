import numpy as np
from scipy.spatial import distance

print("Reading data...")
X_train = np.loadtxt("X_train.dat")
Y_train = np.loadtxt("y_train.dat")
X_test = np.loadtxt("X_test.dat")
Y_test = np.loadtxt("y_test.dat")
print("Done!")

print("Computing baseline")
baseline = np.average(Y_train)
print("Baseline accuracy (MAE)")
baseline_mae = np.mean(np.abs(Y_test - baseline))
print(baseline_mae)
print(Y_test.shape)

nn_array = np.empty([102, 1])
for j in range(0, len(Y_test)):
    closest_dist = 10000000
    test_y = Y_test[j]
    test_x = X_test[j]
    point1 = np.array((X_test[j], Y_test[j]))
    for k in range(0, len(Y_train)):
        train_y = Y_train[k]
        train_x = X_train[k]
        point2 = np.array((X_train[k], Y_train[k]))
        dist = distance.euclidean(point1,point2)
        if dist < closest_dist:
            closest_dist = dist
    nn_array[j] = closest_dist

