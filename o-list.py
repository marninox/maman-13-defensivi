line = 'This line contains words and some have the letter o'
words = line.split()
o_words = []
for word in words:
    if 'o' in word:
        o_words.append(word.upper())
print(', '.join(o_words))