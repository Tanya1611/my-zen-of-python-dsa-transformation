'''Remove All Duplicates from a String

The task is to remove all duplicate characters from a string while keeping the first occurrence of each character in its original order.
'''

s = input("Enter a string: ").lower()
seen = set()  
res = ""      
for char in s:
    if char not in seen:
        seen.add(char)
        res += char

print(f"Result is: {res}")

# Output:
# Enter a string: Golgappa
# Result is: golap