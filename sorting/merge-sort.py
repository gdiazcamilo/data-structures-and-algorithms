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


l = [10, 2, 3, 4, 5, 6, -5]
l_sorted = mergeSort(l)
print(l_sorted)

assert l_sorted == [-5, 2, 3, 4, 5, 6, 10]