def factorial(n):
    # Base case: 0! or 1! is always 1
    if n <= 1:
        return 1
    
    # Recursive case: n * (n-1)!
    return n * factorial(n - 1)


print(factorial(5))  # Output: 120
