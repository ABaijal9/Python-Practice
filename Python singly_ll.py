class Node:
    def __init__ (self, data):
        self.data = data
        self.next_node = None

class singly_LL:
    def __init__(self): #constructor
        self.head = None

    def append(self, data): #add at the end
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        curr = self.head
        while curr.next_node is not None:
            curr = curr.next_node
        curr.next_node = new_node

    def prepend(self,data): #add at the begining
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def delete(self, key): #DELETION
        curr = self.head
        if curr is None:
            return
        elif curr and curr.data == key:
            self.head = curr.next_node
            curr = None
            return
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next_node
        if curr is None: 
            return
        prev.next_node = curr.next_node
        curr = None

    def printing(self): #print linkedlist
        curr = self.head
        while curr is not None:
            print(curr.data , end="->")
            curr = curr.next_node
        print("none")

sll = singly_LL()
sll.append(1)
sll.append(2)
sll.append(3)
sll.prepend(0)
sll.printing()  # Output: 0 -> 1 -> 2 -> 3 -> None
sll.delete(2)
sll.printing()  # Output: 0 -> 1 -> 3 -> None