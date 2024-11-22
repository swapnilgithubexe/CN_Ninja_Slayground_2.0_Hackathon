from typing import List
import math

def areaSwitchCase(ch: int, a: List[float]) -> str:
    ans = 0
    if ch == 1:  # Area of a circle
        ans = math.pi * (a[0] ** 2)
    elif ch == 2:  # Area of a rectangle
        ans = a[0] * a[1]

    rounded_ans = "{:.5f}".format(ans)
    return rounded_ans

# Test cases
def test_areaSwitchCase():
    test_cases = [
        (1, [3], "28.27433"),       # Circle with radius 3
        (1, [7], "153.93804"),      # Circle with radius 7
        (1, [0], "0.00000"),        # Circle with radius 0
        (2, [5, 3], "15.00000"),    # Rectangle with length 5 and width 3
        (2, [2.5, 4.2], "10.50000"),# Rectangle with length 2.5 and width 4.2
        (2, [0, 10], "0.00000")     # Rectangle with one side as 0
    ]

    for i, (ch, a, expected) in enumerate(test_cases):
        result = areaSwitchCase(ch, a)
        assert result == expected, f"Test case {i + 1} failed: {result} != {expected}"
        print(f"Test case {i + 1} passed: {result} == {expected}")

# Run tests
test_areaSwitchCase()
