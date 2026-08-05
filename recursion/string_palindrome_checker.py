''' Palindrome Checker using Recursion

Take as input a string and write a function that checks if the string is a palindrome using recursion. 
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).

Example 1:
Input: Gracious
Output: False

Example 2:
Input: racecar
Output: True
'''

def is_palindrome(text):
    # Base Case: Empty or single-character string
    if len(text) <= 1:
        return True
    
    # If the first character is a space/punctuation, skip it
    if not text[0].isalnum():
        return is_palindrome(text[1:])
        
    # If the last character is a space/punctuation, skip it
    if not text[-1].isalnum():
        return is_palindrome(text[:-1])
        
    # Compare matching case-insensitive characters, then move inward
    if text[0].lower() == text[-1].lower():
        return is_palindrome(text[1:-1])
        
    return False

text = input("Enter a string: ")
lowered_no_spaces_text = text.lower().strip()  # Convert to lowercase for case-insensitive comparison
if is_palindrome(lowered_no_spaces_text):
    print(f'"{text}" is a palindrome.') 
else:
    print(f'"{text}" is not a palindrome.')

# Time Complexity: O(n) where n is the length of the string
# Space Complexity: O(n) due to the recursive call stack

# Output :
# Enter a string: No Lemon No Melon
# "No Lemon No Melon" is a palindrome.