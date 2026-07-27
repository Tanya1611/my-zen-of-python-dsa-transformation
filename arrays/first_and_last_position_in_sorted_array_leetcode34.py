''' First and Last Position of Element in Sorted Array (LeetCode Problem 34)

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
> If target is not found in the array, return [-1, -1].
> You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]
 
Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
'''

import bisect

def searchRange(nums, target):

    # Approach: Using Binary Search with bisect module
    # Time Complexity: O(log n) — Binary search algorithm.
    left = bisect.bisect_left(nums, target)
    right = bisect.bisect_right(nums, target) - 1

    if left <= right:
        return [left, right]
    else:
        return [-1, -1]


nums = [int(x) for x in input("Enter the sorted array elements separated by space: ").split()]
target = int(input("Enter the target element to search: "))

result = searchRange(nums, target)
print(f"The first and last position of the target element is: {result}")

# Output is :
# Enter the sorted array elements separated by space: 5 7 7 8 8 10
# Enter the target element to search: 8
# The first and last position of the target element is: [3, 4]