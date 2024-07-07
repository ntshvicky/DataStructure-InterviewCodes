#  Python function to count occurrences of a substring within a string without using the count() function.

def count_substring(main_string, substring):
    count = 0
    start_index = 0
    
    # Iterate through the main string
    while True:
        # Find the index of the substring in the main string
        index = main_string.find(substring, start_index)
        
        # If substring is not found, break the loop
        if index == -1:
            break
        
        # Increment count and update start_index for next search
        count += 1
        start_index = index + 1
    
    return count

# Example usage:
s = "banana"
sub = "ana"
occurrences = count_substring(s, sub)
print("Number of occurrences of substring '{}' in the main string: {}".format(sub, occurrences))
