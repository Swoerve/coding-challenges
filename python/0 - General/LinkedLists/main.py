class Node:
    """Base Node class for all nodes in a single linked list."""

    def __init__(self, data):
        self.data = data # Assign the data
        self.next = None # Initialize the next node (as null)

class LinkedList:
    """A Single Linked List class that implements all the basic methods and functionality for a single linked list."""

    def __init__(self):
        self.head = None

    def __str__(self) -> str:
        """Returns a string representation of the Single Linked List."""
        temp = self.head
        answer = ""
        while(temp):
            answer += str(temp.data)
            temp = temp.next
        return answer
    
    def push(self, new_data):
        """Pushes a new node at the beginning of the Single Linked List."""
        new_node = Node(new_data)

        new_node.next = self.head

        self.head = new_node
    
    def insertAfterNode(self, prev_node: Node, new_data):
        """Inserts a new node after the given Node."""
        if prev_node is None:
            print("No previous node found")
            return
        
        new_node = Node(new_data)

        new_node.next = prev_node.next

        prev_node.next = new_node
    
    def insertAfterIndex(self, index: int, new_data):
        """Inserts a new node after the given index."""
        curr = self.head
        count = 0
        while(curr):
            if count == index:
                break
            curr = curr.next
            count += 1

        if curr is None:
            print("No previous node found")
            return
        
        new_node = Node(new_data)

        new_node.next = curr.next

        curr.next = new_node
    
    def append(self, new_data):
        """Appends a new node to the end of the Single Linked List."""
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next =  new_node
    
    def exists(self, query):
        """Returns True if the given query is present in the Single Linked List."""
        cur = self.head

        while(cur.next):
            if cur.data == query:
                return True
            cur = cur.next
        return False
    
    def search(self, query):
        """Searches for a query in the Single Linked List and returns its index."""
        cur = self.head
        count = 0
        while(cur.next):
            if cur.data == query:
                return count
            cur = cur.next
            count += 1
        return None
    
    def length(self):
        """Returns the length of the Single Linked List."""
        cur = self.head
        count = 1
        while(cur.next):
            cur = cur.next
            count += 1
        return count

if __name__ == '__main__':
    llist = LinkedList()
  
    llist.head = Node(1)
    second = Node(2)
    third = Node(5)
    
    llist.head.next = second  # Link first node with second
    second.next = third  # Link second node with the third node
    
    print("#1")
    print(llist)

    llist.push(0)

    print("#2")
    print(llist)

    llist.insertAfterIndex(3, 7)

    print("#3")
    print(llist)

    llist.append(9)

    print("#4")
    print(llist)

    print(llist.exists(8))

    print(llist.search(7))
