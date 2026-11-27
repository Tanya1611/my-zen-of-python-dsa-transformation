''' Print decreasing

Given two non-negative integers x and n, design a recursive algoritm to computer x raised to the power n.

Example :
Input: 
x = 2
n = 3
Output: 
Result is 8
'''

def power_func(x:int, n:int) -> int:
    # Base case
    if n==0:
        return 1

    A = power_func(x, n//2)

    return A*A if n%2 ==0 else A*A*x
    

x = int(input("x = "))
n = int(input("n = "))
print(f"Result is {power_func(x, n)}")

# Output :
# x = 5
# n = 2
# Result is 25