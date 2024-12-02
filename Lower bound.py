def lowerBound(arr, x):
    n = len(arr)
    for i in range(n):
        if arr[i] >= x:
            return i
    return n

def run_tests():
    test_cases = [
        {"input": ([1, 2, 4, 6, 8], 5), "expected": 3},
        {"input": ([1, 2, 3, 4, 5], 3), "expected": 2},
        {"input": ([1, 2, 3, 4, 5], 6), "expected": 5},
        {"input": ([1, 2, 3, 4, 5], 1), "expected": 0},
        {"input": ([1, 3, 5, 7], 2), "expected": 1},
        {"input": ([10, 20, 30, 40], 25), "expected": 2},
        {"input": ([10, 20, 30, 40], 50), "expected": 4},
        {"input": ([], 5), "expected": 0},  # Edge case: empty array
    ]

    for i, test in enumerate(test_cases):
        arr, x = test["input"]
        expected = test["expected"]
        result = lowerBound(arr, x)
        print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'}")
        if result != expected:
            print(f"    Input: {test['input']}, Expected: {expected}, Got: {result}")

# Run the tests
if __name__ == "__main__":
    run_tests()
