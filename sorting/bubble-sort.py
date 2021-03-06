from typing import List

# Efficienty of bubble sort is O(n^2)

def bubble_sort(bubbles: List[int]) -> List[int]:
    pending_elements_to_sort = True
    last_sorted_idx = len(bubbles)
    while pending_elements_to_sort:
        pending_elements_to_sort = False
        last_sorted_idx -= 1
        for current_idx in range(last_sorted_idx):
            next_idx = current_idx + 1
            
            if bubbles[current_idx] > bubbles[next_idx]:
                lower_number = bubbles[next_idx]
                higher_number = bubbles[current_idx]
                
                bubbles[next_idx] = higher_number
                bubbles[current_idx] = lower_number

                pending_elements_to_sort = True

    return bubbles


sorted_array = bubble_sort([19,5,2,0,40, 20, 15, 30, -80, 0, 1, 1, 3])
assert sorted_array == [-80, 0, 0, 1, 1, 2, 3, 5, 15, 19, 20, 30, 40]
print (sorted_array)


