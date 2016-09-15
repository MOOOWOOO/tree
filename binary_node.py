# coding: utf-8

__author__ = 'Jux.Liu'


class BinaryNode(object):
    def __init__(self, data=None, left_child=None, right_child=None, parent=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
        self.parent = parent

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

    @property
    def has_left_child(self):
        return self.left_child is not None

    @property
    def has_right_child(self):
        return self.right_child is not None

    @property
    def has_both_child(self):
        return self.has_left_child and self.has_left_child

    @property
    def has_child(self):
        return self.has_left_child or self.has_left_child

    @property
    def is_root(self):
        return self.parent is None

    @property
    def is_leaf(self):
        return not self.has_child

    @property
    def is_left(self):
        return not self.is_root and self == self.parent.left_child

    @property
    def is_right(self):
        return not self.is_root and self == self.parent.right_child
