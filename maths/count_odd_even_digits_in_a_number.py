''' Count number of Odd and Even Digits in a Number

> You are given an integer n. You need to print the number of odd and even digits present in the number.
> The number will have no leading zeroes, except when the number is 0 itself.


Example:
Input: n = 47
Output: Odd digits: 1, Even digits: 1
Explanation: There is 1 odd digit (7) and 1 even digit (4) in 47.

'''

def count_odd_even_digits(n):
    count_odd = 0
    count_even = 0
    if n == 0:
        return 0,1            #Return 0 odd digits and 1 even digit for the number 0
    
    while n > 0:
        digit = n%10
        if digit % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
        n //= 10

    return count_odd, count_even

number = int(input("Enter an integer: "))
count_odd, count_even = count_odd_even_digits(number)
print(f"The number of odd digits in {number} is: {count_odd}")
print(f"The number of even digits in {number} is: {count_even}")

# Output:
# Enter an integer: 47920
# The number of odd digits in 47920 is: 2
# The number of even digits in 47920 is: 3