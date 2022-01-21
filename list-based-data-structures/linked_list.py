class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
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
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        current_element = self.head
        current_position = 1
        while current_element:
            if current_position == position:
                return current_element
            current_position += 1
            current_element = current_element.next
        
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return
            
        previous_elem = self.get_position(position - 1)
        new_element.next = previous_elem.next
        previous_elem.next = new_element
    
    def delete(self, value):
        """Delete the first node with a given value."""
        current_elem = self.head
        previous_elem = None
        while current_elem:
            if current_elem.value == value:
                if current_elem == self.head:
                    self.head = current_elem.next
                else:
                    previous_elem.next = current_elem.next
                    current_elem = None
                break
            
            previous_elem = current_elem
            current_elem = current_elem.next

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
assert ll.head.next.next.value == 3
assert ll.get_position(3).value == 3

# Test insert
ll.insert(e4,3)
assert ll.get_position(3).value == 4

# Test delete
ll.delete(1)
assert ll.get_position(1).value == 2
assert ll.get_position(2).value == 4
assert ll.get_position(3).value == 3