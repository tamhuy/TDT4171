import random
import math

def B(q):
    if q == 1 or q == 0:
        return 0
    return -(q * math.log(q, 2) + (1 - q) * math.log(1 - q, 2))


def argmax(examples, attributes):
    print "Argmax", "-" * 20
    gain = []
    for a in attributes:
        #print a, "-" *10
        #i = importance(a, examples)
        gain.append(importance(a, examples))
    #print asd.index(max(asd))
    #print asd
    return gain.index(max(gain))


def importance(a, examples):
    # print B(25.0/100)
    # E0 = [n0, p0]
    # E1 = [n1, p1]
    # E = [E0, E1] = [[n0, p0], [n1, p1]]
    # n = 1, p = 2
    E = [[0.0, 0.0], [0.0, 0.0]]
    for example in examples:
        if example[a] == 1 and example[len(example) - 1] == 1:
            E[0][0] += 1
        if example[a] == 1 and example[len(example) - 1] == 2:
            E[0][1] += 1
        if example[a] == 2 and example[len(example) - 1] == 1:
            E[1][0] += 1
        if example[a] == 2 and example[len(example) - 1] == 2:
            E[1][1] += 1
    n = E[0][0] + E[1][0]
    p = E[0][1] + E[1][1]
    #print "n, p: ",  n, p
    print "E: ", E
    # print B(p/(p+n))
    remainder = 0
    for j in range(2):
        remainder += (E[j][1] + E[j][0])/(p + n) * B(E[j][1]/(E[j][1]+E[j][0]))
        #print remainder
    gain = B(p/(p+n)) - remainder
    #print B(p/(p+n))
    return gain


def plurality_value(a):
    return max(set(a), key=a.count)

def decision_tree_learning(examples, attributes, parent_examples):
    if not examples:
        return plurality_value(parent_examples)
    #elif examples:
    #    return "Classification"
    elif not attributes:
        return plurality_value(examples)
    else:
        A = argmax(examples, attributes)
        print "A: ", A
        tree = A
        """
        for vk in A:
            exs = something
            subtree = decision_tree_learning(exs, attributes-A, examples)
            #add branch to tree with label A= vk and subtree subtree
        """
    return tree


# Open training data and put it in a 2D list
with open("data/training.txt", "r") as f:
    data = f.readlines()
examples = []
for line in data:
    examples.append([int(i) for i in line.split()])
for i in examples:
    print i

print '*' * 10
'''
count = 0
for example in examples:
    if example[0] == 2 and example[6] == 2 and example[1] == 2 and example[7] == 2:
        count += 1
        print example
print count
print attributes
'''
attributes= [x for x in range(len(examples[0])-1)]
print attributes
#importance(0, examples)
print decision_tree_learning(examples, attributes, 0)
