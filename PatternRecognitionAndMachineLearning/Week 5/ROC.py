import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import roc_curve

det_output = np.loadtxt("detector_output.dat")
det_gt = np.loadtxt("detector_groundtruth.dat")

# sorting the array from smallest to largest
order = np.argsort(det_output)[::-1]
det_output = np.array(det_output)[order]
det_gt = np.array(det_gt)[order]

positive = sum(det_gt)
negative = len(det_gt) - positive

fpr = [0]
tpr = [0]

# For every possible threshold in the data
for threshold in det_output:

    pred = (det_output >= threshold).astype(int)

    tp = np.sum((pred == 1) & (det_gt == 1))
    fp = np.sum((pred == 1) & (det_gt == 0))

    tpr.append(tp/positive)
    fpr.append(fp/negative)


plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.show()
