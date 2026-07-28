''' First Occurrence of Element in an Sorted Array

Given a sorted array of N integers and an integer T. Design an algorithm to find the first occurrence of T in the array.
Note : Output -1 if T is not present in the array.

Example:
Input: n = 5, arr = [1, 3, 3, 10, 15], T = 3
Output: 1
Explanation: The first occurrence of 3 is at index 1.

'''

# Approach: Use Binary Search to find the first occurrence of the target value in a sorted array.
# Time Complexity: O(log n) — Binary search algorithm.

def sorted_first_occurrence(arr: list[int], t: int) -> int:
    lo, hi = 0, len(arr)-1
    temp = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == t:
            temp = mid
            hi = mid - 1     # Move left to find the first occurrence
        elif arr[mid] < t:
            lo = mid + 1
        else:
            hi = mid - 1
    return temp

N = int(input("Enter the number of elements in the sorted array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]
T = int(input("Enter the target value to find: "))

result = sorted_first_occurrence(arr, T)
print(f"The first occurrence of {T} is at index: {result}")

# Output:
# Enter the number of elements in the array: 5
# Enter element of index 0: 10
# Enter element of index 1: 20
# Enter element of index 2: 50
# Enter element of index 3: 60
# Enter element of index 4: 60
# Enter the target value to find: 60
# The first occurrence of 60 is at index: 3