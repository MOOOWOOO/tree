# coding: utf-8
from copy import deepcopy

__author__ = 'Jux.Liu'


class BinaryNode(object):
    def __init__(self, data=None, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child


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

    def layorder(self, base_node):
        if base_node is None:
            return
        node_queue = [base_node]
        while node_queue:
            node = node_queue.pop(0)
            print(node.data)
            if node.left_child is None:
                pass
            else:
                node_queue.append(node.left_child)
            if node.right_child is None:
                pass
            else:
                node_queue.append(node.right_child)


    def depth(self, base_node):
        if base_node is None:
            return 0
        else:
            left_depth = self.depth(base_node=base_node.left_child)
            right_depth = self.depth(base_node=base_node.right_child)

            if left_depth >= right_depth:
                return left_depth + 1
            else:
                return right_depth + 1

    def width(self, base_node, layer=1):
        layer_width = {layer: 0}
        if base_node is None:
            pass
        else:
            layer_width[layer] += 1
            left_width = self.width(base_node=base_node.left_child, layer=layer + 1)
            right_width = self.width(base_node=base_node.right_child, layer=layer + 1)

            for k in left_width:
                if k in layer_width:
                    pass
                else:
                    if left_width[k] == 0:
                        # remove totally empty layer
                        continue
                    else:
                        layer_width[k] = 0
                layer_width[k] += left_width[k]

            for k in right_width:
                if k in layer_width:
                    pass
                else:
                    if right_width[k] == 0:
                        # remove totally empty layer
                        continue
                    else:
                        layer_width[k] = 0
                layer_width[k] += right_width[k]

        return layer_width


'''
0           root
          /     \
1        5       8
        /\     /  \
2      2 3    7    6
       | |    |   / \
3      None None 0   4
                 |  /\
4             None  1 None
'''

if __name__ == '__main__':
    node0 = BinaryNode(data=0)
    node1 = BinaryNode(data=1)
    node2 = BinaryNode(data=2)
    node3 = BinaryNode(data=3)
    node4 = BinaryNode(data=4, left_child=node1)
    node5 = BinaryNode(data=5, left_child=node2, right_child=node3)
    node6 = BinaryNode(data=6, left_child=node0, right_child=node4)
    node7 = BinaryNode(data=7)
    node8 = BinaryNode(data=8, left_child=node7, right_child=node6)
    root = BinaryNode(data='root', left_child=node5, right_child=node8)

    tree = BinaryTree(root)
    tree.preorder(base_node=root)
    print('========')
    tree.inorder(base_node=root)
    print('========')
    tree.postorder(base_node=root)
    print('========')
    td = tree.depth(base_node=root)
    print('max depth of the tree from "{tree}" is {depth}'.format(tree=root.data, depth=td))
    print('========')
    tw = tree.width(base_node=root)
    print('each layer\'s width of the tree from "{tree}" is {width}'.format(tree=root.data, width=tw))
    print('========')
    tree.layorder(base_node=root)
