def checkBalanceParenthesis(s):
    stack = []
    for item in s:
        if item in ")}]":
            if not stack:  # Ensure stack isn't empty before popping
                return False
            top = stack.pop()  # Pop the last opening parenthesis
            if (item == ')' and top != '(') or \
                    (item == '}' and top != '{') or \
                    (item == ']' and top != '['):  # Check for mismatched pairs
                return False
        elif item in "({[":
            stack.append(item)
        else:
            return False  # Invalid character

    return not stack  # Return True if stack is empty, else False


# Test cases
if __name__ == "__main__":
    # Balanced parenthesis
    print(checkBalanceParenthesis("()"))  # Expected: True
    print(checkBalanceParenthesis("()[]{}"))  # Expected: True
    print(checkBalanceParenthesis("{[()]}"))  # Expected: True

    # Unbalanced parenthesis
    print(checkBalanceParenthesis("(]"))  # Expected: False
    print(checkBalanceParenthesis("([)]"))  # Expected: False
    print(checkBalanceParenthesis("{[}"))  # Expected: False

    # Edge cases
    print(checkBalanceParenthesis(""))  # Expected: True (Empty string is balanced)
    print(checkBalanceParenthesis("["))  # Expected: False
    print(checkBalanceParenthesis("]"))  # Expected: False
    print(checkBalanceParenthesis("{[()"))  # Expected: False
    print(checkBalanceParenthesis("{[()]"))  # Expected: False

    # Mixed valid and invalid characters
    print(checkBalanceParenthesis("{[a+b]*(c+d)}"))  # Expected: False (Invalid characters)
    print(checkBalanceParenthesis("{[]}"))  # Expected: True
