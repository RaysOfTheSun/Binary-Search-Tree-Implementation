from Lists.LinkedList.Node import Node


class LinkedList:

    length = 0
    ListHead = None

    def __init__(self):
        self.ListHead = None

    def __getitem__(self, index):
        return self.__get_node(self.ListHead, index).data

    def __get_node(self, node, index):
        if node.index != index:
            return self.__get_node(node.next, index)
        else:
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

    def find(self, key)->bool:
        return self.__find(self.ListHead, key)

    def __remove(self, node, key)->Node:
        if node.data != key:
            node.next = self.__remove(node.next, key)
        elif node.data == key:
            node = node.next  # POOF goes this node. It never existed.
        return node

    def remove(self, key):
        self.ListHead = self.__remove(self.ListHead, key)

    def __traverse(self, node):
        if node is None:
            return
        else:
            print(node.data, end=', ')
            self.__traverse(node.next)

    def traverse(self):
        self.__traverse(self.ListHead)
