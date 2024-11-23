def reverseNum(n):
    ans = 0
    for i in range(len(str(n))):
        remainder = n % 10
        ans = (ans * 10) + remainder
        n = n // 10

    return ans

# Single-digit numbers
print(reverseNum(0))           # Output: 0 (0 reversed is 0)
print(reverseNum(5))           # Output: 5 (5 reversed is 5)

# Multi-digit positive numbers
print(reverseNum(123))         # Output: 321 (123 reversed is 321)
print(reverseNum(987654321))   # Output: 123456789 (987654321 reversed is 123456789)


# Edge cases
print(reverseNum(10))          # Output: 1 (10 reversed is 1)
print(reverseNum(1000))        # Output: 1 (1000 reversed is 1)
