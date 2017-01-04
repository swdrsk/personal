import math
import numpy

class Node(object):
    def __init__(self, key):
        """
        kyes must be list
        """
        self.key = key
        self.height = 0
        self.parent = None
        self.higherChild = None
        self.lowerChild = None


class AVL(object):
    def insert(self, x):
        self.keys.append(x)

    def delete(self):
        pass

    def find(self):
        pass

    def sort(self):
        pass
