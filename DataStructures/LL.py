from Lists.LinkedList.LinkedList import LinkedList

LL = LinkedList()

for item in range(1, 101):
    LL.add(item)

print(LL.ListHead.data)
print(LL.ListHead.next.data)
print(LL.ListHead.next.next.data)
print(LL.ListHead.next.next.next.data)

print(LL.find(50))

LL.remove(50)

print(LL[0])

LL.traverse()

