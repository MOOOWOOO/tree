# coding: utf-8

__author__ = 'Jux.Liu'


class BinaryNode(object):
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __repr__(self):
        return str(self.data)

    def __eq__(self, other):
        if other is None or self is None:
            return False
        else:
            return self.data == other.data

    def __lt__(self, other):
        if self is None:
            return False
        elif other is None:
            return True
        else:
            return self.data < other.data

    def __gt__(self, other):
        if self is None:
            return False
        elif other is None:
            return True
        else:
            return self.data > other.data
