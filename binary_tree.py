# coding: utf-8

from binary_node import BinaryNode

__author__ = 'Jux.Liu'


class BinaryTree(BinaryNode):
    def __init__(self, node=BinaryNode()):
        if isinstance(node, BinaryNode):
            self.root = node
        else:
            self.root = super().__init__(data=node)

    @property
    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def preorder(self, base_node=None):
        # root - left - right
        if base_node is None:
            return
        print(base_node.data)
        self.preorder(base_node=base_node.left_child)
        self.preorder(base_node=base_node.right_child)

    def inorder(self, base_node=None):
        # left - root - right
        if base_node is None:
            return
        self.inorder(base_node=base_node.left_child)
        print(base_node.data)
        self.inorder(base_node=base_node.right_child)

    def postorder(self, base_node=None):
        # left - right - root
        if base_node is None:
            return
        self.postorder(base_node=base_node.left_child)
        self.postorder(base_node=base_node.right_child)
        print(base_node.data)

    def layorder(self, base_node=None):
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

    def append_node(self, base_node, new_node):
        if self.is_empty:
            self.root = new_node
            return root
        else:
            node_queue = [base_node]
            while node_queue:
                node = node_queue.pop(0)
                if node.left_child is None:
                    node.left_child = new_node
                    return node
                elif node.right_child is None:
                    node.right_child = new_node
                    return node
                else:
                    node_queue.append(node.left_child)
                    node_queue.append(node.right_child)

    def append_tree(self, base_node, subtree):
        return self.append_node(base_node=base_node, new_node=subtree.root)

    def drop_node(self, base_node, node):
        if self.is_empty or base_node is None:
            pass
        else:
            if base_node.left_child == node:
                base_node.left_child = None
                return True
            elif base_node.right_child == node:
                base_node.right_child = None
                return True
            else:
                pass

        return False

    def drop_subtree(self, base_node, subtree):
        return self.drop_node(base_node=base_node, node=subtree.root)


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
    print('========')
    p_node = tree.append_node(base_node=node7, new_node=BinaryNode(99))
    tree.inorder(base_node=root)
    print('parent', p_node)
    print('========')
    p_node = tree.append_node(base_node=node7, new_node=BinaryNode(999))
    tree.inorder(base_node=root)
    print('parent', p_node)
    print('========')
    node10 = BinaryNode(data=10)
    node11 = BinaryNode(data=11)
    node12 = BinaryNode(data=12)
    node13 = BinaryNode(data=13)
    node14 = BinaryNode(data=14, left_child=node11)
    node15 = BinaryNode(data=15, left_child=node12, right_child=node13)
    node16 = BinaryNode(data=16, left_child=node10, right_child=node14)
    node17 = BinaryNode(data=17)
    node18 = BinaryNode(data=18, left_child=node17, right_child=node16)
    new_root = BinaryNode(data='new_root', left_child=node15, right_child=node18)
    new_tree = BinaryTree(new_root)
    p_node = tree.append_tree(base_node=node8, subtree=new_tree)
    tree.inorder(base_node=root)
    print('parent', p_node)
    print('========')
    r = tree.drop_node(base_node=node7, node=BinaryNode(999))
    tree.inorder(base_node=root)
    print('drop node result', r)
    print('========')
    r = tree.drop_subtree(base_node=node6, subtree=new_tree)
    tree.inorder(base_node=root)
    print('drop tree result1', r)
    print('========')
    r = tree.drop_subtree(base_node=BinaryNode(99), subtree=new_tree)
    tree.inorder(base_node=root)
    print('drop tree result2', r)
    print('========')
    r = tree.drop_subtree(base_node=p_node, subtree=new_tree)
    tree.inorder(base_node=root)
    print('drop tree result3', r)
    print('beacuse BinaryNode(99) == p_node, but BinaryNode(99) is not p_node')
    print('========')
    bt = BinaryTree()
    print(bt.root.data)
    print(bt.is_empty)
