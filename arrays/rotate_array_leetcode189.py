''' Rotate Array (LeetCode Problem 189)

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

'''

def rotateArray(nums: list[int], k: int) -> None:
    
    # Approach: Reverse the entire array, then reverse the first k elements and the remaining n-k elements.
    # Time Complexity: O(n) — Reverses the array three times.
    k %= len(nums)
    nums.reverse()
    nums[:k]=nums[:k][::-1]
    nums[k:]=nums[k:][::-1]

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]
k = int(input("Enter the number of steps to rotate the array: "))
rotateArray(arr, k)
print(f"Rotated array: {arr}")


'''
Output:
Enter the number of elements in the array: 5
Enter element of index 0: 10
Enter element of index 1: 20
Enter element of index 2: 30
Enter element of index 3: 40
Enter element of index 4: 50
Enter the number of steps to rotate the array: 2
Rotated array: [30, 40, 50, 10, 20]
'''