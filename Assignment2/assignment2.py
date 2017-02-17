import numpy as np

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

def filtering(evidence):
    uT = np.matrix('0.9 0.0; 0.0 0.2')
    uF = np.matrix('0.1 0.0; 0.0 0.8')
    xt1xt = np.matrix('0.7 0.3; 0.3 0.7')
    if len(evidence) == 0:
        return np.matrix('0.5; 0.5')
    else:
        x = xt1xt * filtering(evidence[0:len(evidence)-1])
        if evidence[-1]:
            xe = uT * x
        else:
            xe = uF * x
        xe = (1/np.sum(xe)) * xe
        print xe
    return xe


e = [True, True, False, True, True]
filtering(e)
#print e[0:len(e)-1]
