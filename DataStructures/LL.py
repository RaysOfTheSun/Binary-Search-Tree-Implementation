from Lists.LinkedList.LinkedList import LinkedList

LL = LinkedList()

for item in range(0, 1001):
    LL.add(item)

LL.traverse()
print()
print(LL.find(1000))
LL.remove(1000)
LL.traverse()
print()
print(LL.find(987))



