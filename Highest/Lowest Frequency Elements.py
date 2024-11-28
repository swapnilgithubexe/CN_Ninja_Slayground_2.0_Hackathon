def higherLowerFreqElements(arr):
    freq = {}
    h_freq_element = None
    h_freq = float("-inf")

    l_freq_element = None
    l_freq = float("inf")

    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for key, value in freq.items():
        if value < l_freq or (value == l_freq and key < l_freq_element):
            l_freq = value
            l_freq_element = key

        if value > h_freq or (value == h_freq and key < h_freq_element):
            h_freq = value
            h_freq_element = key

    return h_freq_element, l_freq_element

# Test Case 1: Normal Case
arr1 = [1, 2, 2, 3, 3, 3]
print("Test Case 1:", higherLowerFreqElements(arr1))  # Expected: (3, 1)

    # Test Case 2: All Elements Have Same Frequency
arr2 = [4, 4, 5, 5, 6, 6]
print("Test Case 2:", higherLowerFreqElements(arr2))  # Expected: (4, 4)

    # Test Case 3: Single Element Array
arr3 = [10]
print("Test Case 3:", higherLowerFreqElements(arr3))  # Expected: (10, 10)

    # Test Case 4: Array with Negative Numbers
arr4 = [-1, -1, -2, -2, -3, -3, -3]
print("Test Case 4:", higherLowerFreqElements(arr4))  # Expected: (-3, -1)

    # Test Case 5: Array with One Frequent Element
arr5 = [5, 5, 5, 5, 5]
print("Test Case 5:", higherLowerFreqElements(arr5))  # Expected: (5, 5)

    # Test Case 6: Array with Mixed Positive and Negative Numbers
arr6 = [-10, 0, -10, 10, 10, 10]
print("Test Case 6:", higherLowerFreqElements(arr6))  # Expected: (10, 0)

    # Test Case 7: Array with Duplicates and Unique Element
arr7 = [1, 1, 2, 3, 3, 3, 4, 4]
print("Test Case 7:", higherLowerFreqElements(arr7))  # Expected: (3, 2)

    # Test Case 8: Empty Array
arr8 = []
print("Test Case 8:", higherLowerFreqElements(arr8))  # Expected: (None, None)

    # Test Case 9: Large Array with Repeated Elements
arr9 = [7, 8, 7, 9, 8, 7, 8, 8, 9, 9, 9]
print("Test Case 9:", higherLowerFreqElements(arr9))  # Expected: (8, 7)

    # Test Case 10: All Identical Elements
arr10 = [42, 42, 42, 42]
print("Test Case 10:", higherLowerFreqElements(arr10))  # Expected: (42, 42)