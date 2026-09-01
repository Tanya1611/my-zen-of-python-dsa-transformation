'''
Time Complexity: O(N^2), where N is the size of the array. 
This is because we have two nested loops: one for the starting index and one for the ending index of the subarray.

Space Complexity: O(1), as we are using a constant amount of space for variables, regardless of the input size.
'''

# Function to find maximum sum of subarrays
def maxSubArray(nums: list[int]) -> int:
    
    maxSum = float('-inf')

    # Iterate over each starting index of subarrays
    for i in range(len(nums)):

        sum = 0
        for j in range(i, len(nums)):

            # Add the current element nums[j] to the sum i.e. sum of nums[i...j-1]
            sum += nums[j]
            maxSum = max(maxSum, sum)

    return maxSum


nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
maxSum = maxSubArray(nums)
print("The maximum subarray sum is:", maxSum)