''' Print increasing

Given a positive integer N, design a recursive algorithm to print numbers from 1 to N in the increasing order.

Example 1:
Input: 10
Output: 1 2 3 4 5 6 7 8 9 10
'''

def print_increasing(n: int) -> None:
    # Base case
    if n==0:
        return

    print_increasing(n-1)
    print(n, end = " ")

num = int(input("Enter a number: "))
print_increasing(num)

# Output :
# Enter a number: 7
# 1 2 3 4 5 6 7