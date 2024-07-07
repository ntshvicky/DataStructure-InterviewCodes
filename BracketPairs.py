# Given a string containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid. An input string is valid if:
'''
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Example:
s = "()" should return True
s = "()[]{}" should return True
s = "(]" should return False
s = "([)]" should return False
s = "{[]}" should return True
'''

def is_valid(s):
    # Dictionary to keep track of matching pairs
    matching_bracket = {')': '(', '}': '{', ']': '['}
    stack = []

    for char in s:
        if char in matching_bracket.values():
            # If the character is an opening bracket, push it onto the stack
            stack.append(char)
        elif char in matching_bracket.keys():
            # If the character is a closing bracket
            if stack == [] or matching_bracket[char] != stack.pop():
                return False
        else:
            # Invalid character
            return False

    return stack == []

# Example usage:
print(is_valid("()"))      # True
print(is_valid("()[]{}"))  # True
print(is_valid("(]"))      # False
print(is_valid("([)]"))    # False
print(is_valid("{[]}"))    # True
