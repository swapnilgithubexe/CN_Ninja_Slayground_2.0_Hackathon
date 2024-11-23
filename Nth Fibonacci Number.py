def nthFibonacciNumber(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a = 0
    b = 1
    for i in range(2, n+1):
        a, b = b, a + b

    return b

# Edge cases
print(nthFibonacciNumber(0))  # Output: 0 (0th Fibonacci number is 0)
print(nthFibonacciNumber(1))  # Output: 1 (1st Fibonacci number is 1)

# Small numbers
print(nthFibonacciNumber(2))  # Output: 1 (2nd Fibonacci number is 1)
print(nthFibonacciNumber(3))  # Output: 2 (3rd Fibonacci number is 2)
print(nthFibonacciNumber(5))  # Output: 5 (5th Fibonacci number is 5)

# Larger numbers
print(nthFibonacciNumber(10))  # Output: 55 (10th Fibonacci number is 55)
print(nthFibonacciNumber(20))  # Output: 6765 (20th Fibonacci number is 6765)

# Very large numbers
print(nthFibonacciNumber(50))  # Output: 12586269025 (50th Fibonacci number is 12586269025)
