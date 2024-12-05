def printSpiralMatrix(arr: list[list[int]]) -> list[int]:
    if not arr or not arr and not arr[0]:
        return []

    n, m = len(arr), len(arr[0])
    top, left, down, right = 0, 0, n-1, m-1
    ans = []

    direction = 0

    while top <= down and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                ans.append(arr[top][i])

            top += 1

        elif direction == 1:
            for i in range(top, down + 1):
                ans.append(arr[i][right])

            right -= 1

        elif direction == 2:
            for i in range(right, left - 1, -1):
                ans.append(arr[down][i])

            down -= 1

        elif direction == 3:
            for i in range(down, top - 1, -1):
                ans.append(arr[i][left])

            left += 1

        direction = (direction + 1) % 4

    return ans

if __name__ == "__main__":
    # Test case 1: Square matrix
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(printSpiralMatrix(matrix1))  # Expected: [1, 2, 3, 6, 9, 8, 7, 4, 5]

    # Test case 2: Rectangular matrix (more columns than rows)
    matrix2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8]
    ]
    print(printSpiralMatrix(matrix2))  # Expected: [1, 2, 3, 4, 8, 7, 6, 5]

    # Test case 3: Rectangular matrix (more rows than columns)
    matrix3 = [
        [1, 2],
        [3, 4],
        [5, 6]
    ]
    print(printSpiralMatrix(matrix3))  # Expected: [1, 2, 4, 6, 5, 3]

    # Test case 4: Single row
    matrix4 = [
        [1, 2, 3, 4]
    ]
    print(printSpiralMatrix(matrix4))  # Expected: [1, 2, 3, 4]

    # Test case 5: Single column
    matrix5 = [
        [1],
        [2],
        [3],
        [4]
    ]
    print(printSpiralMatrix(matrix5))  # Expected: [1, 2, 3, 4]

    # Test case 6: Single element
    matrix6 = [
        [1]
    ]
    print(printSpiralMatrix(matrix6))  # Expected: [1]

    # Test case 7: Empty matrix
    matrix7 = []
    print(printSpiralMatrix(matrix7))  # Expected: []

    # Test case 8: Non-square matrix
    matrix8 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
    print(printSpiralMatrix(matrix8))  # Expected: [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]

    # Test case 9: Larger matrix
    matrix9 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print(printSpiralMatrix(matrix9))  # Expected: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
