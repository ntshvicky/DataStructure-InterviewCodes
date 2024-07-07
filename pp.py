def is_valid_parentheses(s: str):
    '''
    :type s: str - String to be checked for validity
    :rtype: bool - True if the string is valid, False otherwise
    '''
    if len(s) > 104:  # Check if the length exceeds the maximum limit
        return False

    stack = []

    for char in s:
        if char in "({[":
            # If it's an opening bracket, push to the stack
            stack.append(char)
        elif char in ")}]":
            # If it's a closing bracket, check if it matches the last opening bracket
            if not stack:
                return False
            if char == ")" and stack[-1] != "(":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            if char == "]" and stack[-1] != "[":
                return False
            stack.pop()
        else:
            # Invalid character
            return False

    # If the stack is empty, all brackets are properly closed
    return True if not stack else False


if __name__ == '__main__':
    line = input("Enter a string of parentheses: ")
    if is_valid_parentheses(line):
        print("valid")
    else:
        print("invalid")
