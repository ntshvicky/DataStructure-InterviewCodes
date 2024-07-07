def replace_vowels(word, vowels, replacement_char):
    result = ''
    for char in word:
        if char.lower() in vowels:
            result += replacement_char
        else:
            result += char
    return result

# Vowels and word
vowels = ['a', 'e', 'i', 'o', 'u']
word = "PythonProgramming"

# Replacing vowels
replaced_word = replace_vowels(word, vowels, '*')
print("Word with vowels replaced:", replaced_word)  # Output: Pyth*nPr*gr*mm*ng
