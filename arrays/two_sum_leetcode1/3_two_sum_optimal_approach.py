'''
Time Complexity: O(N log N) due to sorting the array initially, where N is the number of elements. 
                 The two-pointer traversal runs in O(N).

Space Complexity: O(N) because we store the array elements along with their original indices in a separate list or vector for sorting, maintaining original positions.
'''

def twoSumIndices(arr, target):
    # Create list of tuples (value, original_index)
    nums_with_index = [(num, idx) for idx, num in enumerate(arr)]
    
    # Sort the list by values
    nums_with_index.sort(key=lambda x: x[0])

    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = nums_with_index[left][0] + nums_with_index[right][0]
        if current_sum == target:
            # Return original indices of found elements
            return [nums_with_index[left][1], nums_with_index[right][1]]
        elif current_sum < target:
            # Move left pointer right to increase sum
            left += 1
        else:
            # Move right pointer left to decrease sum
            right -= 1
    
    # No valid pair found
    return [-1, -1]

nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
target = int(input("Enter the target value: "))
indices = twoSumIndices(nums, target)

print("The indices for target sum is:", indices)