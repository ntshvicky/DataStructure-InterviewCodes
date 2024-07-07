# Given a string, find the length of the longest substring without repeating characters.
s = "abcabcbb"

def length_of_longest_substring(s):
    char_index = {}
    left = 0
    max_length = 0
    
    for right, char in enumerate(s):
        if char in char_index and char_index[char] >= left:
            left = char_index[char] + 1
        char_index[char] = right
        max_length = max(max_length, right - left + 1)
    
    return max_length

result = length_of_longest_substring(s)
print(result)  # Output: 3
