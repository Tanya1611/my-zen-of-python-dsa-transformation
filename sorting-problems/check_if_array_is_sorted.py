''' Check if an Array is Sorted

Problem Statement: 
Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. 
If the array is sorted then return True, Else return False.

Example 1:
Input: N = 5, array[] = {1,2,3,4,5}
Output: True.
Explanation: The given array is sorted i.e Every element in the array is smaller than or equals to its next values, So the answer is True.

Example 2:
Input: N = 5, array[] = {5,4,6,7,8}
Output: False.
Explanation: The given array is Not sorted i.e Every element in the array is not smaller than or equal to its next values, So the answer is False.
Here element 5 is not smaller than or equal to its future elements.
'''

def check_array_sorted(arr :list[int], n: int) -> bool :

    # Bruteforce : String from beginning - pick an element and check all other elements are greater than or equal to it & Repeat till last element.
    # Time Complexity: O(N2), as it uses two nested loops to compare every pair of elements in the array.
    # Space Complexity: O(1), as no extra space is used apart from a few variables.
    
    #for i in range(n-1):
    #    for j in range(i+1,n):
    #        If any element is smaller than the previous one, return false
    #        if arr[j]<arr[i]:
    #            return False
    

    # Optimal : Check every element with its previous element if the previous element is smaller than or equal to the current element then we will move to the next index.
    # Time Complexity: O(N), as it checks each adjacent pair once in a single pass through the array.
    # Space Complexity: O(1), as it uses constant extra space regardless of input size.
    for i in range(1,n):
        if arr[i]<arr[i-1]:
            return False

    return True

n = int(input("Enter number of elements in an array: "))
arr = [int(input(f"Enter element at index {i}: ")) for i in range(n)]
checker = check_array_sorted(arr, n)
if(checker):
    print("Array is Sorted.")
else:
    print("Array is Unsorted.")

# Output:
# Enter the number of elements in the array: 5
# Enter element of index 0: 101
# Enter element of index 1: 102
# Enter element of index 2: 101
# Enter element of index 3: 104
# Enter element of index 4: 106
# Array is Unsorted.