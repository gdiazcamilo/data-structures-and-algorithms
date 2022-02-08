# This is called a top-down implementation of merge sort. It's using recursion.
# The merge sort is O(N log(N)) time complexity.
# Merge sort is faster than bubble sort but use more memory.
# There are more efficient implementations. This is just for practice I did it without looking other code.

operations = 0

def mergeSort(array):
    global operations
    

    if len(array) == 1:
        operations += 1
        return array
    
    mid_idx = len(array) // 2
    first_half = mergeSort(array[:mid_idx])
    second_half = mergeSort(array[mid_idx:])
    operations += 3
    return sort(first_half, second_half)

def sort(array1, array2):
    global operations 

    if not array1:
        operations += 1
        return array2
    if not array2:
        operations += 1
        return array1
    
    array1_idx = 0
    array2_idx = 0
    array1_length = len(array1)
    array2_length = len(array2)
    sorted_array = []

    
    total_length = array1_length + array2_length
    operations += 7
    for _ in range(total_length):
        if array1_idx == array1_length:
            sorted_array.extend(array2[array2_idx:])
            operations += 2
            return sorted_array
        if array2_idx == array2_length:
            sorted_array.extend(array1[array1_idx:])
            operations += 2
            return sorted_array

        if array1[array1_idx] <= array2[array2_idx]:
            sorted_array.append(array1[array1_idx])
            array1_idx += 1
            operations += 6
        else:
            sorted_array.append(array2[array2_idx])
            array2_idx += 1
            operations += 4

    return sorted_array


# print(sort([10], [2, 3]))


l = [10, 2, 3, 4, 5, 6, -5, 2, 3, 4, 5, 6, -5, 2, 3, 4, 5, 6, -5]
l_sorted = mergeSort(l)
print(l_sorted)

# assert l_sorted == [-5, 2, 3, 4, 5, 6, 10]

print(operations)