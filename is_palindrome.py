# check if a given string is a palindrome.
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Example usage:
print(is_palindrome("madam"))  # Output: True
print(is_palindrome("hello"))  # Output: False
