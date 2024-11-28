def secondLargestSmallestNums(arr):
    highest = float("-inf")
    second_highest = float("-inf")

    smallest = float("inf")
    second_smallest = float("inf")

    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num


        if num > highest:
            second_highest = highest
            highest = num
        elif num > second_highest and num != highest:
            second_highest = num

    return second_highest, second_smallest


    # Test Case 1: Normal Case
arr1 = [1, 2, 3, 4, 5]
print("Test Case 1:", secondLargestSmallestNums(arr1))  # Expected: (4, 2)

    # Test Case 2: Array with Duplicates
arr2 = [1, 1, 2, 2, 3, 3]
print("Test Case 2:", secondLargestSmallestNums(arr2))  # Expected: (2, 2)

    # Test Case 3: Single Element Array
arr3 = [10]
print("Test Case 3:", secondLargestSmallestNums(arr3))  # Expected: (-inf, inf)

    # Test Case 4: Array with Negative Numbers
arr4 = [-10, -20, -30, -40]
print("Test Case 4:", secondLargestSmallestNums(arr4))  # Expected: (-20, -30)

    # Test Case 5: Array with All Identical Elements
arr5 = [5, 5, 5, 5]
print("Test Case 5:", secondLargestSmallestNums(arr5))  # Expected: (-inf, inf)

    # Test Case 6: Array with Mixed Positive and Negative Numbers
arr6 = [-10, 0, 10, 20]
print("Test Case 6:", secondLargestSmallestNums(arr6))  # Expected: (10, 0)

    # Test Case 7: Empty Array
arr7 = []
print("Test Case 7:", secondLargestSmallestNums(arr7))  # Expected: (-inf, inf)
