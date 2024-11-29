def addOneToNum(arr):
    n = len(arr)

    while n > 1 and arr[0] == 0:
        arr.pop(0)

    carry = 1
    for i in range(n-1, -1, -1):
        arr[i] += 1
        if arr[i] < 10:
            carry = 0
            break
        else:
            arr[i] = 0

    if carry:
        arr.insert(0, carry)

    return arr

arr = [1, 2, 3]
print(addOneToNum(arr))  # Expected Output: [1, 2, 4]

arr = [9]
print(addOneToNum(arr))  # Expected Output: [1, 0]

arr = [9, 9, 9]
print(addOneToNum(arr))  # Expected Output: [1, 0, 0, 0]

arr = [9, 0, 0, 0, 9]
print(addOneToNum(arr))  # Expected Output: [9, 0, 0, 1, 0]

arr = [1, 2, 3, 4]
print(addOneToNum(arr))  # Expected Output: [1, 2, 3, 5]


