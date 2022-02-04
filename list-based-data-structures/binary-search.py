def binary_search_idx(input_array, value):
    from_idx = 0
    upto_idx = len(input_array) - 1
    while from_idx <= upto_idx:
        half_idx = int((from_idx + upto_idx) / 2)
        middle_element = input_array[half_idx]
        if value == middle_element:
            return half_idx
        if value > middle_element:
            from_idx = half_idx + 1
        else:
            upto_idx = half_idx - 1
        
    return -1


test_list = [1,3,9,11,15,19,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43]
    
index_found = binary_search_idx(test_list, 11)
assert index_found == 3

index_found = binary_search_idx(test_list, 15)
assert index_found == 4

index_found = binary_search_idx(test_list, 1)
assert index_found == 0

index_found = binary_search_idx(test_list, 43)
assert index_found == 20

index_found = binary_search_idx(test_list, 25)
assert index_found == -1

index_found = binary_search_idx(test_list, 50)
assert index_found == -1

index_found = binary_search_idx(test_list, -99)
assert index_found == -1



def binary_search(input_array, value):
    """
    This implementation doesn't return the index and it's less efficient but it was my first approach.
    I really don't know if it's possible to return the index of the found element with this approach. 
    """
    current_array = input_array
    while current_array:
        middle_idx = int((len(current_array) - 1) / 2)
        middle_element = current_array[middle_idx]
        if value == middle_element:
            return True
        if value > middle_element:
            current_array = current_array[middle_idx+1:]
        else:
            current_array = current_array[:middle_idx]
    
    return False


index_found = binary_search(test_list, 11)
assert index_found

index_found = binary_search(test_list, 15)
assert index_found

index_found = binary_search(test_list, 1)
assert index_found

index_found = binary_search(test_list, 43)
assert index_found

index_found = binary_search(test_list, 25)
assert not index_found

index_found = binary_search(test_list, 50)
assert not index_found

index_found = binary_search(test_list, -99)
assert not index_found
