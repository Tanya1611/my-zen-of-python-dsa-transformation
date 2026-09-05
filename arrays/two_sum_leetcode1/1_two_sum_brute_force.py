

def twoSum(nums: list[int], target) -> int:

    start,end = -1,-1

    for i in range(len(nums)-1):
        start = i
        for j in range(i+1,len(nums)):
            if nums[j]+nums[i] == target:
                end=j
                return [i,j]
    return [-1,-1]


nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

indices = twoSum(nums, target)

print("The indices for trget sum is:", indices)