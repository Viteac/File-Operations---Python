this = 'words.txt'
with open(this) as f:
    file = f.read().split()


file = list(set(file))

for i, v in enumerate(file):
    if v.endswith('.'):
        u = v.rstrip('.')
        file.pop(i)
    elif v.endswith(','):
        u = v.rstrip(',')
        file.pop(i)

        file.insert(i, u)

print('-' * 20)
print(file)
print('-' * 20)


c = 0
longest = set()
for e in file:
    long = len(e)
    if long > c:
        c = long
        longest.clear()
        longest.add(e)
    elif long == c:
        longest.add(e)

g = ','.join(longest)


if len(longest) < 2:
    print(f'The longest word in a File: {this} is : {g} with {c} characters')
else:
    print(f'The longest words in a File: {this} are: {g} with {c} characters')
