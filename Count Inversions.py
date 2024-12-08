def countInversions(arr, n):
    ##Brute Force
    count = 0
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                count += 1

    return count


if __name__ == "__main__":
    # Basic Test
    arr1 = [1, 3, 2, 4]
    print(f"Test 1: {countInversions(arr1, len(arr1))}")  # Expected Output: 1

    # Sorted Array
    arr2 = [1, 2, 3, 4, 5]
    print(f"Test 2: {countInversions(arr2, len(arr2))}")  # Expected Output: 0

    # Reverse Sorted Array
    arr3 = [5, 4, 3, 2, 1]
    print(f"Test 3: {countInversions(arr3, len(arr3))}")  # Expected Output: 10

    # Array with Duplicates
    arr4 = [2, 3, 2, 3]
    print(f"Test 4: {countInversions(arr4, len(arr4))}")  # Expected Output: 1

    # Empty Array
    arr5 = []
    print(f"Test 5: {countInversions(arr5, len(arr5))}")  # Expected Output: 0

    # Single Element Array
    arr6 = [1]
    print(f"Test 6: {countInversions(arr6, len(arr6))}")  # Expected Output: 0

    # Array with All Equal Elements
    arr7 = [3, 3, 3, 3]
    print(f"Test 7: {countInversions(arr7, len(arr7))}")  # Expected Output: 0

