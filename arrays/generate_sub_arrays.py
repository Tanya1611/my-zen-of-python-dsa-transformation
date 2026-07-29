''' Generate all sub-arrays of an array

Given an array of n integers, generate all possible sub-arrays of the given array.

Example:
Input: nums = [1, 2, 3]
Output: 
1
1 2 3
2 
2 3
3

'''

# Time Complexity: O(n^3) — Three nested loops to generate all sub-arrays.
def generate_sub_arrays(nums: list[int]) -> None:
    n = len(nums)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(nums[k], end=" ")
            print()

nums = [int(x) for x in input("Enter the array elements separated by space: ").split()]

generate_sub_arrays(nums)

# Output is :
# Enter the array elements separated by space: 2 4 6 8
# 2
# 2 4
# 2 4 6
# 2 4 6 8
# 4
# 4 6
# 4 6 8
# 6
# 6 8
# 8