import pickle
import numpy as np
import matplotlib.pyplot as plt
import time


def unpickle(file):
    with open(file, 'rb') as f:
        dict = pickle.load(f, encoding="latin1")
    return dict


def class_acc(pred, gt):
    #Code comparing the 2 vectors
    nppred = np.array(pred)
    npgt = np.array(gt)

    data = len(nppred)
    correct = np.count_nonzero(nppred == npgt)
    return correct/data


def cifar10_classifier_random(x):
    #Return the correct size vector filled with random numbers from {0,9}
    x = np.array(x)
    data = len(x)
    return np.random.randint(9, size=(data))


def cifar10_classifier_1nn(x, trdata, trlabels):
    #Classify the data of x with the trdata with 1-NN principle and return a
    # vector with the predicted labels
    start_time = time.time()
    predictions = []

    for i in range(x.shape[0]):
        print(i)
        min_dist = 0
        min_dist_iterator = 0
        for j in range(trdata.shape[0]):
            #dist = np.sum(np.square(np.array(x[i]) - np.array(trdata[j])))
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

# Not working distance calculation
def distance_sq(pointA, pointB):
    return (np.sum(
        (np.sum(pointA[:,:,0] - pointB[:,:,0])**2) +
        (np.sum(pointA[:,:,1] - pointB[:,:,1])**2) +
        (np.sum(pointA[:,:,2] - pointB[:,:,2])**2)
        ))

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

print(trdata.shape)

# Labels for training data

labels1 = datadict1["labels"]
labels2 = datadict2["labels"]
labels3 = datadict3["labels"]
labels4 = datadict4["labels"]
labels5 = datadict5["labels"]

tr_gt_labels = np.append(np.append(np.append(np.append(
    labels1, labels2, axis=0), labels3, axis=0), labels4, axis=0),
    labels5, axis=0)

labeldict = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML/cifar-10-batches-py/batches.meta')
label_names = labeldict["label_names"]

print(tr_gt_labels.shape)

# Testing data

testdict = unpickle('C:/Users/vanik/PycharmProjects/Intro to ML/cifar-10-batches-py/test_batch')
testdata = testdict["data"]
test_gt_labels = testdict["labels"]

testdata = testdata.reshape(10000, 3, 32, 32).transpose(0, 2, 3, 1).astype("uint8")


tr_gt_labels = np.array(tr_gt_labels)

rand = cifar10_classifier_random(tr_gt_labels)
print("Random accuracy: ", class_acc(rand, tr_gt_labels))


predictions = cifar10_classifier_1nn(testdata[0:100], trdata, tr_gt_labels)
print("Comparing all test data to all training data: ", class_acc(predictions,
                                                   test_gt_labels[0:100]))
