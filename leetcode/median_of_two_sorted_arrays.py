"""
https://leetcode.com/problems/median-of-two-sorted-arrays/
Difficulty: hard

Things we know:
- There are 2 sorted arrays. Let's call them A and B
- At least one of them will have at least one element. Never both will be empty
- Solution should be Log(len(A)+len(B))

Main ideas to solve the algorithm:
 - Binary Search (required to implement the solution I'll explain)

The median is the middle value of a group of values which are organized whether ascending or descending order.
When the number of elements is odd the median is just one value (the one in the middle).
When the number of elements is even the median is the average of the two elements in the middle.

Following examples are not related. Meaning that the even case is not for array A and odd case is not for array B.
    Even case:                         Odd case:
         middle                                middle
           v                                      v
L = [ 1, 2, 3, 4 ]                    L = [ 1, 2, 3, 4, 5 ]
         v  v                                     v
          \/                                 median = 3
   median = ( 2 + 3) / 2
   median = 2.5


Can we just merge and sort the arrays?
The simplest solution will be to merge the two arrays, sort them and then calculate the median based on the above rules,
but the most efficient of the sort algorithms will give us time complexity of O(N), which is greater than O(Log(M+N)) 
that we are asked. So we can't merge and sort.

What else can be do?
We know that the median is at the middle... which means that there's going to be elements at the left and at the right 
of the median. So, there's going to be one partition to the left and one to the right of the median. 
If we can, somehow, find the elements at the right and at the left, we're going to be closer to the solution.

How can we find those elements when the numbers are in different arrays?
We know that the left and right partitions have the same size when the total elements is even; 
and one is larger than the other when the total elements is odd (by one element).

                    Even case:                                                      Odd case:
                  L = [ 1, 2, 3, 4 ]                                           L = [ 1, 2, 3, 4, 5 ]
left partition -> [ 1, 2 ]  [3, 4] <- right partition       left partition -> [ 1, 2 ]  [ 3, 4, 5 ] <- right partition (first possibility if round down the half)
                                                            left partition -> [ 1, 2, 3 ]  [ 4, 5 ] <- right partition (second possibility if round up the half)

If we know that, then we can say that the median it's:          If we know that, we can say the median it's 
 [max(left partition) + min(right partition)] / 2               the first element of the right partition (if we rounded down) or
This is the same than:                                          the last element from the left partition (if rounded up)
 [left_partition[-1] + right_partition[0]] / 2
It's better to use the index because max and min 
functions are O(N) time complexity.


We need to identity which numbers from the array A and array B belongs to the left partition.
If the total number of elements are 10 (even), then the partitions would be 5 and 5.
If the total number of elements are 9 (odd), then the partitions would be 4 and 5.

We don't know which are the elements, only how many elements must be in each partition.
We do know that all the elements in the left must be less or equal than all the elements to the right or if the partitions 
are sorted ascending we can reformulate this as: the last element from the left partition must be <= than first element of the right partition.
Since that is true, we can state the elements in the left partition must be conformed by the elements at the beginning of one or both of the arrays
because the arrays are sorted ascending and the firsts elements are the smaller than the last elements.
For example: For a total of 10 elements in both A and B, the left partition must have 5 numbers, 
3 of which could be the first 3 elements of A and the remaining 2, the first 2 element of B.

What do we do to find these partitions and the elements within them?
We don't know what else to do, so we start GUESSING.
Start guessing with the "most probable" or "obvious" case. This is that one part of the elements in the left partition
are conformed by the half of elements from one array, let's say A. And the remaining, from the other array (B).


Examples:
    Example 1                                                                   Example 2
        elements in A = 5                                                           elements in A = 4                                             
        elements in B = 5                                                           elements in B = 7                                             
        total elements = 10                                                         total elements = 11                                           
                                                                                                                                                
        left partition = total elements / 2                                         left partition = total elements / 2                           
        left partition = 10 / 2                                                     left partition = 11 / 2
        left partition = 5                                                          left partition = 5 (rounded down)                                           
                                                                                                                                        
        half of A = length(A) / 2                                                   half of A = length(A) / 2                   
        half of A = 5 / 2                                                           half of A = 4 / 2                                
        half of A = 2 (rounded down)                                                half of A = 2
                                                                                                                                        
        numbers coming from A = half of A                                           numbers coming from A = half of A                
        numbers coming from A = 2 (the first 2)                                     numbers coming from A = 2 (the first 2)                       
                                                                                                                                        
        numbers coming from B = left partition - numbers coming from A              numbers coming from B = left partition - numbers coming from A
        numbers coming from B = 5 - 2                                               numbers coming from B = 5 - 2                                 
        numbers coming from B = 3 (the first 3)                                     numbers coming from B = 3 (the first 3)      


    Example 3                                                                   Example 4
        elements in A = 1                                                           elements in A = 10                                             
        elements in B = 9                                                           elements in B = 1                                             
        total elements = 10                                                         total elements = 11                                           
                                                                                                                                                
        left partition = total elements / 2                                         left partition = total elements / 2                           
        left partition = 10 / 2                                                     left partition = 11 / 2
        left partition = 5                                                          left partition = 5 (rounded down)                                           
                                                                                                                                        
        half of left partition = left partition / 2                                 half of left partition = left partition / 2                   
        half of left partition = 5 / 2                                              half of left partition = 5 / 2                                
        half of left partition = 2 (rounded down)                                   half of left partition = 2 (rounded down)                     
                                                                                                                                        
        numbers coming from A = half of left partition                              numbers coming from A = half of left partition                
        numbers coming from A = 2 (the first 2) <-- INDEX OF OF BOUNDS ERROR        numbers coming from A = 2 (the first 2)                       
                                                                                                                                        
        numbers coming from B = left partition - numbers coming from A              numbers coming from B = left partition - numbers coming from A
        numbers coming from B = 5 - 2                                               numbers coming from B = 5 - 2                                 
        numbers coming from B = 3 (the first 3)                                     numbers coming from B = 3 (the first 3) <-- INDEX OF OF BOUNDS ERROR

As we can see in the examples there are some edge cases with example 3 and 4, 
but we will handle them later when we have a working solution to not overcomplicate things right now.

Since we are just guessing and our guess could be wrong and if it's wrong we would need to make other guess. 
(That sounds like we are going to need a loop). So, let's say we take the half of A as a first guess and it turns out
the guess is wrong, that means that we need to take another guess. So, it's useful to keep in memory the range of 
elements we are taking from A so we can change them if the guess is wrong.

How do we verify that our guess (the partitions) are correct?
The elements in left partition must be less or equal than the elements in the right partition.
The right partition is automatically conformed by the elements in both array that do not belong to the left partition.
We have one part of the left partition in array A (numbers coming from A) 
and the other part in the array B (numbers coming from B). 
The same thing applies for the right partition: the remaining elements from A that are not in `numbers coming from A` and
the remaining elements from B that are not in `numbers coming from B` conforms the right partition.
So we have four arrays: 2 for the left partition and 2 for the right partition.

A = [ 1, 2, 3, 4, 5 ]
B = [ 3, 5, 7, 8, 9 ]

Left partition (5 elements):                        Right partition (5 elements):
A[0:numbers coming from A + 1]                          A[numbers coming from A + 1:]
A[0:3] = [ 1, 2 ]                                       A[3:] = [3, 4, 5]

B[0:numbers coming from B + 1] = [ 3, 5, 7 ]            B[numbers coming from B + 1:] = [8, 9]
B[0:4] = [ 3, 5, 7 ]                                    B[4:] = [8, 9]

We need to check if the numbers in the two arrays in left partition are <= than the elements in the right partition.
We already know that all the numbers in A[0:3] <= A[3:] because A is sorted; same thing for B. So, half of the job is done.
Now, we need to check if numbers in A[0:3] <= B[4:].
We could iterate over each element to compare it, but that again will by O(N/2) because we are operating with half of elements
and if the guess is incorrect we'll need to do it again and again until we find the right guess, so that's not efficient.

Given that our arrays are sorted, we can simplify that and say that 
the last element in A[0:3] must be <= than the first element in B[4:]. We can simplify even further: we don't really 
need the whole array, just the last element from A[0:3] which is A[numbers coming from A - 1] --> A[1] --> 2;
and the first element from B[4:0] which is B[numbers coming from B] --> B[3] --> 8.
2 <= 8 is True, so we're good. 

We see that `numbers coming from A` and `numbers coming from B` are behaving like an index, so we will call them
A_idx and B_idx respectively and decrease them by 1 to access the last element of the left partition,
instead of the range of elements.
A_idx = numbers coming from A - 1
B_idx = numbers coming from B - 1

Now we need to check the other part.
B[B_idx] <= A[A_idx + 1]
B[2] <= A[2]
7 <= 3 is False, so our partitions are incorrect, the guess is incorrect, we need make another guess.

We know that A_idx and B_idx are the last elements in the left partition, so 
when we say `A_idx + 1` or `B_idx` + 1 we are referring to the min or first element in the right partition.


What elements to we pick for the subsequent guesses?
In the scenario above B[B_idx] is not less or equal than A[A_idx + 1] and the arrays are sorted,
that means that we need to pick an element that is less than B[B_idx], 
which means that we need to pick an element to the left of B[B_idx] because the arrays are sorted in ascending order.
In other words, this is the same that saying that we need to pick an element higher than A[A_idx + 1],
which means that we need to pick an element to the right of A[A_idx + 1] because the arrays are sorted in ascending order.
In fact, it's better to pick the element at the right of A[A_idx + 1] because previously we determined 
the value of B_idx based on the value of A_idx (numbers coming from B = left partition - numbers coming from A),
and keep doing it that way it's more consistent.

In the case I just explained in the paragraph above B[B_idx] is not <= than A[A_idx + 1], 
so we need to increase A_idx to pick an element at the right of it.
But, when the case is that A[A_idx] is not <= than B[B_idx + 1], then we decrease A_idx to pick lower elements (at the left of A_idx).

All right, we know now that we need to choose a element to the right of A[A_idx + 1], recalculate B_idx based on that and try another guess.
We could just increment A_idx by 1 when our guesses are incorrect, but again that will lead us to a O(N/2) or maybe O(N/4) time complexity 
in the worst case because we are checking half of the elements one by one.
So, here we will do a Binary Search, to increase the probability of finding the correct partition in less guesses or attempts.

Remember that A_idx = numbers coming from A.
To use Binary Search we need to change how we are choosing A_idx, what we did previously was to use the half of A: length(A) / 2.
We're going to change that a little and calculate it differently.
We want to start at the middle (half of A), and if the guess is wrong we will increase or decrease the numbers of elements coming from A.
If decreasing then we know for sure that the numbers to the right are not part of the left partition and viceversa.
Then, in the next guess, we are working with half of the elements from A and we want to do the same and 
pick the elements from the middle of the half, and so on.

One efficient way to do that is use two indexes for A. That will indicate the range in which we pick the middle element.
We call these two indexes `from_idx` and `to_idx`.
In the first guess the indexes are set like this:
`from_idx` = 0
`to_idx` = length(A) - 1

To find the middle:
(from_idx + to_idx) / 2 -->  (0+4)/2  --> 2

Now let's say we need to decrease the number of element from A because A[A_idx] was not <= than B[B_idx + 1],
this means the elements at the right of A[A_idx] do not form part of the left partition,
so we set the `to_idx` = A_idx - 1, and repeat the process:
`from_idx` = 0
`to_idx` = A_idx - 1 = 1

To find the middle:
(from_idx + to_idx) / 2 -->  (0+1)/2 --> 0

If we need to increase the number of element from A, then we set:
`from_idx` = A_idx + 1

Ok, now we know how to make the guesses and how to check if the guesses are right.

What after whe found the right partitions?
Now, we have 2 cases: odd and even.
When the total elements in both arrays are even, it means our partitions have the same amount of elements.
When the total elements in both arrays are odd, it means we have one partitions larger than the other by one element.
Remember the arrays are sorted in ascending or non-decreasing order.

Even:
We take the maximun (the last one) element from left, add the minium (first element) of right and divide by 2. 
The thing is that the left partition is conformed by two arrays, to find the maximun we do:
left_max = max(A[A_idx], B[B_idx])
right_min = min(A[A_idx+1], B[B_idx + 1])
median = (left_max + right_min) / 2

Odd:
Median will be the min element from the largest partition.
The largest will be the left partition if when doing the binary search we divide by two the length(A) - 1; 
if we do length(A) / 2, the right partition will be the largest.

Edge cases
We have 1 index signanilling the end of the elements in A that forms the left part; 
1 index signanilling the end of the elements in B that forms the left part;
If any of those indexes is less than 0 (out of bound) then we'll use the default value of -infinity.
That means that all the elements in A or B are going to be part of the right partition and none in the left.

For the right partition we have 1 signanilling the end of the elements in A that forms the right part; 
1 index signanilling the end of the elements in B that forms the right part;
If any of those indexes is less greater than the length of the respective array (out of bound) then we'll use the default value of +infinity.
That means that all the elements in A or B are going to be part of the left partition and none in the right.

"""




