from typing import List

# Efficienty of bubble sort is O(n^2)

operations = 0

def bubble_sort(bubbles: List[int]) -> List[int]:
    global operations 

    pending_elements_to_sort = True
    last_sorted_idx = len(bubbles)
    operations = 2

    while pending_elements_to_sort:
        pending_elements_to_sort = False
        last_sorted_idx -= 1
        operations += 3
        for current_idx in range(last_sorted_idx):
            next_idx = current_idx + 1
            operations += 1
            if bubbles[current_idx] > bubbles[next_idx]:
                
                lower_number = bubbles[next_idx]
                higher_number = bubbles[current_idx]
                
                bubbles[next_idx] = higher_number
                bubbles[current_idx] = lower_number

                pending_elements_to_sort = True
                operations += 10

    return bubbles


sorted_array = bubble_sort([10, 2, 3, 4, 5, 6, -5, 2, 3, 4, 5, 6, -5, 2, 3, 4, 5, 6, -5])
# assert sorted_array == [-5, 2, 3, 4, 5, 6, 10]
print (sorted_array)

print(operations)