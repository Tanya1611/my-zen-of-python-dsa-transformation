''' Binary Search (LeetCode Problem 704)

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

'''

def binarySearch(nums: list[int], target: int) -> int:
    low, high = 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

        

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

target = int(input("Enter the target element to search: "))
print(f"Index of target element is: {binarySearch(arr, target)}")

'''
Output:
Enter the number of elements in the array: 5
Enter element of index 0: 2
Enter element of index 1: 4
Enter element of index 2: 6
Enter element of index 3: 8
Enter element of index 4: 9
Enter element of index 5: 10
Enter the target element to search: 9
Index of target element is: 4
'''