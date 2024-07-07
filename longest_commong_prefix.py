'''
Problem Statement: Given a set of strings, find the longest common prefix.Examples:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
def longest_common_prefix(strs):
    if not strs:
        return ""

    common_prefix = strs[0]
    
    for string in strs[1:]:
        while string[:len(common_prefix)] != common_prefix:
            common_prefix = common_prefix[:-1]
            if not common_prefix:
                return ""
    
    return common_prefix

# better O(n * m)
def longest_common_prefix_using_zip(strs):
    if not strs:
        return ""

    # Using zip to iterate through characters of each string simultaneously
    for i, chars in enumerate(zip(*strs)):
        if len(set(chars)) > 1:
            return strs[0][:i]
    
    # If all strings have been traversed without returning, the entire first string is the common prefix
    return min(strs)

# Test cases
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]

print(longest_common_prefix(strs1))  # Output: "fl"
print(longest_common_prefix(strs2))  # Output: ""
