class Node:
    def __init__(self, data):
        self.data = data #this is to initialize the data of the node
        self.next = None #this is to initialize the next pointer of the node to None
class CircularLinkedList:
    def __init__(self):
        self.head = None #this is to initialize the head pointer to None

    def append(self, data):
        new_node = Node(data) #this is to create a new node with the given data

        if self.head is None:
            self.head = new_node #this is to set the head pointer to the new node if the list is empty
            new_node.next = self.head #this is to set the next pointer of the new node to point to itself, making it circular
            return
        
        last_node = self.head #this is to set the last_node pointer to the head of the list
        while last_node.next != self.head: #this is to traverse the list until the last node is reached
            last_node = last_node.next
        last_node.next = new_node #this is to set the next pointer of the last node
        new_node.next = self.head #this is to set the next pointer of the new node to point to the head, maintaining circularity

    def traverse(self): 
        if self.head is None:
            print("List is empty") #this is to print a message if the list is empty
            return
        
        current = self.head #this is to set the current pointer to the head of the list
        print("Circular Linked List:")
        print("start -> ", end="")
       
        while True:
            print(current.data, end=" -> ") #this is to print the data of the current node
            current = current.next #this is to set the current pointer to the next node in the list
            if current == self.head: #this is to check if we have traversed back to the head
                break
        print("back to head")


cll = CircularLinkedList()
cll.append(10)
cll.append(20)
cll.append(30)
cll.append(40)


cll.traverse()