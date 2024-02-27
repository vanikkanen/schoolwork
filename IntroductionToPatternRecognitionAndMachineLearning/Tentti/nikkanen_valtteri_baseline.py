import numpy as np


def calc_baseline(y):
    print("Computing baseline regression")
    est_y = np.mean(y)
    return est_y

def least_squares_fit(X, y):
    print("Computing 1-dim linear regression")
    parameters = np.zeros([13, 2])
    print(parameters.shape)
    for i in range(X.shape[1]):
        x = np.vstack([X[:, i], np.ones(len(X))]).T
        a, b = np.linalg.lstsq(x, y, rcond=None)[0]
        list = [a, b]
        parameters[i] = np.array(list)
    return parameters


def MAE(predictions, y):
    return 0


print("Reading data... ", end="")
tr_data = np.loadtxt("C:/Users/vanik/PycharmProjects/Intro to "
                     "ML/Tentti/X_train.dat")
test_data = np.loadtxt("C:/Users/vanik/PycharmProjects/Intro to "
                     "ML/Tentti/X_test.dat")
tr_target = np.loadtxt("C:/Users/vanik/PycharmProjects/Intro to "
                     "ML/Tentti/y_train.dat")
test_target = np.loadtxt("C:/Users/vanik/PycharmProjects/Intro to "
                     "ML/Tentti/y_test.dat")
print("Done!")
print(test_target.shape)
regression_results = least_squares_fit(tr_data, tr_target)
predictions = np.zeros([len(test_target)], len(regression_results))
for i in regression_results:
    for j in range(test_target):


print("All done")

#print("    Baseline accuracy ", calc_baseline(tr_target))
