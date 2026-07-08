# ____Search an Element____
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Node
n1=Node(10)
n2=Node(20)
n3=Node(30)

n1.next=n2
n2.next=n3

current = n1
target =20
while current:
    if (current.data==target):
        print("Found")
        break
    current=current.next
else:
    print("Not Found")
