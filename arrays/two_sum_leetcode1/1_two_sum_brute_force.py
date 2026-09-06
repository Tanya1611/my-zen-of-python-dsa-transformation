'''
Time Complexity: O(N2) because we use two nested loops to check every possible pair of elements in the array, where N is the size of the array.

Space Complexity: O(1) as we use a constant amount of extra space regardless of input size.
'''

def twoSum(nums: list[int], target) -> int:

    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j]+nums[i] == target:
                return [i,j]
    return [-1,-1]


nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
target = int(input("Enter the target value: "))
indices = twoSum(nums, target)

print("The indices for target sum is:", indices)