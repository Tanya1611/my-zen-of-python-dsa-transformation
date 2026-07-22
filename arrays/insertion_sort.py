''' Insertion Sort Algorithm Implementation in Python

Given an array of N integers, sort the array in ascending order using the Insertion Sort algorithm.

Example:
Input: nums = [60, 20, 10, 40, 25]
Output: [10, 20, 25, 40, 60]
Explanation: The array is sorted in ascending order using the Insertion Sort algorithm.

> Insertion Sort is a simple sorting algorithm that builds the final sorted array one item at a time.
> Insertion sort is a stable sort, meaning that it preserves the relative order of equal elements.
> Insertion sort is an in-place sorting algorithm, meaning it requires only O(1) extra memory space.

'''

def insertionSort(nums: list[int], n: int) -> None:
    '''
    Approach: Using Insertion Sort Algorithm
    Time Complexity: O(n^2) — Nested loops iterate through the array.
    Space Complexity: O(1) — Modifies the array in place.
    
    In best case,
    TC: O(n) — When the input array is already sorted, the inner loop condition immediately fails, requiring only one comparison per element and zero shifting operations.
    SC: O(1) — Still modifies the array in place.
    '''

    for i in range(1,n):
        key = nums[i]
        j = i-1
        while j >= 0 and key < nums[j]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
        

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

insertionSort(arr, N)
print(f"Sorted array using Insertion Sort is: {arr}")

'''
Output:
Enter the number of elements in the array: 5
Enter element of index 0: 55
Enter element of index 1: 45
Enter element of index 2: 35
Enter element of index 3: 25
Enter element of index 4: 15
Sorted array using Insertion Sort is: [15, 25, 35, 45, 55]
'''