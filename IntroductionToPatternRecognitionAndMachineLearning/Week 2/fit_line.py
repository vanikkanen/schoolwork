'''
DATA.ML.100 # Purpose of code
Creator: Valtteri Nikkanen
Student number: 282688
'''

import matplotlib.pyplot as plt
import numpy as np

x = []
y = []


def my_linfit(x, y):

    b = (np.sum(((np.sum(y*x))/(np.sum(x*x)))*x) - np.sum(y)) / (np.sum(((np.sum(x))/(np.sum(x*x)))*x - 1))
    a = (np.sum(y*x)-b*np.sum(x))/(np.sum(x*x))
    return a, b


def onclick(event):

    if str(event.button) == "MouseButton.LEFT":
        x.append(event.xdata)
        y.append(event.ydata)

        # Draw the clicked point
        plt.plot(event.xdata, event.ydata, marker="o")
        plt.show()

    elif str(event.button) == "MouseButton.RIGHT":

        # Disconnect the drawing capability
        fig.canvas.mpl_disconnect(cid)

        # Convert to numpy for linfit function
        npx = np.array(x)
        npy = np.array(y)
        a, b = my_linfit(npx, npy)

        # Plot the fitted line
        plt.plot(npx, npy, 'kx')
        xp = np.arange(-2, 5, 0.1)
        plt.plot(xp, a * xp + b, 'r')
        print(f"My fit : a={a} and b={b}")
        plt.show()


def main():

    global fig
    fig, ax = plt.subplots()

    plt.xlim(-2, 5)
    plt.ylim(-2, 5)

    global cid
    cid = fig.canvas.mpl_connect('button_press_event', onclick)
    plt.show()


if __name__ == "__main__":
    main()
