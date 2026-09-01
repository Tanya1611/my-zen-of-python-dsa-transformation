'''
Time Complexity: O(N^3), where N is the size of the array. 
This is because we have three nested loops: 
-> one for the starting index
-> one for the ending index
-> one for calculating the sum of the subarray.

Space Complexity: O(1), as we are using a constant amount of space for variables, regardless of the input size.

'''

# Function to find maximum sum of subarrays
def maxSubArray(nums: list[int]) -> int:
    
    maxSum = float('-inf')

    # Iterate over each starting index of subarrays
    for i in range(len(nums)):
        
        for j in range(i, len(nums)):

            #Variable to store the sum of the current subarray
            sum = 0

            # Calculate the sum of subarray nums[i...j]
            for k in range(i, j + 1):
                sum += nums[k]

            maxSum = max(maxSum, sum)

    return maxSum


nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))

maxSum = maxSubArray(nums)

print("The maximum subarray sum is:", maxSum)