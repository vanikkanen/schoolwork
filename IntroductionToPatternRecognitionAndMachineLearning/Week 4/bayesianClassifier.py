import math
import pickle
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import multivariate_normal
import time
import skimage.transform as st


def unpickle(file):
    with open(file, 'rb') as f:
        dict = pickle.load(f, encoding="latin1")
    return dict


def class_acc(pred, gt):
    # Code comparing the 2 vectors
    nppred = np.array(pred)
    npgt = np.array(gt)

    data = len(nppred)
    correct = np.count_nonzero(nppred == npgt)
    return correct / data


def cifar10_classifier_random(x):
    # Return the correct size vector filled with random numbers from {0,9}
    x = np.array(x)
    data = len(x)
    return np.random.randint(9, size=(data))


def cifar10_color(X):
    print("Calculating average colors for training data")
    Xp = np.empty([len(X), 3])

    for i in range(X.shape[0]):
        if (i % 1000 == 0):
            print(i, "/", len(X))

        red = np.average(X[i][:, :, 0])
        green = np.average(X[i][:, :, 1])
        blue = np.average(X[i][:, :, 2])
        Xp[i] = [red, green, blue]

    return Xp


def cifar10_2x2_color(X):
    print("Calculating average colors for training data")
    Xf = np.empty([len(X), 2, 2, 3])
    for i in range(X.shape[0]):
        Xf[i] = 255 * (st.resize(X[i], (2, 2)))

    return Xf

def cifar10_YxY_color(X, size):
    print("Calculating average colors for training data")
    Xd = np.empty([len(X), size, size, 3])
    for i in range(X.shape[0]):
        Xd[i] = 255 * (st.resize(X[i], (size, size)))

    return Xd

def cifar_10_naivebayes_learn(Xp, Y):
    # Calculate p
    print("Calculating p")
    p = np.zeros([10, 1])
    for i in range(len(Y)):
        classID = Y[i]
        p[classID] += 1
    p = p / len(Y)

    # Calculate mu
    print("Calculating mu")
    mu = np.zeros([10, 3])
    for i in range(len(Xp)):
        classID = Y[i]
        mu[classID] += Xp[i]
    for j in range(len(p)):
        mu[j] = mu[j] / (len(Xp) * p[j])

    # Calculate sigma
    print("Calculating sigma")
    sigma = np.zeros([10, 3])
    for i in range(len(Xp)):
        classID = Y[i]
        sigma[classID] += np.square(Xp[i] - mu[classID])
    for j in range(len(p)):
        sigma[j] = sigma[j] / ((len(Xp) - 1) * p[j])

    return mu, sigma, p


def cifar10_classifier_naivebayes(x, mu, sigma, p):
    print("Calculating naive Bayes classifiers and predictions based on them")
    predictions = []
    for i in range(len(x)):
        if (i % 1000 == 0):
            print(i, "/", len(x))
        best_prediction = 0
        class_prediction = -1
        for j in range(10):

            new_prediction = norm.pdf(x[i][0], mu[j][0],
                                      np.sqrt(sigma[j][0])) * \
                             norm.pdf(x[i][1], mu[j][1],
                                      np.sqrt(sigma[j][1])) * \
                             norm.pdf(x[i][2], mu[j][2],
                                      np.sqrt(sigma[j][2])) * \
                             p[j]

            if new_prediction > best_prediction:
                best_prediction = new_prediction
                class_prediction = j

        predictions.append(class_prediction)

    return predictions


def cifar_10_bayes_learn(Xf, Y):
    # Calculate p
    print("Calculating better p")
    p = np.zeros([10, 1])
    for i in range(len(Y)):
        classID = Y[i]
        p[classID] += 1
    p = p / len(Y)

    # Need to split the images to their own arrays to calculate covariance
    # matrix
    data_by_class = {}
    for i in range(len(p)):
        data = np.zeros([int(p[0] * len(Y)), Xf.shape[1]])
        iter = 0
        for j in range(Xf.shape[0]):
            if Y[j] == i:
                data[iter] = Xf[j]
                iter += 1
        data_by_class[i] = data

    # Calculate mu
    print("Calculating better mu")
    mu = np.zeros([len(p), Xf.shape[1]])
    for i in range(len(p)):
        class_mu = np.average(data_by_class[i], axis=0)
        mu[i] = class_mu

    # Calculate sigma
    print("Calculating better sigma")
    sigma = np.zeros([len(p), Xf.shape[1], Xf.shape[1]])
    for i in range(len(p)):
        class_sigma = np.cov(data_by_class[i].T)
        sigma[i] = class_sigma

    return mu, sigma, p


