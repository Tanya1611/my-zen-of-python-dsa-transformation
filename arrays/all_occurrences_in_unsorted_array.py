''' All Occurrences of Element in an Unsorted Array

Given an array of N integers and an integer T. Design an algorithm to find the indices of all occurrences of T in the array.
Note : Output -1 if T is not present in the array.

Example:
Input: n = 5, arr = [1, 2, 3, 2, 7], T = 2
Output: 
1
3
Explanation: The occurrences of element 2 are at indices 1 and 3.

'''

# Approach: Iterate array -> Match the target value -> Maintain a flag checker -> Print index

def all_occurrences(arr: list[int], t:int) -> None:
    flag = False
    for i, value in enumerate(arr):
        if value == t:
            flag = True
            print(i)
    if not flag:
        print(-1)

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]
T = int(input("Enter the target value to find indices: "))

all_occurrences(arr, T)

# Output:
# Enter the number of elements in the array: 5
# Enter element of index 0: 45
# Enter element of index 1: 35
# Enter element of index 2: 55
# Enter element of index 3: 15
# Enter element of index 4: 45
# Enter the target value to find indices: 45
# 0
# 4