def median_of_two_arrays(A, B):
    if len(A) > len(B):
        A, B = B, A

    max_idx = len(A) + len(B) - 1
    left_partition_max_idx = max_idx // 2

    from_idx = 0
    to_idx = len(A) - 1

    while True:
        A_idx = (from_idx + to_idx) // 2
        B_idx = left_partition_max_idx - A_idx - 1

        A_max_left = A[A_idx] if A_idx >= 0 else float('-infinity')
        B_max_left = B[B_idx] if B_idx >= 0 else float('-infinity')
        A_min_right = A[A_idx + 1] if A_idx + 1 < len(A) else float('infinity')
        B_min_right = B[B_idx + 1] if B_idx + 1 < len(B) else float('infinity')

        partition_is_correct = A_max_left <= B_min_right and B_max_left <= A_min_right
        if partition_is_correct:
            if (max_idx + 1) % 2 == 0:
                return (max(A_max_left, B_max_left) + min(A_min_right, B_min_right)) / 2
            else:
                left_size = A_idx + B_idx + 2
                right_size = (max_idx + 1) - left_size
                if left_size > right_size:
                    return max(A_max_left, B_max_left)
                else:
                    return min(A_min_right, B_min_right)
        else:
            if A_max_left > B_min_right:
                to_idx = A_idx - 1
            elif B_max_left > A_min_right:
                from_idx = A_idx + 1





A = [2,3,4,5,6]
B = [1]
6, 9, 10, 28, 50
print(median_of_two_arrays(A, B))


def findMedianSortedArrays(nums1, nums2) -> float:
    full_array = sorted(nums1 + nums2)
    if len(full_array) % 2 == 0:
        return (full_array[len(full_array)//2] + full_array[(len(full_array)//2) - 1]) / 2
    else:
        return full_array[len(full_array)//2]

print(findMedianSortedArrays(A, B))

