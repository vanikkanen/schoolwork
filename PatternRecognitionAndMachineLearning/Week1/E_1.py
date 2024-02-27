'''
DATA.ML.200 # Single neuron gradient descent.
Most of the code was taken from code snippet given in the lecture notebook.
Then the Gradient descent rules were put in to replace the Hebbian learning rules
Creator: Valtteri Nikkanen
Student number: 282688
'''

import matplotlib.pyplot as plt
import numpy as np
from numpy.linalg import inv
from scipy.special import expit

np.random.seed(13)
x_h = np.random.normal(1.1,0.3,5)
x_e = np.random.normal(1.9,0.4,5)
y_h = np.zeros(x_h.shape)
y_h[:] = 0.0
y_e = np.zeros(x_e.shape)
y_e[:] = +1.0

x_tr = np.concatenate((x_h,x_e))
y_tr = np.concatenate((y_h,y_e))

w0_t = 0
w1_t = 0
num_of_epochs = 101
learning_rate = 1.5

for e in range(num_of_epochs):
    for x_ind,x in enumerate(x_tr):
        # Hebbian learning implemented
        y = expit(w1_t*x+w0_t)
        # Hebbian learning method
        #w1_t = w1_t+learning_rate*(y_tr[x_ind]-y)*x
        #w0_t = w0_t+learning_rate*(y_tr[x_ind]-y)*1
        # Gradient descent method
        w1_t = w1_t - learning_rate * (-2 * ((y_tr[x_ind] - y) * x * y * (1 - y)))
        w0_t = w0_t - learning_rate * (-2 * (y_tr[x_ind] - y) * y * (1 - y))

    if np.mod(e,20) == 0 or e == 1 : # Plot after every 20th epoch
        y_pred = expit(w1_t*x_tr+w0_t)
        MSE = np.sum((y_tr-y_pred)**2)/(len(y_tr))
        plt.title(f'Epoch={e} w0={w0_t:.2f} w1={w1_t:.2f} MSE={MSE:.2f}')
        plt.plot(x_h,y_h,'co', label="hobbit")
        plt.plot(x_e,y_e,'mo', label="elf")
        x = np.linspace(0.0,+5.0,50)
        plt.plot(x,expit(w1_t*x+w0_t),'b-',label='y=logsig(w1x+w0)')
        plt.plot([0.5, 5.0],[0.5,0.5],'k--',label='y=0 (class boundary)')
        plt.xlabel('height [m]')
        plt.legend()
        plt.show()

np.set_printoptions(precision=2)
print(f'True values y={y_tr} and predicted values y_pred={y_pred}')