def cifar10_classifier_bayes(x, mu, sigma, p):
    print("Calculating better Bayes classifiers and predictions based on them")
    predictions = []
    for i in range(len(x)):
        if (i % 1000 == 0):
            print(i, "/", len(x))
        best_prediction = 0
        class_prediction = -1
        for j in range(len(p)):

            new_prediction = multivariate_normal.pdf(x[i].T, mu[j],
                                                     sigma[j])*p[j]

            if new_prediction > best_prediction:
                best_prediction = new_prediction
                class_prediction = j
        predictions.append(class_prediction)

    return predictions


def cifar10_classifier_1nn(x, trdata, trlabels):
    # Classify the data of x with the trdata with 1-NN principle and return a
    # vector with the predicted labels
    start_time = time.time()
    predictions = []

    for i in range(x.shape[0]):
        print(i)
        min_dist = 0
        min_dist_iterator = 0
        for j in range(trdata.shape[0]):
            # dist = np.sum(np.square(np.array(x[i]) - np.array(trdata[j])))
            dist = np.sum(np.abs(np.array(x[i]) - np.array(trdata[j])))
            if min_dist == 0 or min_dist > dist:
                min_dist = dist
                min_dist_iterator = j

        predictions.append(trlabels[min_dist_iterator])

    end_time = time.time()
    print("Elapsed time: ", end_time - start_time)
    return np.array(predictions)


def distance(pointA, pointB, _norm=np.linalg.norm):
    return _norm(pointA - pointB)


# Training data

datadict1 = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML'
                     '/cifar-10-batches-py/data_batch_1')
datadict2 = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML'
                     '/cifar-10-batches-py/data_batch_2')
datadict3 = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML'
                     '/cifar-10-batches-py/data_batch_3')
datadict4 = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML'
                     '/cifar-10-batches-py/data_batch_4')
datadict5 = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML'
                     '/cifar-10-batches-py/data_batch_5')

trdata1 = datadict1["data"]
trdata2 = datadict2["data"]
trdata3 = datadict3["data"]
trdata4 = datadict4["data"]
trdata5 = datadict5["data"]

trdata = np.append(np.append(np.append(np.append(
    trdata1, trdata2, axis=0), trdata3, axis=0), trdata4, axis=0),
    trdata5, axis=0)

trdata = trdata.reshape(50000, 3, 32, 32).transpose(0, 2, 3, 1).astype(
    "uint8")

# Labels for training data

labels1 = datadict1["labels"]
labels2 = datadict2["labels"]
labels3 = datadict3["labels"]
labels4 = datadict4["labels"]
labels5 = datadict5["labels"]

tr_gt_labels = np.append(np.append(np.append(np.append(
    labels1, labels2, axis=0), labels3, axis=0), labels4, axis=0),
    labels5, axis=0)

labeldict = unpickle(
    'C:/Users/vanik/PycharmProjects/Intro to ML/cifar-10-batches-py/batches.meta')
label_names = labeldict["label_names"]

# Testing data

testdict = unpickle(
    'C:/Users/vanik/PycharmProjects/Intro to ML/cifar-10-batches-py/test_batch')
testdata = testdict["data"]
test_gt_labels = testdict["labels"]

testdata = testdata.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype(
    "uint8")

tr_gt_labels = np.array(tr_gt_labels)

# Calculate random accuracy
rand = cifar10_classifier_random(tr_gt_labels)
print("Random accuracy: ", class_acc(rand, tr_gt_labels))

# Calculate average colors in 1x1 px training images
Xp = cifar10_color(trdata)

# Resize test images to 1px
print("Resizing test images to 1px")
testdata_1px = np.zeros([testdata.shape[0], 3])
for i in range(testdata.shape[0]):
    testdata_1px[i] = 255 * (st.resize(testdata[i], (1, 1)))


# Learn from training data for naive version
naive_mu, naive_sigma, naive_p = cifar_10_naivebayes_learn(Xp, tr_gt_labels)

# Naively classify resized test images
naive_predictions = cifar10_classifier_naivebayes(testdata_1px, naive_mu,
                                                  naive_sigma, naive_p)
print("Naive Bayes classifier accuracy: ", class_acc(naive_predictions,
                                                     test_gt_labels))

# Learn from training data for better version
better_mu, better_sigma, better_p = cifar_10_bayes_learn(Xp, tr_gt_labels)

# Classify resized test images
better_predictions = cifar10_classifier_bayes(testdata_1px, better_mu,
                                              better_sigma, better_p)

print("Better Bayes classifier accuracy: ", class_acc(better_predictions,
                                                      test_gt_labels))


# Resize test images to 2x2px
print("Resizing test images to 2x2px")
testdata_2x2px = np.zeros([testdata.shape[0], 2, 2, 3])
for i in range(testdata.shape[0]):
    testdata_2x2px[i] = 255 * (st.resize(testdata[i], (2, 2)))

