''' First Occurrence of Element in an UnsortedArray

Given an array of N integers and an integer T. Design an algorithm to find the first occurrence of T in the array.
Note : Output -1 if T is not present in the array.

Example:
Input: n = 5, arr = [1, 2, 3, 4, 5], T = 3
Output: 2
Explanation: The first occurrence of 3 is at index 2.

'''

# Approach: Iterate array -> Match the target value -> Return index => Linear Search

def first_occurrence(arr: list[int], t:int) -> int:
    for i, value in enumerate(arr):
        if value == t:
            return i
    return -1

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]
T = int(input("Enter the target value to find: "))

print(f"The first occurrence of {T} is at index: {first_occurrence(arr, T)}")


# Output:
# Enter the number of elements in the array: 5
# Enter element of index 0: 10
# Enter element of index 1: 30
# Enter element of index 2: 50
# Enter element of index 3: 20
# Enter element of index 4: 50
# Enter the target value to find: 50
# The first occurrence of 50 is at index: 2