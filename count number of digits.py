def countNumOfDigits(n):
    count = 0
    for i in str(abs(n)):
        count += 1
    return count

# Single-digit numbers
print(countNumOfDigits(0))           # Output: 1 (0 has 1 digit)
print(countNumOfDigits(5))           # Output: 1 (5 has 1 digit)
print(countNumOfDigits(-7))          # Output: 1 (-7 has 1 digit)

# Multi-digit positive numbers
print(countNumOfDigits(123))         # Output: 3 (123 has 3 digits)
print(countNumOfDigits(987654321))   # Output: 9 (987654321 has 9 digits)

# Multi-digit negative numbers
print(countNumOfDigits(-456))        # Output: 3 (-456 has 3 digits)
print(countNumOfDigits(-1000000))    # Output: 7 (-1000000 has 7 digits)

# Edge cases
print(countNumOfDigits(10))          # Output: 2 (10 has 2 digits)
print(countNumOfDigits(-10))         # Output: 2 (-10 has 2 digits)
print(countNumOfDigits(1000000000))  # Output: 10 (1 billion has 10 digits)
