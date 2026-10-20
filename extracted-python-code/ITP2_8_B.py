from sys import stdout, stdin

read = stdin.readlines()
write = stdout.write

q = int(read[0])

dictionary = dict()
output = ""

for input_line in read[1:]:
    operation, *args = input_line.split()
    if operation == "0":
        key, x = args[0], args[1]
        dictionary[key] = x
    elif operation == "1":
        key = args[0]
        # output += f'{dictionary.setdefault(key, "0")}\n'
        output += f'{dictionary.get(key, "0")}\n'
    elif operation == "2":
        key = args[0]
        dictionary[key] = "0"

write(output)

