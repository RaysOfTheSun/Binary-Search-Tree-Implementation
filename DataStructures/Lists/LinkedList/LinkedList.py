from Lists.LinkedList.Node import Node
import sys
import copy


class LinkedList:

    length = 0
    ListHead = None

    def __init__(self):
        self.ListHead = None

    def __getitem__(self, index):
        return self.__i_get_node(self.ListHead, index).data

    def __get_node(self, node, index):
        if node.index != index:
            return self.__get_node(node.next, index)
        else:
            return node

    @staticmethod
    def __i_get_node(node, index):
        while node.index != index:
            node = node.next

        return node

    def __add(self, data)->Node:
        node = Node(data)
        if node is not None:
            node.next = self.ListHead
            self.ListHead = node

        self.length += 1
        node.index = self.length - 1

        return node

    def add(self, data):
        self.ListHead = self.__add(data)

    def __find(self, node, key)->bool:
        if node is None:
            return False
        elif node.data != key:
            return self.__find(node.next, key)
        else:
            return True

    @staticmethod
    def __i_find(node, key)->bool:
        while node is not None:
            if node.data == key:
                return True
            else:
                node = node.next
        return False  # We have ran out of nodes to search

    def find(self, key)->bool:
        return self.__i_find(self.ListHead, key)

    def __remove(self, node, key=None)->Node:
        prev_limit = sys.getrecursionlimit()
        if key is None:
            node = node.next
        else:
            if node.data != key:
                node.next = self.__remove(node.next, key)
                sys.setrecursionlimit((sys.getrecursionlimit() + 1))  # No idea how I'll be able to patch the link
                # where data == key previously was using an iterative method. This will do for now.
            elif node.data == key:
                node = node.next  # POOF goes this node. It never existed.
                sys.setrecursionlimit(prev_limit)
        return node

    def remove(self, key=None):
        if key is not None:
            if self.find(key):
                self.ListHead = self.__remove(self.ListHead, key)
        else:
            self.ListHead = self.__remove(self.ListHead)

    def __traverse(self, node):
        if node is None:
            return
        else:
            print(node.data, end=', ')
            self.__traverse(node.next)

    @staticmethod
    def __i_traverse(node):
        while node is not None:
            print(node.data, end=', ')
            node = node.next

    def traverse(self):
        self.__i_traverse(self.ListHead)
