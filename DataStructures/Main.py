from Trees.BinaryTree.BinarySearchTree import BinarySearchTree

tree = BinarySearchTree()

items = ['q', 'w', 'e', 't', 'y', 'u', 'i', 'o', 'p', 'w', 'w', 'w']
# 10, 50, 40, 50, 60, 30, 45, 55, 70, 51, 56, 61, 80, 5, 4, 6
for item in items:
    tree.add(item)

tree.show_traversals()
tree.remove('w')
print()
tree.show_traversals()


value = (input("Enter a value to find in the tree: "))

if tree.find(value) is True:
    print("The value {} is in the tree.".format(value))
else:
    print("The value {} is not in the tree.".format(value))
