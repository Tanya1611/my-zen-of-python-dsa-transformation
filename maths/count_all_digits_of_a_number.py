''' Count all Digits of a Number

> You are given an integer n. You need to print the number of digits in the number.
> The number will have no leading zeroes, except when the number is 0 itself.

Example:
Input: n = 14
Output: 2
Explanation: There are 2 digits in 14.

'''

def count_digits(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        n //= 10
        count += 1
    return count

number = int(input("Enter an integer: "))
digit_count = count_digits(number)
print(f"The number of digits in {number} is: {digit_count}")

# Output:
# Enter an integer: 2468
# The number of digits in 2468 is: 4