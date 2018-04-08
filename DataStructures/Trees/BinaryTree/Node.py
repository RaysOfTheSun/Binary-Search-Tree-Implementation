# Date: April 5, 2018


class Node:

    left_child: None
    right_child: None
    data = None

    def __init__(self, data):
        """"Although pointers are declared as class attributes,
        if they are not initialized in the constructor they do
        not appear as attributes of the object. Therefore,
        initialization in the constructor is a must."""
        self.data = data
        self.left_child = None
        self.right_child = None
