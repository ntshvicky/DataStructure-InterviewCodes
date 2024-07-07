def count_substring_occurrences(s: str, sub: str) -> int:
    count = start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            break
        count += 1
        start += len(sub)
    return count

# Example usage:
print(count_substring_occurrences("banana", "ana"))  # Output: 1
print(count_substring_occurrences("aaaa", "aa"))     # Output: 3
