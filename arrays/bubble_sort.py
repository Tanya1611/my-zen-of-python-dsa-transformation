''' Bubble Sort Algorithm Implementation in Python

Given an array of N integers, sort the array in ascending order using the Bubble Sort algorithm.

Example:
Input: nums = [5, 1, 4, 2, 8]
Output: [1, 2, 4, 5, 8]
Explanation: The array is sorted in ascending order using the Bubble Sort algorithm.

> Bubble Sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements and swaps them if they are in the wrong order. 
> In each pass through the list, the largest unsorted element "bubbles" up to its correct position.
> The algorithm gets its name because smaller elements "bubble" to the top of the list.
> Bubble sort has n-1 passes through the list, where n is the number of elements in the list.

'''


def bubbleSort(nums: list[int], n: int) -> None:
    '''
    Approach: Using Bubble Sort Algorithm
    Time Complexity: O(n^2) — Nested loops iterate through the array.
    Space Complexity: O(1) — Modifies the array in place.

    
    TC: O(n) — In the best case, when the array is already sorted, the algorithm will only make one pass through the array.
    SC: O(1) — Still modifies the array in place.
    '''

    for i in range(1,n):
        flag = False                      # Flag to check if any swaps were made during the pass
        for j in range(n-i):
            if nums[j] > nums[j+1]:       # If the current element is greater than the next element, swap them
                nums[j], nums[j+1] = nums[j+1], nums[j]
                flag = True               # Flag is set to True if a swap is made
        if not flag:                      # If no swaps were made, the array is already sorted
            break                         # Break out of the loop early to optimize performance 
        

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

bubbleSort(arr, N)
print(f"Sorted array using Bubble Sort is: {arr}")

'''
Output:
Enter the number of elements in the array: 5
Enter element of index 0: 150
Enter element of index 1: 130
Enter element of index 2: 100
Enter element of index 3: 170
Enter element of index 4: 100
Sorted array using Bubble Sort is: [100, 100, 130, 150, 170]
'''