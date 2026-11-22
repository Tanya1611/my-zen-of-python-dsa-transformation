''' Replace Pi with its actual value i.e., 3.14

Given a string, design a recursive algorithm to replace all the pi's in the given string with 3.14 and print the resulting string.

Example 1:
Input: "pip"
Output: "3.14p"
'''

def replace_pi(arr: list[str], i: int):

    if i>=len(arr)-1:
        return

    if arr[i]=="p" and arr[i+1]=="i":
        arr[i:i+2]=list("3.14")
        replace_pi(arr, i+4)
    else:
        replace_pi(arr,i+1)

text = list(input("Enter a string: "))
replace_pi(text,0)
print(f'Final replaced string is: {"".join(text)}')

# Output :
# Enter a string: pipipppip
# Final replaced string is: 3.143.14pp3.14p