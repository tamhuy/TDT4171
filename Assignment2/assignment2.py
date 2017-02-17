import numpy as np
'''
x0 = np.matrix('0.5; 0.5')
e1x1 = np.matrix('0.9 0.0; 0.0 0.2')
x1x0 = np.matrix('0.7 0.3; 0.3 0.7')
#print(x0)
#print(x1x0)
x1 = x1x0 * x0
x1e1 = e1x1 * x1
alpha = 1/np.sum(x1e1)
x1e1 = alpha*x1e1

x2e1 = x1x0 * x1e1

x2e12 = e1x1 * x2e1
#print x2e12
alpha = 1/np.sum(x2e12)
#print "alpha: ", alpha
x2e12 = alpha * x2e12

#print "alpha: ", alpha
#print "x1: ", x1
##print "x1e1: ", x1e1
#print "x2e1", x2e1
#print "x2e12", x2e12
'''

def filtering(evidence):
    uT = np.matrix('0.9 0.0; 0.0 0.2')  # Chance of rain given umbrella
    uF = np.matrix('0.1 0.0; 0.0 0.8')  # Chance of rain given no umbrella
    xt1xt = np.matrix('0.7 0.3; 0.3 0.7')   # Chance that it rains given weather the day before
    if len(evidence) == 0:  # Base case of the recursion
        return np.matrix('0.5; 0.5')    # Chance of rain given no prior information is 50/50
    else:
        x = xt1xt * filtering(evidence[0:len(evidence)-1])  # Recursive call
        if evidence[-1]:    # If an umbrella is observed
            xe = uT * x
        else:               # If an umbrella is not observed
            xe = uF * x
        xe = (1/np.sum(xe)) * xe    # Normalization
        print xe
    return xe

filtering([True, True, False, True, True])



def forwardBackward(ev, prior):
    sad = 0