# coding: utf-8
from binary_tree import BinaryNode, BinaryTree

__author__ = 'Jux.Liu'


class BinarySearchTree(BinaryTree):
    def append_node(self, base_node=None, node=BinaryNode()):
        if base_node is None:
            base_node = self.root

        if isinstance(node, BinaryNode):
            pass
        else:
            node = BinaryNode(data=node)

        if node < base_node:
            if base_node.left_child is None:
                base_node.left_child = node
                base_node.left_child.parent = base_node
                return True
            else:
                base_node = self.root.left_child
                subtree = BinarySearchTree(node=base_node)
                return subtree.append_node(base_node=base_node, node=node)
        elif node > base_node:
            if base_node.right_child is None:
                base_node.right_child = node
                base_node.right_child.parent = base_node
                return True
            else:
                base_node = self.root.right_child
                subtree = BinarySearchTree(node=base_node)
                return subtree.append_node(base_node=base_node, node=node)
        else:
            return False

    def search(self, base_node=None, node=BinaryNode()):
        if base_node is None:
            base_node = self.root

        if isinstance(node, BinaryNode):
            pass
        else:
            node = BinaryNode(data=node)

        if base_node == node:
            return {'node': base_node, 'parent': base_node.parent}
        elif base_node > node:
            return self.search(base_node=base_node.left_child, node=node)
        elif base_node < node:
            return self.search(base_node=base_node.right_child, node=node)

    def drop_node(self, base_node=None, node=BinaryNode()):
        if isinstance(node, BinaryNode):
            pass
        else:
            node = BinaryNode(data=node)

        search_res = self.search(base_node=base_node, node=node)
        n = search_res['node']
        p = search_res['parent']
        if n is None and p is None:
            return False
        else:
            if n.is_leaf:
                if n.is_left:
                    n.parent.left_child = None
                elif n.is_right:
                    n.parent.right_child = None
                return True
            else:
                if n.is_left:
                    pass
                elif n.is_right:
                    pass
                elif n.is_root:
                    pass


if __name__ == '__main__':
    node1 = BinaryNode(data=1)
    node2 = BinaryNode(data=2)
    node3 = BinaryNode(data=3)
    node4 = BinaryNode(data=4)
    node5 = BinaryNode(data=5)
    root = node4

    tree = BinarySearchTree(root)

    for item in [node3, node1, node2, node5]:
        tree.append_node(base_node=root, node=item)
        tree.layorder(base_node=root)
        print("========")
    tree.layorder(root)
    print("========")
    print(tree.search(node=node5))
