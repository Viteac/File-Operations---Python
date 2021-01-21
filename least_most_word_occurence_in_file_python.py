
with open('words.txt', 'r') as f:
    read = f.read()
words = read.lower().split()  # load the file with words to count, lowercase them and create a list.

for word in words:   # Strip the words of punctuation
    if word.endswith(',') or word.endswith('.'):
        words[words.index(word)] = word.rstrip(",.")

most_common_item = max(words, key=words.count)
count_word_most = words.count(most_common_item)
print(f'Least common occurs {count_word_most} times: \n {most_common_item}')


least_common_item = min(words, key=words.count)
count_word_least = words.count(least_common_item)
print(f'Least common occurs {count_word_least} time: \n  {least_common_item}')
