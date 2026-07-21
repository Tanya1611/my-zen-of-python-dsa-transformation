''' Selection Sort Algorithm Implementation in Python

Given an array of N integers, sort the array in ascending order using the Selection Sort algorithm.

Example:
Input: nums = [70, 20, 50, 30, 10]
Output: [10, 20, 30, 50, 70]
Explanation: The array is sorted in ascending order using the Selection Sort algorithm.

> Selection Sort is a simple sorting algorithm that divides the input list into two parts: 
  - the sublist of items already sorted, which is built up from left to right at the front (left) of the list, 
  - and the sublist of items remaining to be sorted that occupy the rest of the list. 
> Initially, the sorted sublist is empty and the unsorted sublist is the entire input list. 
> The algorithm proceeds by finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, 
  - exchanging (swapping) it with the leftmost element of the unsorted sublist and moving the boundary of the sorted sublist one element to the right.
> Selection sort is not a stable sort, meaning that it does not preserve the relative order of equal elements.
> Selection sort is an in-place sorting algorithm, meaning it requires only O(1) extra memory space.

'''

def selectionSort(nums: list[int], n: int) -> None:
    '''
    Approach: Using Selection Sort Algorithm
    Time Complexity: O(n^2) — Nested loops iterate through the array.
    Space Complexity: O(1) — Modifies the array in place.
    
    TC: O(n^2) — In the best case, when the array is already sorted, the algorithm will still make the same number of comparisons.
    SC: O(1) — Still modifies the array in place.
    '''

    for i in range(1,n):
        min_idx = i-1
        for j in range(i, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i-1], nums[min_idx] = nums[min_idx], nums[i-1]
        

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

selectionSort(arr, N)
print(f"Sorted array using Selection Sort is: {arr}")

'''
Output:
Enter the number of elements in the array: 5
Enter element of index 0: 43
Enter element of index 1: 40
Enter element of index 2: 49
Enter element of index 3: 45
Enter element of index 4: 40
Sorted array using Selection Sort is: [40, 40, 43, 45, 49]
'''