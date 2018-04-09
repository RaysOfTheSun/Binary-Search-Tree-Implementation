from Lists.LinkedList.Node import Node


class LinkedList:

    ListHead = None

    def __init__(self):
        self.ListHead = None

    def __add(self, data)->Node:
        node = Node(data)
        if node is not None:
            node.next = self.ListHead
            self.ListHead = node
        return node

    def add(self, data):
        self.ListHead = self.__add(data)

