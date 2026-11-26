''' Print decreasing

Given a positive integer N, design a recursive algorithm to print numbers from N to 1 in the decreasing order.

Example 1:
Input: 10
Output: 10 9 8 7 6 5 4 3 2 1
'''

def print_decreasing(n: int) -> None:
    # Base case
    if n==0:
        return

    print(n, end = " ")
    print_decreasing(n-1)
    

num = int(input("Enter a number: "))
print_decreasing(num)

# Output :
# Enter a number: 5
# 5 4 3 2 1