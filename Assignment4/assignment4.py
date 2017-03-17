import random


def importance(attributes, examples):
    return random.randint(0, 10)

def plurality_value(a):
    print "plurality"

def decision_tree_learning(examples, attributes, parent_examples):
    if not examples:
        return plurality_value(parent_examples)
    elif examples:
        return "Classification"
    elif not attributes:
        return plurality_value(examples)
    else:
        A = 0
        for a in attributes:
            i = importance(a, examples)
            if i > A:
                A = i
        tree = A
        for vk in A:
            exs = something
            subtree = decision_tree_learning(exs, attributes-A, examples)
            add branch to tree with label A= vk and subtree subtree
    return tree

importance(1, 2)
