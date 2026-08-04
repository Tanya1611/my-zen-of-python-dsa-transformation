''' Toggle Case
Take as input S, a string. Write a function that toggles the case of all characters in the string. Print the value returned.

Constraints
Length of string should be between 1 to 1000.


Sample Input:
abC
Sample Output:
ABc

Explanation-
Toggle Case means to change UpperCase character to LowerCase character and vice-versa.
'''

text = input("Enter a string: ")

toggled = ""

for char in text:
    ascii_val = ord(char)
    if 65 <= ascii_val <= 90:
        toggled += chr(ascii_val + 32)
    elif 97 <= ascii_val <= 122:
        toggled += chr(ascii_val - 32)
    else:
        toggled += char

print("Toggled String: " + toggled)

# Output : 
# Enter a string: wELCOMetOgERMany
# Toggled String: WelcomEToGermANY