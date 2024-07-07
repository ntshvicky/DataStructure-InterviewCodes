def count_vowels(word, vowels):
    count = 0
    for char in word.lower():  # Convert to lowercase to handle both cases
        if char in vowels:
            count += 1
    return count

# Vowels and word
vowels = ['a', 'e', 'i', 'o', 'u']
word = "PythonProgramming"

# Counting vowels
vowel_count = count_vowels(word, vowels)
print("Number of vowels:", vowel_count)  # Output: Number of vowels: 4
