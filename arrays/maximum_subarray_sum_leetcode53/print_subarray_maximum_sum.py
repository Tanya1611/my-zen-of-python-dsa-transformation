'''
Time Complexity: O(n), where n is the number of elements in the array. We traverse the array only once.

Space Complexity: O(1). We use a constant amount of space for variables.
'''

def maxSubArray(nums: list[int]) -> int:

    # Maximum sum
    maxSum = float("-inf")

    # Current sum of subarray
    sum = 0
    ansStart, ansEnd = -1, -1
    for i in range(len(nums)):
        ansStart = i
        # Add current element to the sum
        sum += nums[i] 
            
        # Update maxSum if current sum is greater
        if(sum>maxSum):
            maxSum = sum

        # Reset sum to 0 if it becomes negative
        if(sum<0):
            sum=0

    return ansStart, ansEnd

nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
startIndex, endIndex = maxSubArray(nums)
print("The subarrayy with maximum sum is:", nums[startIndex:endIndex+1])