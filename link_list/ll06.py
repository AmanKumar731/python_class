# ____Insert at Beginning____

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n1=Node(23)
n2=Node(24)
n3=Node(25)
n4=Node(26)
n5=Node(27)
n6=Node(28)
n7=Node(29)
newNode=Node(5)    #adding New Node

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
newNode.next=n1    #
n1=newNode
current=n1
while current:
    print(current.data,end="--->")
    current=current.next

print(None)