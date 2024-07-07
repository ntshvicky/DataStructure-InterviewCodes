

def first_non_repeating_char(s: str) -> str:
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    
    for char in s:
        if char_count[char] == 1:
            return char
    return None

# Example usage:
print(first_non_repeating_char("swiss"))  # Output: "w"
print(first_non_repeating_char("aabb"))   # Output: None
