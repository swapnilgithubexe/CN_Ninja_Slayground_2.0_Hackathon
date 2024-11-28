def twoSum(arr, target):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    for num in arr:
        complement = target - num
        if complement == num and freq[num] > 1:
            return True
        elif complement != num and complement in freq:
            return True
    return False

print(twoSum([1, 2, 3, 4, 5], 6))  # True -> (1 + 5) or (2 + 4)
print(twoSum([1, 2, 3, 4, 5], 10)) # False -> No such pair exists
print(twoSum([1, 1, 2, 3], 2))     # True -> (1 + 1)
print(twoSum([5, 5, 5, 5], 10))    # True -> (5 + 5)
print(twoSum([1], 2))              # False -> Only one element, no pair
print(twoSum([0, 0, 3, 4], 0))     # True -> (0 + 0)
print(twoSum([-3, 4, 1, 2], 1))    # True -> (-3 + 4)
print(twoSum([], 5))               # False -> Empty array
print(twoSum([1, 2, 3], 5))        # True -> (2 + 3)
print(twoSum([1, 2, 3], 7))        # False -> No such pair exists