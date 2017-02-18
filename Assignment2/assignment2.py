import numpy as np

uT = np.array([[0.9, 0.0], [0.0, 0.2]]) # Chance of rain given umbrella
uF = np.array([[0.1, 0.0], [0.0, 0.8]]) # Chance of rain given no umbrella
xt1xt = np.array([[0.7, 0.3], [0.3, 0.7]])  # Chance that it rains given weather the day before
initial = np.array([0.5, 0.5])
evidence = [True, True, False, True, True]    # Sequence of observations
evidence2 = [True, True]  # Used for checking if results are the same as in the book/slides


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
def forwardbackward(ev, prior):
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
        print "Smoothed Value: ", sv[i]
    return sv


# Based on equation 5.11 on page 577
def viterbi(ev, prior):
    xt, xf = np.array([None] * len(ev)), np.array([None] * len(ev))     # Initializing empty arrays
    init = forward([ev[0]], prior)  # Initial values
    xt[0], xf[0] = init[0], init[1]

    for i in range(1, len(ev)):
        if ev[i]:   # If an umbrella is observed
            xt[i] = (uT[0][0] * max(xt1xt[0][0] * xt[i-1], xt1xt[0][1] * xf[i-1]))
            xf[i] = (uT[1][1] * max(xt1xt[0][1] * xt[i-1], xt1xt[0][0] * xf[i-1]))
        else:       # If an Umbrella is not observed
            xt[i] = (uF[0][0] * max(xt1xt[0][0] * xt[i-1], xt1xt[0][1] * xf[i-1]))
            xf[i] = (uF[1][1] * max(xt1xt[0][1] * xt[i-1], xt1xt[0][0] * xf[i-1]))
    print "xT: ", xt
    print "xF: ", xf


def main():
    print "Forward: "
    forward(evidence, initial)         # Task B

    print "\n", "-"*10
    print "Forward-Backward: "
    forwardbackward(evidence, initial)  # Task C

    print "\n", "-" * 10
    print "Viterbi: "
    viterbi(evidence, initial)          # Task C

main()
