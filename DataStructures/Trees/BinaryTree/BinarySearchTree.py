# Date: April 5, 2018

"""This is a simple implementation of a binary search tree
using python"""

from Trees.BinaryTree.Node import Node


class BinarySearchTree:

    __RootNode = None

    """Methods that makes use of the [operation_item] naming template is a method 
    that acts as an interface to the actual method [operation]. This is because 
    we do not want to reference the tree's root node in the client code.
    Another thing is, I can't use default arguments as there are situations in where
    a node has to be checked if it is null (if node is None)"""

    def __init__(self):
        self.__RootNode = None

    # Inserts an item into the binary search tree
    # Returns an item of type Node
    def __insert(self, node, data)->Node:
        if node is None:  # Null is equivalent to None in python
            node = Node(data)
        elif data <= node.data:
            node.left_child = self.__insert(node.left_child, data)
        else:
            node.right_child = self.__insert(node.right_child, data)
        return node

    # This method serves as an interface to the 'insert' method.
    # I think it is quite annoying to repeatedly reference the root node
    # for every insertion operation
    def insert_item(self, data):
        self.__RootNode = self.__insert(self.__RootNode, data)

    def __search(self, node, key)->bool:
        if node is None:  # Since we ran out of nodes to search,
            return False  # the item is not in the tree
        elif key < node.data:
            return self.__search(node.left_child, key)
        elif key > node.data:
            return self.__search(node.right_child, key)
        else:
            return True

    def search_item(self, key)->bool:
        return self.__search(self.__RootNode, key)

    @staticmethod
    def __get_child(node)->Node:
        if node.right_child is not None:
            return node.right_child
        else:
            return node.left_child

    def __find_min(self, node)->int:
        # Go as deep as possible in the node's left
        # subtree as it will contain values that are
        # much smaller than the parent node
        if node.left_child is not None:
            return self.__find_min(node.left_child)
        else:
            return node.data

    # Removes an item from the tree
    def __delete(self, node, key)->Node:
        if key < node.data:
            node.left_child = self.__delete(node.left_child, key)
        elif key > node.data:
            node.right_child = self.__delete(node.right_child, key)
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
                node.right_child = self.__delete(node.right_child, node.data)
        return node

    def delete_item(self, key):
        self.__RootNode = self.__delete(self.__RootNode, key)
