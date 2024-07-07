def generate_substrings(s: str):
    substrings = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            substrings.append(s[i:j])
    return substrings

# Example usage:
substrings = generate_substrings("abcabcbb")
for substring in substrings:
    print(substring)


'''
Outpput - 
a
ab
abc
abca
abcab
abcabc
abcabcb
abcabcbb
b
bc
bca
bcab
bcabc
bcabcb
bcabcbb
c
ca
cab
cabc
cabcb
cabcbb
a
ab
abc
abcb
abcbb
b
bc
bcb
bcbb
c
cb
cbb
b
bb
b

'''