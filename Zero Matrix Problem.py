def zeroMatrix(arr: list[list[int]]) -> list[list[int]]:
    n = len(arr)
    m = len(arr[0])
    row = [0] * n
    column = [0] * m

    for i in range(0, n):
        for j in range(0, m):
            if arr[i][j] == 0:
                row[i], column[j] = 1, 1

    for i in range(0, n):
        for j in range(0, m):
            if row[i] == 1 or column[j] == 1:
                arr[i][j] = 0

    return arr

def test_zeroMatrix():
    # Test case 1: Matrix with multiple zeros
    arr = [
        [1, 2, 3],
        [4, 0, 6],
        [7, 8, 0]
    ]
    expected = [
        [1, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    assert zeroMatrix(arr) == expected, "Test case 1 failed"

    # Test case 2: Matrix with no zeros
    arr = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert zeroMatrix(arr) == expected, "Test case 2 failed"

    # Test case 3: Matrix with all zeros
    arr = [
        [0, 0],
        [0, 0]
    ]
    expected = [
        [0, 0],
        [0, 0]
    ]
    assert zeroMatrix(arr) == expected, "Test case 3 failed"

    # Test case 4: Matrix with one row
    arr = [
        [1, 0, 3]
    ]
    expected = [
        [0, 0, 0]
    ]
    assert zeroMatrix(arr) == expected, "Test case 4 failed"

    # Test case 5: Matrix with one column
    arr = [
        [1],
        [0],
        [3]
    ]
    expected = [
        [0],
        [0],
        [0]
    ]
    assert zeroMatrix(arr) == expected, "Test case 5 failed"

    # Test case 6: Matrix with a single element (zero)
    arr = [[0]]
    expected = [[0]]
    assert zeroMatrix(arr) == expected, "Test case 6 failed"

    # Test case 7: Matrix with a single element (non-zero)
    arr = [[5]]
    expected = [[5]]
    assert zeroMatrix(arr) == expected, "Test case 7 failed"

    print("All test cases passed!")

test_zeroMatrix()
