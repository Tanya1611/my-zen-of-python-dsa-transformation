''' Third Maximum Number (LeetCode Problem 414)

Given an array of N integers, find the third maximum number in the array.
Note : If the third maximum does not exist, return the maximum number.

Example 1:
Input: nums = [1,2]
Output: 2
Explanation:
The first distinct maximum is 2.
The second distinct maximum is 1.
The third distinct maximum does not exist, so the maximum (2) is returned instead.

Example 2:
Input: nums = [2,2,3,1]
Output: 1
Explanation:
The first distinct maximum is 3.
The second distinct maximum is 2 (both 2's are counted together since they have the same value).
The third distinct maximum is 1.

Constraints:
1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1

'''

# Approaches: 
# 1) Using Python's built-in sort() method
# 2) Using Three Variables to Track Maximums

def thirdMax(nums: list[int]) -> int:
    
    '''
    Approach 1: Using Python's built-in sort() method
    Time Complexity: O(n log n) — Sorts the array in ascending order.
    Space Complexity: O(1) — Modifies the array in place.
    arr.sort()
    return arr[-3] if len(arr) >= 3 else arr[-1]

    
    Approach 2: Using Three Variables to Track Maximums
    Time Complexity: O(n) — Iterates through the original array once. 
    Space Complexity: O(1) — Requires no extra memory.
    '''

    first_msf = float('-inf')
    second_msf = float('-inf')
    third_msf = float('-inf')

    for num in nums:
        if num == first_msf or num == second_msf or num == third_msf:
            continue

        if num > first_msf:
            third_msf = second_msf
            second_msf = first_msf
            first_msf = num
        elif num > second_msf:
            third_msf = second_msf
            second_msf = num
        elif num > third_msf:
            third_msf = num
    if(third_msf == float('-inf')):
        return max(first_msf,second_msf)
    return third_msf

        

N = int(input("Enter the number of elements in the array: "))
arr = [int(input(f"Enter element of index {i}: ")) for i in range(N)]

print(f"The third maximum number is: {thirdMax(arr)}")

'''
Output:
Enter the number of elements in the array: 5
Enter element of index 0: 4
Enter element of index 1: 7
Enter element of index 2: 4
Enter element of index 3: 2
Enter element of index 4: 0
The third maximum number is: 2
'''