def remove_vowels(word, vowels):
    result = ''
    for char in word:
        if char.lower() not in vowels:
            result += char
    return result

# Vowels and word
vowels = ['a', 'e', 'i', 'o', 'u']
word = "PythonProgramming"

# Removing vowels
word_without_vowels = remove_vowels(word, vowels)
print("Word without vowels:", word_without_vowels)  # Output: PythnPrgrmmng
