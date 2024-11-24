def gcdCacl(n, m):
    while m:
        n, m = m, n % m
    return n


if __name__ == "__main__":
    print("Test Case 1: Basic GCD")
    print("Input: 54, 24 | Expected Output: 6 | Actual Output:", gcdCacl(54, 24))
    print()

    print("Test Case 2: Co-prime Numbers")
    print("Input: 101, 103 | Expected Output: 1 | Actual Output:", gcdCacl(101, 103))
    print()

    print("Test Case 3: One Number is Zero")
    print("Input: 0, 15 | Expected Output: 15 | Actual Output:", gcdCacl(0, 15))
    print("Input: 22, 0 | Expected Output: 22 | Actual Output:", gcdCacl(22, 0))
    print()

    print("Test Case 4: Same Numbers")
    print("Input: 12, 12 | Expected Output: 12 | Actual Output:", gcdCacl(12, 12))
    print()

    print("Test Case 5: One Number is 1")
    print("Input: 1, 50 | Expected Output: 1 | Actual Output:", gcdCacl(1, 50))
    print("Input: 50, 1 | Expected Output: 1 | Actual Output:", gcdCacl(50, 1))
    print()

    print("Test Case 6: Large Numbers")
    print("Input: 123456, 789012 | Expected Output: 12 | Actual Output:", gcdCacl(123456, 789012))