'''
Time Complexity: O(N) because we traverse the array only once, and each lookup or insertion in the dictionary takes O(1) on average, where N is the size of the array.

Space Complexity: O(N) since in the worst case we may store all elements of the array in the dictionary.
'''

#Function to find the indices of target sum values
def twoSumUsingDict(nums: list[int], target: int):

    #Creating an empty dictionary
    dict_nums = {}
    flag = 0

    # Iterating over elements of array with indices
    for ind, element in enumerate(nums):

        req_element = target-element

        # if required values found then break and fetch it from dictionary
        if req_element in dict_nums.values():
            flag = 1
            endIndex = ind
            break

        # Store the current element and the index
        dict_nums[ind] = element


    if (flag):

        # Iterating over dictionary
        for key, value in dict_nums.items():

            # Take out the key which is the required index value
            if(value == req_element):
                startIndex = key
                return [startIndex, endIndex]
            
    return [-1,-1]

nums = list(map(int, input("Enter the elements of the array (space-separated): ").split()))
target = int(input("Enter the target value: "))
indices = twoSumUsingDict(nums, target)

print("The indices for target sum is:", indices)


'''
Output:

Enter the elements of the array (space-separated): 15 30 25 40 35 60 25
Enter the target value: 85
The indices for target sum is: [2, 5]
'''