def sortNums(arr):
    count0, count1, count2 = 0, 0, 0
    for num in arr:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    idx = 0
    for i in range(count0):
        arr[idx] = 0
        idx += 1

    for i in range(count1):
        arr[idx] = 1
        idx += 1

    for i in range(count2):
        arr[idx] = 2
        idx += 1

    return arr

def run_tests():
    test_cases = [
        {"input": ([0, 2, 1, 2, 0, 1, 0],), "expected": [0, 0, 0, 1, 1, 2, 2]},
        {"input": ([0, 0, 1, 1, 2, 2],), "expected": [0, 0, 1, 1, 2, 2]},
        {"input": ([0, 0, 0, 0],), "expected": [0, 0, 0, 0]},
        {"input": ([1, 1, 1, 1],), "expected": [1, 1, 1, 1]},
        {"input": ([2, 2, 2, 2],), "expected": [2, 2, 2, 2]},
        {"input": ([1],), "expected": [1]},
        {"input": ([],), "expected": []},
        {"input": ([2, 2, 1, 1, 0, 0],), "expected": [0, 0, 1, 1, 2, 2]},
        {"input": ([2, 1, 1, 0, 2, 0, 1],), "expected": [0, 0, 1, 1, 1, 2, 2]},
        {"input": ([2, 1, 2, 1, 1],), "expected": [1, 1, 1, 2, 2]},
    ]

    for i, test in enumerate(test_cases):
        arr = test["input"][0]  # Extract the array
        expected = test["expected"]
        result = sortNums(arr[:])  # Pass a copy of the array to avoid mutation issues
        print(f"Test Case {i + 1}: {'Passed' if result == expected else 'Failed'}")
        if result != expected:
            print(f"    Input: {test['input']}, Expected: {expected}, Got: {result}")

# Run the tests
if __name__ == "__main__":
    run_tests()
