class LinkedList():

    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head


    def printList(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

    
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



class Node():

    def __init__(self, data):
        self.data = data
        self.next = None



lst = LinkedList()
lst.head = Node(1)
lst.printList()

lst.insert_at_tail(2)
lst.printList()