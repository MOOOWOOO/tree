# coding: utf-8
from binary_tree import BinaryNode, BinaryTree

__author__ = 'Jux.Liu'


class BinarySearchTree(BinaryTree):
    def append_node(self, base_node=None, node=BinaryNode()):
        if base_node is None:
            base_node = self.root

        if node < base_node:
            if base_node.left_child is None:
                node.data['l'] = '/'
                base_node.left_child = node
                return True
            else:
                base_node = self.root.left_child
                subtree = BinarySearchTree(node=base_node)
                return subtree.append_node(base_node=base_node, node=node)
        elif node > base_node:
            if base_node.right_child is None:
                node.data['l'] = '\\'
                base_node.right_child = node
                return True
            else:
                base_node = self.root.right_child
                subtree = BinarySearchTree(node=base_node)
                return subtree.append_node(base_node=base_node, node=node)
        else:
            return False


if __name__ == '__main__':
    node1 = BinaryNode(data=1)
    node2 = BinaryNode(data=2)
    node3 = BinaryNode(data=3)
    node4 = BinaryNode(data=4)
    node5 = BinaryNode(data=5)
    root = node4

    tree = BinarySearchTree(root)

    for item in [node3, node1, node2,  node5]:
        tree.append_node(base_node=root, node=item)
        tree.layorder(base_node=root)
        print("========")
    tree.layorder()
