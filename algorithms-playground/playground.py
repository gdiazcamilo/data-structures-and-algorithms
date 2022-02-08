def mergeSort(array):
    if len(array) == 1:
        return array
    
    mid_idx = len(array) // 2
    first_half = mergeSort(array[:mid_idx])
    second_half = mergeSort(array[mid_idx:])
    return sort(first_half, second_half)

def sort(array1, array2):
    if not array1:
        return array2
    if not array2:
        return array1
    
    array1_idx = 0
    array2_idx = 0
    array1_length = len(array1)
    array2_length = len(array2)
    sorted_array = []

    
    total_length = array1_length + array2_length
    for _ in range(total_length):
        if array1_idx == array1_length:
            sorted_array.extend(array2[array2_idx:])
            return sorted_array
        if array2_idx == array2_length:
            sorted_array.extend(array1[array1_idx:])
            return sorted_array

        if array1[array1_idx] <= array2[array2_idx]:
            sorted_array.append(array1[array1_idx])
            array1_idx += 1
        else:
            sorted_array.append(array2[array2_idx])
            array2_idx += 1

    return sorted_array

    


# print(sort([10], [2, 3]))


l = [10,2,3,4,5,6,-5]
l_sorted = mergeSort(l)
print(l_sorted)



# from typing import Optional

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# safety = 0
# def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
#     global safety
#     safety += 1
#     if safety > 1000:
#         print('infinity recursion')
#         return

#     iterator = head
#     previous = None
#     while iterator:
#         temp = iterator.next
#         iterator.next = previous

#         previous = iterator
#         iterator = temp

#     return previous
                    

# head2 = ListNode(1)
# head2.next = ListNode(2)
# head2.next.next = ListNode(3)
# head2.next.next.next = ListNode(4)
# head2.next.next.next.next = ListNode(5)


# node = reverseList(head2)
# while node:
#     print(node.val)
#     node = node.next



