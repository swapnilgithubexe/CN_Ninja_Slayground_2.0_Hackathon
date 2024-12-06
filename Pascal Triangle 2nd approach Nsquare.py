def pascalTriangle(n: int):
    triangle = []

    for i in range(n):
        ans = []
        value = 1
        for j in range(i + 1):
            ans.append(value)
            value = value * (i - j) // (j + 1)

        print()
        triangle.append(ans)

    return triangle

def test_pascalTriangle():
    # Test case 1: n = 1
    # Output: [[1]]
    print("Test Case 1: n = 1")
    print(pascalTriangle(1))

    # Test case 2: n = 2
    # Output: [[1], [1, 1]]
    print("\nTest Case 2: n = 2")
    print(pascalTriangle(2))

    # Test case 3: n = 3
    # Output: [[1], [1, 1], [1, 2, 1]]
    print("\nTest Case 3: n = 3")
    print(pascalTriangle(3))

    # Test case 4: n = 4
    # Output: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
    print("\nTest Case 4: n = 4")
    print(pascalTriangle(4))

    # Test case 5: n = 5
    # Output:
    # [
    #  [1],
    #  [1, 1],
    #  [1, 2, 1],
    #  [1, 3, 3, 1],
    #  [1, 4, 6, 4, 1]
    # ]
    print("\nTest Case 5: n = 5")
    print(pascalTriangle(5))

if __name__ == "__main__":
    test_pascalTriangle()