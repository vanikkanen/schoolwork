import math
import pickle
import numpy as np
import matplotlib.pyplot as plt
import time
import skimage.transform as st
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import keras


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


def one_hot_inputs(Y):

    one_hots = np.zeros([len(Y), 10])
    for i in range(len(Y)):
        one_hots[i][Y[i]] = 1
    print(one_hots[0])
    return one_hots

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

# Transform gt labels into one hot vectors
one_hot_tr_gt_labels = one_hot_inputs(tr_gt_labels)
