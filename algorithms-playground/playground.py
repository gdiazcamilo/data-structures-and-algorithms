from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @property
    def next_node(self):
        return self.next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    current_node = head
    while current_node.next:
        if current_node.val == current_node.next.val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    
    return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(3)
head.next.next.next.next.next = ListNode(3)
head.next.next.next.next.next.next = ListNode(3)

node = deleteDuplicates(head);
while node:
    print(node.val)
    node = node.next
