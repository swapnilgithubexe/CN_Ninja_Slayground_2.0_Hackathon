def checkPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Edge cases
print(checkPrime(1))  # Output: False (1 is not a prime number)
print(checkPrime(2))  # Output: True (2 is a prime number)
print(checkPrime(3))  # Output: True (3 is a prime number)

# Small prime numbers
print(checkPrime(5))  # Output: True (5 is a prime number)
print(checkPrime(7))  # Output: True (7 is a prime number)

# Non-prime numbers
print(checkPrime(4))  # Output: False (4 is not a prime number)
print(checkPrime(6))  # Output: False (6 is not a prime number)
print(checkPrime(8))  # Output: False (8 is not a prime number)
print(checkPrime(9))  # Output: False (9 is not a prime number)

# Larger prime numbers
print(checkPrime(29))  # Output: True (29 is a prime number)
print(checkPrime(31))  # Output: True (31 is a prime number)

# Large non-prime number
print(checkPrime(100))  # Output: False (100 is not a prime number)
print(checkPrime(121))  # Output: False (121 is not a prime number)

# Very large prime number
print(checkPrime(104729))  # Output: True (104729 is a prime number)
