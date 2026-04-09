class Node:
    def __init__(self, data):
        self.data = data   
        self.next = None    

class my_list:
    def __init__(self):
        self.head = None

#checks if string is empty
    def is_empty(self):
        return self.head is None
    
#displays all elements in the list
    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ". join(elements) + " -> None")

#counts the number of nodes
    def size(self):
        count = 0
        current = self.head
        while current:
            count +=1
            current = current.next
        return count

# inserts a new node at the beginning of the list
#time complex O(1)
    def prepend(self,data):    
        new_node =Node(data)
        new_node.next= self.head
        self.head = new_node

#insert anew node at the end of the list
#time complex O(n)
    def append(self,data):
        new_node = Node(data)
# If list is empty, new node becomes head        
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

#insert at specific position 
#Time Complexity: O(n)
    def insert_at_position(self, data, position):
        if position == 0:
            self.prepend(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):  
            if not current:
                print("Position out of bounds")
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

#deletion by value
    def delete_by_value(self,value):
        if self.head and self.head.data == value: 
            self.head = self.head.next
            return
    
        prev = self.head
        while prev and prev.next:
            if prev.next.data == value:
                prev.next = prev.next.next
                return
            prev = prev.next
    
        print("Value not found")

#search element
    def search(self, value):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.data == value:
                return index
            current_node = current_node.next
            index += 1
        return -1
    
#TEST CASE
if __name__ == "__main__":
    my_list = my_list()

    my_list.append(1)
    my_list.append(2)
    my_list.append(3)
    my_list.append(4)

    print("Original linkedlist: ")
    my_list.display()

    my_list.insert_at_position(30,4)
    print("insert 30 at position 4: ")
    my_list.display()

    my_list.delete_by_value(1)
    print("deletion of value 1: ")
    my_list.display()

    
    print("search for 3 in LinkedList: ",my_list.search(3) )

    print("linkedlist size: ",my_list.size())


