''' Find the difference in ASCII codes between consecutive characters in a string.

Take as input S, a string. Write a program that inserts between each pair of characters the difference between their ascii codes and print the ans.

Sample Input:
acb

Sample Output:
a2c-1b

'''


s=input()
result = []
    
result.append(s[0])
for i in range(1, len(s)):
    diff = ord(s[i]) - ord(s[i-1])
    result.append(str(diff))
    result.append(s[i])
        
print("".join(result))

# Output
# andcbth
# a13n-10d-1c-1b18t-12h