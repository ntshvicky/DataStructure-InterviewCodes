my_tuple = (1, 2, 3, 4, 5)

# Slicing works similarly in tuples as in lists

# reverse the tuple
subtuple = my_tuple[::-1]
print(subtuple)  # Output: (5, 4, 3, 2, 1)

# Read step by 2
subtuple = my_tuple[::2]
print(subtuple)  # Output: (1, 3, 5)

# Read step by 3
subtuple = my_tuple[::3]
print(subtuple)  # Output: (1, 4)