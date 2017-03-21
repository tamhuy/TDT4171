import random
import math


class Node:
    def __init__(self, data, leaf):
        self.data = data
        self.children = {}
        self.leaf = leaf

    def add_child(self, key, value):
        self.children[key] = value


def B(q):
    if q == 1 or q == 0:
        return 0
    return -(q * math.log(q, 2) + (1 - q) * math.log(1 - q, 2))


def argmax(examples, attributes, rand):
    if rand:
        return random.choice(attributes)
    else:
        gain = []
        for a in attributes:
            gain.append(importance(a, examples))
        return attributes[gain.index(max(gain))]


def importance(a, examples):
    # E0 = [p0, n0]
    # E1 = [p1, n1]
    # E = [E0, E1] = [[p0, n0], [p1, n1]]
    # p = 1, n = 2
    E = [[0.0, 0.0], [0.0, 0.0]]
    for example in examples:
        if example[a] == 1 and example[len(example) - 1] == 1:
            E[0][0] += 1
        elif example[a] == 1 and example[len(example) - 1] == 2:
            E[0][1] += 1
        elif example[a] == 2 and example[len(example) - 1] == 1:
            E[1][0] += 1
        elif example[a] == 2 and example[len(example) - 1] == 2:
            E[1][1] += 1
    p = E[0][0] + E[1][0]
    n = E[0][1] + E[1][1]
    remainder = 0
    for j in range(2):
        remainder += (E[j][0] + E[j][1])/(p + n) * B(E[j][0]/(E[j][0]+E[j][1]))
    return B(p/(p+n)) - remainder


def plurality_value(a):
    return max(set(a), key=a.count)


def decision_tree_learning(examples, attributes, parent_examples, rand):
    qwe = []
    for example in examples:
        qwe.append(example[len(example)-1])
    if not examples:
        return Node(plurality_value(parent_examples), True)
    elif len(set(qwe)) == 1:
        return Node(set(qwe).pop(), True)
    elif not attributes:
        return Node(plurality_value(qwe), True)
    else:
        A = argmax(examples, attributes, rand)
        root = Node(A, False)
        for vk in range(1, 3):
            exs = []
            for example in examples:
                if example[A] == vk:
                    exs.append(example)
            copy = list(attributes)
            copy.remove(A)
            subtree = decision_tree_learning(exs, copy, examples, rand)
            root.add_child(vk, subtree)
    return root


def readfile(file):
    # Open training data and put it in a 2D list
    with open(file, "r") as f:
        data = f.readlines()
    list = []
    for line in data:
        list.append([int(i) for i in line.split()])
    #for i in examples:
    #    print i
    return list


def count(tree, test):
    while not tree.leaf:
        if test[tree.data] == 1:
            tree = tree.children[1]
        else:
            tree = tree.children[2]
    return tree.data


def main():
    examples = readfile("data/training.txt")
    attributes = [x for x in range(len(examples[0])-1)]
    tree = decision_tree_learning(examples, attributes, None, False)
    test = readfile("data/test.txt")
    counter = 0
    for line in test:
        if count(tree, line) == line[len(line)-1]:
            counter += 1
    print counter
main()
