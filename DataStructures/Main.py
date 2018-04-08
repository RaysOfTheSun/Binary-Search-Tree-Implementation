from Trees.BinaryTree.BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()

items = [10, 50, 40, 50, 60, 30, 45, 55, 70, 51, 56, 61, 80, 5, 4, 6]

for item in items:
    tree.insert_item(item)
