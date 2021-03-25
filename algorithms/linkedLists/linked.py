class LinkedList():

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    
    def insert_at_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    
    #O(n) - Traversal
    def insert_at_tail(lst, data):

        new_node = Node(data)

        if lst.get_head() == None:
            lst.head = new_node
            return
        
        temp = lst.get_head()
        while temp.next:
            temp = temp.next

        temp.next = new_node
        return


    #O(n) - Return boolean
    def search(self, data):
        if self.get_head() is None:
            return False
        
        current = self.get_head()
        while current.next:
            if current.data == data:
                return True
            current = current.next
        
        return False

    #O(n) - Return message
    def delete(self, data):
        deleted = False

        if self.is_empty():
            return deleted

        current = self.get_head()
        previous_node = None
        
        while current is not None:

            if data is current.data:
                previous_node.next = current.next
                current.next = None
                deleted = True
                break

            previous_node = current
            current = current.next

        if deleted:
            print(f"The data {data} is deleted!")
        else:
            print(f"The data {data} is not in list!")
            
        return deleted

    
    #O(n)
    def length(self):
        current = self.get_head()
        lenght = 0

        while current:
            lenght += 1
            current = current.next

        return lenght


    def reverse(self):
        previous = None
        next_node = None
        current = self.get_head()

        while current:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

            self.head = previous
        return self.head

    def remove_duplicates(self):
        #Sorted order
        current = self.get_head() 
	
        while current is not None:
            next_node = current.next
            while next_node is not None and next_node.data == current.data:
                next_node = next_node.next
		
            current.next = next_node
            current = next_node
        return self.head
		

class Node():

    def __init__(self, data):
        self.data = data
        self.next = None



lst = LinkedList()
lst.head = Node(1)

lst.insert_at_tail(2)
lst.insert_at_tail(3)
lst.insert_at_head(0)
lst.insert_at_head(-1)
lst.insert_at_tail(4)
lst.insert_at_tail(5)
lst.insert_at_tail(5)
lst.printList()

print(lst.search(2))
print(lst.search(5))

print(lst.delete(3))
lst.printList()

print(f"Total nodes: {lst.length()}")

print('Linked list reverse')
lst.reverse()
lst.printList()

print('Remove duplicates')
lst.remove_duplicates()
lst.printList()