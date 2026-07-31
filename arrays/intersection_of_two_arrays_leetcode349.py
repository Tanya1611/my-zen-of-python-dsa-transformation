''' Intersection of Two Arrays (LeetCode Problem 349)

Given two integer arrays nums1 and nums2, return an array of their intersection. 
> Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.
 
Constraints:
1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000

'''

def intersectionOfArrays(nums1: list[int], nums2: list[int]) -> list[int]:
    
    set1 = set(nums1)
    set2 = set(nums2)
    
    intersection = set1 & set2

    return list(intersection)

nums1 = list(map(int, input("Enter the elements of the first array (space-separated): ").split()))
nums2 = list(map(int, input("Enter the elements of the second array (space-separated): ").split()))
print(f"Intersection of the two arrays: {intersectionOfArrays(nums1, nums2)}")

'''
Output:
Enter the elements of the first array (space-separated): 1 3 5 2 7 4 5 9 5 
Enter the elements of the second array (space-separated): 7 4 3 2 5 8 5 3
Intersection of the two arrays: [2, 5, 7, 4, 3]
'''