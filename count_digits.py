def count_digits(n):
    # Handle negative numbers
    n = abs(n)
    
    # Special case for zero
    if n == 0:
        return 1
    
    # Initialize count
    count = 0
    
    # Count digits using division
    while n > 0:
        n //= 10
        count += 1
    
    return count

# Test the function
print(count_digits(12345))  # Output: 5
print(count_digits(-12345)) # Output: 5
print(count_digits(0))      # Output: 1
