def find_all_occurrences(s: str, sub: str) -> list:
    occurrences = []
    start = 0
    while True:
        index = s.find(sub, start)
        if index == -1:
            break
        occurrences.append(index)
        start = index + 1
    return occurrences

# Example usage:
s = "apple"
substring = "p"
indices = find_all_occurrences(s, substring)
print(indices)  # Output: [1, 2]
