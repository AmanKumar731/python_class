class Node:
    def __init__(self, data):
        self.data = data
        self.next = None #this is to initialize the next pointer to None

first = Node(1) #this is to create a new node with data 1
second = Node(2) #this is to create a new node with data 2
first.next = second #this is to link the first node to the second node

print(first.data) #this is to print the data of the first node
print(first.next.data) #this is to print the data of the second node

class LinkedList:
    def __init__(self):
        # this is to initialize the head pointer to None
        self.head = None
    def append(self,data):
        new_node = Node(data) #this is to create a new node with the given data


        # if the linked list is empty, set the head to the new node
        if self.head is None:
            self.head = new_node
            return
        # otherwise, traverse to the end of the list and append the new node
        last_node = self.head #this is to set the last_node pointer to the head of the list

        while last_node.next: #this is to traverse the list until the last node is reached
            last_node = last_node.next #this is to set the last_node pointer to the next node in the list
        last_node.next = new_node #this is to set the next pointer of the last node to the new node


    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head 
        self.head = new_node
        #this is to set the next pointer of the new node to the head of the list
    
    def remove(self,data):
        current = self.head #this is to set the current pointer to the head of the list
        if current is None:
            print("List is empty") #this is to print a message if the list is empty
            return
        
        # if head is the one to be deleted
        if current.data == data:
            print("the head is the one to be deleted")
            self.head = current.next
            return 
        # if head is not the one to be deleted, traverse the list to find the node to be deleted
        prev = None #this is to initialize the prev pointer to None
        while current and current.data != data:
            prev = current
            current = current.next #this is to traverse the list until the node is found
        if current is None:
            print("Node not found") #this is to print a message if the node is not found
            return
        prev.next = current.next #this is to set the next pointer of the previous node to the next node of the current node, effectively removing the current node from the list
        print("Node deleted") #this is to print a message if the node is deleted
        return
    
    def traverse(self):
        current = self.head #this is to set the current pointer to the head of the list
        while current:
            print(current.data, end=" -> ") #this is to print the data of the current node
            current = current.next #this is to set the current pointer to the next node in the list
        print("None") #this is to print None at the end of the list

    

print("Linked List:")
my_list = LinkedList() #this is to create a new linked list
my_list.append(1) #this is to append a new node with data 1 to the linked list
my_list.append(2) #this is to append a new node with data 2 to the linked list
my_list.append(3) #this is to append a new node with data 3 to the linked list
my_list.prepend(0) #this is to prepend a new node with data 0 to the linked list
my_list.remove(2) #this is to remove the node with data 2 from the linked list
my_list.traverse() #this is to traverse