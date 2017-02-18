import numpy as np

uT = np.array([[0.9, 0.0], [0.0, 0.2]]) # Chance of rain given umbrella
uF = np.array([[0.1, 0.0], [0.0, 0.8]]) # Chance of rain given no umbrella
xt1xt = np.array([[0.7, 0.3], [0.3, 0.7]])  # Chance that it rains given weather the day before
prior = np.array([0.5, 0.5])
ev = [True, True, False, True, True]    # Sequence of observations
ev2 = [True, True]  # Used for checking if results are the same as in the book/slides


# Based on equation 15.5 on page 572 and on the lecture slides
def forward(ev, prior):
    if not ev:  # Base case of the recursion
        return prior    # Chance of rain given no prior information is 50/50
    else:
        x = np.dot(xt1xt, forward(ev[0:len(ev)-1], prior))  # Recursive call
        if ev[-1]:      # If an umbrella is observed
            xe = np.dot(uT, x)
        else:           # If an umbrella is not observed
            xe = np.dot(uF, x)
        print normalize(xe)
    return normalize(xe)


def normalize(x):
    return x/x.sum()    # Normalization


# Based on equation 15.9 on page 574 and on the lecture slides
def backward(b, ev):
    if ev:  # If an umbrella is observed
        return np.dot(np.dot(uT, b), xt1xt)
    else:   # If an umbrella is not observed
        return np.dot(np.dot(uF, b), xt1xt)


# Based on figure 15.4 on page 576
def forwardBackward(ev, prior):
    fv = np.array([None] * (len(ev) + 1))   # Initialize the vector of forward messages
    sv = np.array([None] * (len(ev) + 1))   # Initialize the vector of backward messages
    fv[0] = prior   # First known step
    b = np.array([1.0, 1.0])    # A representation of backward messages
    print "Forward messages"
    for i in range(1,len(ev) + 1):  # Using the forward function to fill the array with forward messages
        fv[i] = forward([ev[i-1]], fv[i-1])
    for i in range(len(ev), -1, -1): # Using the backward function to update backwards messages
        print "Iteration: ", i
        print "b: ", b
        sv[i] = normalize(np.multiply(fv[i], b))    # Normalize and update backwards messages
        b = backward(b, [ev[i-1]])
    print "Smoothed values: ", sv
    return sv


def viterbi(ev, prior):
    xT, xF = np.array([None] * len(ev)), np.array([None] * len(ev))
    init = forward([ev[0]], prior)
    xT[0], xF[0] = init[0], init[1]     # True

    for i in range(1, len(ev)):
        if ev[i]:
            xT[i] = (uT[0][0] * max(xt1xt[0][0] * xT[i-1], xt1xt[0][1] * xF[i-1]))  # true
            xF[i] = (uT[1][1] * max(xt1xt[0][1] * xT[i-1], xt1xt[0][0] * xF[i-1]))  # true
        else:
            xT[i] = (uF[0][0] * max(xt1xt[0][0] * xT[i-1], xt1xt[0][1] * xF[i-1]))  # false
            xF[i] = (uF[1][1] * max(xt1xt[0][1] * xT[i-1], xt1xt[0][0] * xF[i-1]))  # false
    print "xT: ", xT
    print "xF: ", xF


def main():
    print "Forward: "
    forward(ev, prior)         # Task B

    print "\n", "-"*10
    print "Forward-Backward: "
    forwardBackward(ev, prior)  # Task C

    print "\n", "-" * 10
    print "Viterbi: "
    viterbi(ev, prior)          # Task C

main()