def custom_round(n):
    if n < 0:
        n = abs(n)
        if n < 1:
            return -1 if n >= 0.5 else 0
        else:
            return -5 * round(n / 5)
    elif n < 1:
        return 1 if n >= 0.5 else 0
    else:
        return 5 * round(n / 5)

# Test cases
print(custom_round(0.52))   # Output: 1
print(custom_round(0.49))   # Output: 0
print(custom_round(2.6653)) # Output: 5
print(custom_round(-0.52))  # Output: -1
print(custom_round(-0.49))  # Output: 0
print(custom_round(-2.6653))# Output: -5
