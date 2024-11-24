def reverseArray(n: int, nums: list[int]) -> list[int]:
    front = 0
    end = n - 1
    while end > front:
        nums[front], nums[end] = nums[end], nums[front]
        front += 1
        end -= 1

    return nums

# Test Case 1: Array with multiple elements
n = 5
nums = [1, 2, 3, 4, 5]
print(reverseArray(n, nums))  # Expected Output: [5, 4, 3, 2, 1]

# Test Case 2: Array with two elements
n = 2
nums = [10, 20]
print(reverseArray(n, nums))  # Expected Output: [20, 10]

# Test Case 3: Array with one element
n = 1
nums = [42]
print(reverseArray(n, nums))  # Expected Output: [42]

# Test Case 4: Empty array
n = 0
nums = []
print(reverseArray(n, nums))  # Expected Output: []

# Test Case 5: Array with negative numbers
n = 4
nums = [-1, -2, -3, -4]
print(reverseArray(n, nums))  # Expected Output: [-4, -3, -2, -1]

# Test Case 6: Array with mixed positive and negative numbers
n = 6
nums = [-5, 10, 15, -20, 25, -30]
print(reverseArray(n, nums))  # Expected Output: [-30, 25, -20, 15, 10, -5]

# Test Case 7: Array with duplicate values
n = 4
nums = [7, 7, 7, 7]
print(reverseArray(n, nums))  # Expected Output: [7, 7, 7, 7]
