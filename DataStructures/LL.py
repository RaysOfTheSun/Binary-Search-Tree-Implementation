from Lists.LinkedList.LinkedList import LinkedList
import sys

LL = LinkedList()

items = range(0, 100001)

for item in items:
    LL.add(item)

LL.traverse()
print()
LL.remove(-1)
print(sys.getrecursionlimit())

LL.traverse()



