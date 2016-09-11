# coding: utf-8
from copy import deepcopy

__author__ = 'Jux.Liu'


class BinaryNode(object):
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def insert_left(self, node):
        if self.left_child is None:
            self.left_child = node
        else:
            left_tree = deepcopy(self.left_child)
            self.left_child = node
            node.left_child = left_tree



class BinaryTree(object):
    def __init__(self, node):
        self.node = node

    @property
    def is_empty(self):
        if self.node.data is None:
            return True
        else:
            return False

    def preorder(self, base_node):
        # root - left - right
        if base_node is None:
            return
        print(base_node.data)
        self.preorder(base_node=base_node.left_child)
        self.preorder(base_node=base_node.right_child)

    def inorder(self, base_node):
        # left - root - right
        if base_node is None:
            return
        self.inorder(base_node=base_node.left_child)
        print(base_node.data)
        self.inorder(base_node=base_node.right_child)

    def postorder(self, base_node):
        # left - right - root
        if base_node is None:
            return
        self.postorder(base_node=base_node.left_child)
        self.postorder(base_node=base_node.right_child)
        print(base_node.data)


'''
        root
         /\
        5  4
       /\  /\
      2 3  1 None
      | |  |
      None None
'''

if __name__ == '__main__':
    node1 = BinaryNode(data=1)
    node2 = BinaryNode(data=2)
    node3 = BinaryNode(data=3)
    node4 = BinaryNode(data=4, left_child=node1)
    node5 = BinaryNode(data=5, left_child=node2, right_child=node3)
    root = BinaryNode(data='root', left_child=node5, right_child=node4)

    tree = BinaryTree(root)
    tree.preorder(base_node=root)
    print('========')
    tree.inorder(base_node=root)
    print('========')
    tree.postorder(base_node=root)
