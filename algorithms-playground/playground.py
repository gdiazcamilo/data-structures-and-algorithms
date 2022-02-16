# based on the explanation from visualgo.net
# worst case -> O(N^2)
# averae case -> O(NLog(N))
# It's in-place algorithm. In practice and with some optimizations is faster than merge sort and use less memory than merge sort.
def quick_sort(array, from_idx, to_idx):
    if to_idx <= from_idx + 1:
        return array
        
    # We're going to choose an element (`pivot`) and and move it to the final sorted position that it should be.
    pivot_idx = from_idx
    pivot = array[pivot_idx]

    # `store_idx` tell us in which position we're going to put the elements that are <= than `pivot`
    store_idx = pivot_idx + 1

    # Move all the elements <= pivot next to pivot
    for idx in range(from_idx + 1, to_idx):
        if array[idx] <= pivot:
            swap(array, store_idx, idx)
            store_idx += 1
    
    # Now we know that pivot should be after the last element that we moved, 
    # but Quick Sort is an in-place algorithm so we just swap `pivot` with the last_element.
    # Then `pivot` will be at its final position.
    swap(array, store_idx - 1, pivot_idx)
    
    # Now that `pivot` it's at its final position, we do the same but with the elements to the left and then with the elements to the right.
    #sorted_first_half = 
    quick_sort(array, pivot_idx, store_idx - 1)
    # now that first half is sorted, sort the second half to finish
    #sorted_array = 
    quick_sort(array, store_idx, to_idx)
    
    return array


def swap(array, idx1, idx2):
    array[idx1], array[idx2] = array[idx2], array[idx1]


#array = [100,99,98,97,96,95,94,93,92,91,90,89,88,87,86,85,84,83,82,81,80]
array = [1,5,15,0,60,2,3,5,11]
print(quick_sort(array, 0, len(array)))