''' String Compression

Take as input S, a string. Write a function that does basic string compression. Print the value returned. E.g. for input “aaabbccds” print out a3b2c2ds.


Input Format
A single String S.


Constraints
A string of length between 1 to 1000

Sample Input
aaabbccds

Sample Output
a3b2c2ds

Explanation
In the given sample test case 'a' is repeated 3 times consecutively, 'b' is repeated twice, 'c' is repeated twice. 
But, 'd' and 's' occurred only once that's why we do not write their occurrence.

'''


text = input("Enter a string: ") 
    
result = [text[0]]
ind=0
point=0
for char in text[1:]:
    if char != result[-1]:
        if ind>0:
            result.append(str(ind+1))
        result.append(text[point+1])
        ind=0
    else:
        ind += 1
    point +=1
if(result[-1] >='a' and result[-1] <='z' and ind>0):
    result.append(str(ind+1))
print("Compressed String: " + "".join(result))

# Output:
# Enter a string: aaahhhdddggcvruuu
# Compressed String: a3h3d3g2cvru3