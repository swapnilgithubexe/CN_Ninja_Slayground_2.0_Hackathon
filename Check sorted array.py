def checkSortedArray(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

# Edge cases
print(checkSortedArray([]))               # Output: True (An empty array is considered sorted)
print(checkSortedArray([5]))              # Output: True (A single-element array is sorted)

# Sorted arrays
print(checkSortedArray([1, 2, 3, 4, 5]))  # Output: True (Array is sorted in ascending order)
print(checkSortedArray([10, 20, 30]))     # Output: True (Array is sorted in ascending order)

# Unsorted arrays
print(checkSortedArray([5, 4, 3, 2, 1]))  # Output: False (Array is sorted in descending order)
print(checkSortedArray([1, 3, 2, 4, 5]))  # Output: False (Array is not fully sorted)

# Arrays with duplicates
print(checkSortedArray([1, 2, 2, 3, 3]))  # Output: True (Array is sorted with duplicates)
print(checkSortedArray([1, 1, 1, 1]))     # Output: True (Array with all identical elements is sorted)

# Mixed arrays
print(checkSortedArray([3, 5, 8, 7, 10])) # Output: False (Array is not sorted)
print(checkSortedArray([1, 2, 3, 5, 4]))  # Output: False (Array is partially sorted but not fully)
