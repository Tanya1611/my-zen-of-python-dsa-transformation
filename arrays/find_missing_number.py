'''   Find missing number

Problem: Given an integer array of size n containing distinct values in the range from 0 to n (inclusive), return the only number missing from the array within this range.

Example 1:
Input: nums = [0, 2, 3, 1, 4]
Output: 5

Explanation:
nums contains 0, 1, 2, 3, 4 thus leaving 5 as the only missing number in the range [0, 5]

Example 2:
Input: nums = [0, 1, 2, 4, 5, 6]
Output: 3

Explanation:
nums contains 0, 1, 2, 4, 5, 6 thus leaving 3 as the only missing number in the range [0, 6]


Constraints:
n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique.
'''

def missingNumber(nums: list[int]) -> int:
    
    N = len(nums) 
        
    for i in range(0, N+1):
        flag = 0
            
        for num in nums:
            if num == i:
                flag = 1
                break
            
        
        if flag == 0:
            return i
        
    return -1
 

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

ans = missingNumber(arr)
    
print(f"The missing number is: {ans}")