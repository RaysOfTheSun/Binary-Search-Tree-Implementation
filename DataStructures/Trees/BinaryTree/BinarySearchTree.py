# Date: April 5, 2018

"""This is a simple implementation of a binary search tree
using python"""

from Trees.BinaryTree.Node import Node


class BinarySearchTree:

    __RootNode = None

    def __init__(self):
        self.__RootNode = None

    # Inserts an item into the binary search tree
    def __add(self, node, data)->Node:
        if node is None:  # Null is equivalent to None in python
            node = Node(data)
        elif data <= node.data:
            node.left_child = self.__add(node.left_child, data)
        else:
            node.right_child = self.__add(node.right_child, data)
        return node

    # Serves as an interface to the '__add' method.
    # This avoids repeatedly referencing the root node
    # outside of this class
    def add(self, data):
        self.__RootNode = self.__add(self.__RootNode, data)

    # Searches for an item in the tree
    def __find(self, node, key)->bool:
        if node is None:  # Since we ran out of nodes to search,
            return False  # the item is not in the tree
        elif key < node.data:
            return self.__find(node.left_child, key)
        elif key > node.data:
            return self.__find(node.right_child, key)
        else:
            return True

    # Serves as an interface to the '__find' method.
    # This avoids repeatedly referencing the root node
    # outside of this class
    def find(self, key)->bool:
        return self.__find(self.__RootNode, key)

    # Returns the node's existing child
    @staticmethod
    def __get_child(node)->Node:
        if node.right_child is not None:
            return node.right_child
        else:
            return node.left_child

    # Finds the minimum value in the given subtree
    def __find_min(self, node)->int:
        # Go as deep as possible in the node's left
        # subtree as it will contain values that are
        # much smaller than the parent node
        if node.left_child is not None:
            return self.__find_min(node.left_child)
        else:
            return node.data

    # Removes an item from the tree
    def __remove(self, node, key)->Node:
        if key < node.data:
            node.left_child = self.__remove(node.left_child, key)
        elif key > node.data:
            node.right_child = self.__remove(node.right_child, key)
        else:  # we found the item in the tree. Let's get rid of it
            # The item to be deleted is a leaf node
            if (node.right_child is None) and (node.left_child is None):
                node = None
            # The item to be deleted is a node that has one child
            elif (((node.right_child is not None) and (node.left_child is None))
                    or ((node.left_child is not None) and (node.right_child is None))):
                node = self.__get_child(node)
            # The item to be deleted is a node that has two children
            elif (node.right_child is not None) and (node.left_child is not None):
                node.data = self.__find_min(node.right_child)
                node.right_child = self.__remove(node.right_child, node.data)
        return node

    # Serves as an interface to the '__remove' method.
    # This avoids repeatedly referencing the root node
    # outside of this class
    def remove(self, key):
        # As the item is not in the tree, there is nothing to delete
        if(self.find(key)) is False:
            return
        else:
            self.__RootNode = self.__remove(self.__RootNode, key)
            if (self.find(key)) is True:
                # Check for duplicates and get rid of them too
                self.remove(key)
            else:
                return

    def __traverse_inorder(self, node):
        if node is not None:
            self.__traverse_inorder(node.left_child)
            print(node.data, end=', ')
            self.__traverse_inorder(node.right_child)

    # Serves as an interface to the '__traverse_inorder' method.
    # This eliminates the need to reference the root node
    # outside of this class
    def traverse_inorder(self):
        self.__traverse_inorder(self.__RootNode)

    # Serves as an interface to the '__traverse_postorder' method.
    # This eliminates the need to reference the root node
    # outside of this class
    def __traverse_postorder(self, node):
        if node is not None:
            self.__traverse_postorder(node.left_child)
            self.__traverse_postorder(node.right_child)
            print(node.data, end=', ')

    def traverse_postorder(self):
        self.__traverse_postorder(self.__RootNode)

    def __traverse_preorder(self, node):
        if node is not None:
            print(node.data, end=', ')
            self.__traverse_preorder(node.left_child)
            self.__traverse_preorder(node.right_child)

    # Serves as an interface to the '__traverse_preorder' method.
    # This eliminates the need to reference the root node
    # outside of this class
    def traverse_preorder(self):
        self.__traverse_preorder(self.__RootNode)

    def show_traversals(self):
        print("Preorder Traversal: ", end=' ')
        self.traverse_preorder()
        print()
        print("Postorder Traversal: ", end=' ')
        self.traverse_postorder()
        print()
        print("Inorder Traversal: ", end=' ')
        self.traverse_inorder()
        print()
