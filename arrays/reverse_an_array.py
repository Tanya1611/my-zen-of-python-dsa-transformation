''' Reverse an Array

Given an array of N integers, design an algorithm to reverse the array.

Example:
Input: n = 5, arr = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: The array is reversed.

'''

# Approaches: 
# 1) Use Python's built-in reverse() method
# 2) Use Temporary Array
# 3) Use Slicing
# 4) Use Two Pointers approach

def reverse_array(arr: list[int], n: int) -> None:

    # Approach 1: Using Python's built-in reverse() method
    # Time Complexity: O(n) — Highly optimized low-level execution loop.
    # Space Complexity: O(1) — Modifies the array in place.
    # arr.reverse()

    # Approach 2: Using Slicing
    # Time Complexity: O(n) — Copy every single element into the new array.
    # Space Complexity: O(n) — Creates an entirely new array in memory rather than modifying the original one in place.
    # arr = arr[::-1]
    
    # Approach 3:Using Temporary Array
    # Time Complexity: O(n) — Iterates through the original array once.
    # Space Complexity: O(n) — Requires additional memory equal to the array size.
    # rev_arr = []
    # for i in range(n-1, -1, -1):
    #     rev_arr.append(arr[i])

    # Approach 3: Using Two Pointers / In Place Swapping approach
    # Time Complexity: O(n) — Solves in exactly n//2 iterations.
    # Space Complexity: O(1) — Requires no extra memory.
    # For Loop
    x=n//2
    for i in range(x):
        arr[i], arr[n-i-1] = arr[n-i-1], arr[i]

    # While Loop
    # i, j = 0, n-1
    # while i < j:
    #     arr[i], arr[j] = arr[j], arr[i]
    #     i += 1
    #     j -= 1

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

reverse_array(arr, N)
print(f"The reversed array is: {arr}")


# Output:
# Enter the number of elements in the array: 7
# Enter element of index 0: 2
# Enter element of index 1: 4
# Enter element of index 2: 6
# Enter element of index 3: 8
# Enter element of index 4: 10
# Enter element of index 5: 12
# Enter element of index 6: 14
# The reversed array is: [14, 12, 10, 8, 6, 4, 2]