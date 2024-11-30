def binarySearch(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


arr = [1, 2, 3, 4, 5]
target = 3
print(f"Test Case 1: {binarySearch(arr, target)} == 2")

    # Test Case 2: Target is at the beginning
arr = [1, 2, 3, 4, 5]
target = 1
print(f"Test Case 2: {binarySearch(arr, target)} == 0")

    # Test Case 3: Target is at the end
arr = [1, 2, 3, 4, 5]
target = 5
print(f"Test Case 3: {binarySearch(arr, target)} == 4")

    # Test Case 4: Target is not in the array
arr = [1, 2, 3, 4, 5]
target = 6
print(f"Test Case 4: {binarySearch(arr, target)} == -1")

    # Test Case 5: Empty array
arr = []
target = 3
print(f"Test Case 5: {binarySearch(arr, target)} == -1")

    # Test Case 6: Single element array (target exists)
arr = [3]
target = 3
print(f"Test Case 6: {binarySearch(arr, target)} == 0")

    # Test Case 7: Single element array (target does not exist)
arr = [3]
target = 1
print(f"Test Case 7: {binarySearch(arr, target)} == -1")

    # Test Case 8: Array with duplicate elements (target exists)
arr = [1, 1, 2, 3, 3, 4, 5]
target = 3
print(f"Test Case 8: {binarySearch(arr, target)} == 3 or 4")

    # Test Case 9: Array with negative numbers
arr = [-5, -3, -1, 0, 1, 3, 5]
target = -3
print(f"Test Case 9: {binarySearch(arr, target)} == 1")

    # Test Case 10: Large array
arr = list(range(1, 10001))
target = 9999
print(f"Test Case 10: {binarySearch(arr, target)} == 9998")
