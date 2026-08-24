'''Move all Zeros to the end of the array

Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.

Example 1:
Input: 1 ,0 ,2 ,3 ,0 ,4 ,0 ,1
Output: 1 ,2 ,3 ,4 ,1 ,0 ,0 ,0
Explanation: All the zeros are moved to the end and non-negative integers are moved to front by maintaining order

Example 2:
Input : 1,2,0,1,0,4,0
Output: 1,2,1,4,0,0,0
Explanation : All the zeros are moved to the end and non-negative integers are moved to front by maintaining order
'''

def moveZeroes(arr):
        
    temp = [0] * len(arr)
    index = 0

    for num in arr:
        # If non-zero, copy to temp
        if num != 0:
            temp[index] = num
            index += 1

        # Copy temp back to original
    for i in range(len(arr)):
        arr[i] = temp[i]

    return arr


n = int(input("Enter number of elements in an array: "))
arr = [int(input(f"Enter element at index {i}: ")) for i in range(n)]  
result = moveZeroes(arr)
    
print("Array after moving zeroes:", end=" ")
for num in result:
    print(num, end=" ")

'''
Time Complexity: O(N), we can move all zeroes to end in linear time.
Space Complexity: O(N), additional space used for temporary array.

Output:
Enter number of elements in an array: 5
Enter element at index 0: 0
Enter element at index 1: 2
Enter element at index 2: 0
Enter element at index 3: 3
Enter element at index 4: 1
Array after moving zeroes: 2 3 1 0 0
'''