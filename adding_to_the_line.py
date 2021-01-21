file = 'kaczka.txt'
new_file = 'kaczka3.txt'

with open(file) as f:  # Open the file to read
    read = f.readlines()

count = 0  # Counter that will be used for counting lines

for line in read:  # For loop to iterate over the lines
    if not line == '\n':   # If line has a new line "\n" skip the line
        line = line.strip('\n')  # Were striping the element of new line character "\n"
        count += 1  # Counter indecent about 1
        read[count] = f'{line}:{count}'  # add new element to the line
        k = read[count]
        print(read[count])
        with open(new_file, 'a') as f:  # Add element to the new line in new file
            f.write(f'{k}\n')

print(f' Content of {file} is written in {new_file}')






