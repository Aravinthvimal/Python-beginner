word = input()
word = sorted(word)
sorted_word = sorted(word, key=lambda letter: word.count(letter))
print("".join(sorted_word))