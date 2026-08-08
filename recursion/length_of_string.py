''' Find length of string using recursion

Take as input a string and write a function that returns the length of the string using recursion.

Example 1:
Input: Hello
Output: 5
'''

def length_of_string(s):
    # Base Case: If the string is empty, return 0
    if s == "":
        return 0
    else:
        # Recursive Case: Return 1 + length of the rest of the string
        return 1 + length_of_string(s[1:])

text = input("Enter a string: ")
length = length_of_string(text)
print(f'The length of the string "{text}" is: {length}')

# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) due to the recursive call stack    

# Output :
# Enter a string: Germany
# The length of the string "Germany" is: 7