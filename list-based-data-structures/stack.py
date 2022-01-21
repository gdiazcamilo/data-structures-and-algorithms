class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    """
    Using `insert_first` instead of `append` makes the operation faster, O(1) because we don't have to iterate all the elements in the list to get the last one inserted.
    """
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        new_element.next = self.head
        self.head = new_element
        

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        previous_head = self.head
        if previous_head is None:
            return None
        self.head = self.head.next
        return previous_head

class Stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        return self.ll.delete_first()
        
    
# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a Stack
stack = Stack(e1)

# Test stack functionality
stack.push(e2)
stack.push(e3)
assert stack.pop().value == 3
assert stack.pop().value == 2
assert stack.pop().value == 1
assert stack.pop() is None
stack.push(e4)
assert stack.pop().value == 4