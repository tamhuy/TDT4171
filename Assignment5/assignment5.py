import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import ImageGrid
import numpy as np
import math

def something():
    a = [1, 2]
    b = [2, 4]
    t, s = [-6, 6], [1, 2]
    fig, ax = plt.subplots()
    ax.plot(a, b)
    ax.grid(True)
    plt.show()


def test():
    x = np.arange(-6, 6, 0.1)
    y = np.arange(-6, 6, 0.1)
    print x
    X, Y = np.meshgrid(x, y)
    print X
    Z = np.zeros(X.shape)
    print Z
    for i in xrange(X.shape[0]):
        for j in xrange(X.shape[1]):
            Z[i, j] = L_simple([X[i, j], Y[i, j]])

    print Z
    plt.pcolormesh(X, Y, Z)
    plt.show()
    print "Min: ", min(Z)


def o(w, x):
    return 1/(1 + math.e ** - np.inner(w, x))


def L_simple(w):
    return (o(w, [0, 1]) - 1) ** 2 + (o(w, [0, 1])) ** 2 + (o(w, [1, 1]) - 1) ** 2

w1 = [-6, 6]
w2 = [-6, 6]
w = [1, 0]

#print L_simple(w)
#print (o(asd, [0, 1]) - 1) ** 2 + (o(asd, [0, 1])) ** 2 + (o(asd, [1,1]) - 1) ** 2
test()
