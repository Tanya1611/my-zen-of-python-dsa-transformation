"""Valid Anagrams

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input : s = "anagram" , t = "nagaram"
Output : true

Explanation :
We can rearrange the characters of string s to get string t as frequency of all characters from both strings is same.

Example 2:
Input : s = "dog" , t = "cat"
Output : false

Explanation :
We cannot rearrange the characters of string s to get string t as frequency of all characters from both strings is not same.
"""

def isAnagram(s: str, t: str) -> bool:

    # Time Complexity: O(N log N) due to sorting.
    # Space Complexity: O(N) to store sorted lists (sorted method is used).
    return len(s) == len(t) and sorted(s) == sorted(t)


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = isAnagram(str1, str2)
print("True" if result else "False")


'''
------------------OUTPUT--------------------
Enter first string: TERMINAL
Enter second string: RETLMNAI
True
--------------------------------------------
'''