testdata_2x2px = testdata_2x2px.reshape(testdata.shape[0], 12)
print(testdata_2x2px.shape)

# Calculate average colors in 2x2 px training images
Xf = cifar10_2x2_color(trdata)
Xf = Xf.reshape(Xf.shape[0], 12)

# Learn from training data for better version
best_mu, best_sigma, best_p = cifar_10_bayes_learn(Xf, tr_gt_labels)

# Classify resized test images
best_predictions = cifar10_classifier_bayes(testdata_2x2px, best_mu,
                                              best_sigma, best_p)

print("2x2 Bayes classifier accuracy: ", class_acc(best_predictions,
                                                      test_gt_labels))

# 4x4
Y = 4
# Resize test images to 4x4px
print("Resizing test images to 4x4px")
testdata_4x4px = np.zeros([testdata.shape[0], Y, Y, 3])
for i in range(testdata.shape[0]):
    testdata_4x4px[i] = 255 * (st.resize(testdata[i], (Y, Y)))

testdata_4x4px = testdata_4x4px.reshape(testdata.shape[0], Y*Y*3)

# Calculate average colors in 4x4 px training images
Xd = cifar10_YxY_color(trdata, Y)
Xd = Xd.reshape(Xd.shape[0], Y*Y*3)

# Learn from training data for better version
best_mu, best_sigma, best_p = cifar_10_bayes_learn(Xd, tr_gt_labels)
best_predictions = cifar10_classifier_bayes(testdata_4x4px, best_mu,
                                              best_sigma, best_p)

print("4x4 Bayes classifier accuracy: ", class_acc(best_predictions,
                                                      test_gt_labels))

"""
# 8x8
Y = 8
# Resize test images to 8x8px
print("Resizing test images to 8x8px")
testdata_8x8px = np.zeros([testdata.shape[0], Y, Y, 3])
for i in range(testdata.shape[0]):
    testdata_8x8px[i] = 255 * (st.resize(testdata[i], (Y, Y)))

testdata_8x8px = testdata_8x8px.reshape(testdata.shape[0], Y*Y*3)

# Calculate average colors in 8x8 px training images
Xd = cifar10_YxY_color(trdata, Y)
Xd = Xd.reshape(Xd.shape[0], Y*Y*3)

# Learn from training data for better version
best_mu, best_sigma, best_p = cifar_10_bayes_learn(Xd, tr_gt_labels)
best_predictions = cifar10_classifier_bayes(testdata_8x8px, best_mu,
                                              best_sigma, best_p)

print("8x8 Bayes classifier accuracy: ", class_acc(best_predictions,
                                                      test_gt_labels))


# 16x16
Y = 16
# Resize test images to 16x16px
print("Resizing test images to 16x16px")
testdata_16x16px = np.zeros([testdata.shape[0], Y, Y, 3])
for i in range(testdata.shape[0]):
    testdata_16x16px[i] = 255 * (st.resize(testdata[i], (Y, Y)))

testdata_16x16px = testdata_16x16px.reshape(testdata.shape[0], Y*Y*3)

# Calculate average colors in 16x16 px training images
Xd = cifar10_YxY_color(trdata, Y)
Xd = Xd.reshape(Xd.shape[0], Y*Y*3)

# Learn from training data for better version
best_mu, best_sigma, best_p = cifar_10_bayes_learn(Xd, tr_gt_labels)
best_predictions = cifar10_classifier_bayes(testdata_16x16px, best_mu,
                                              best_sigma, best_p)

print("16x16 Bayes classifier accuracy: ", class_acc(best_predictions,
                                                      test_gt_labels))

# 32x32
Y = 32
# Resize test images to 32x32px
print("Resizing test images to 32x32px")
testdata_32x32px = np.zeros([testdata.shape[0], Y, Y, 3])
for i in range(testdata.shape[0]):
    testdata_32x32px[i] = 255 * (st.resize(testdata[i], (Y, Y)))

testdata_32x32px = testdata_32x32px.reshape(testdata.shape[0], Y*Y*3)

# Calculate average colors in 32x32 px training images
Xd = cifar10_YxY_color(trdata, Y)
Xd = Xd.reshape(Xd.shape[0], Y*Y*3)

# Learn from training data for better version
best_mu, best_sigma, best_p = cifar_10_bayes_learn(Xd, tr_gt_labels)
best_predictions = cifar10_classifier_bayes(testdata_32x32px, best_mu,
                                              best_sigma, best_p)

print("32x32 Bayes classifier accuracy: ", class_acc(best_predictions,
                                                      test_gt_labels))
"""