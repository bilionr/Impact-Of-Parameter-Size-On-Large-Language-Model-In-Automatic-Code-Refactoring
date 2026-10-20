str = input()
q = int(input())
for i in range(q):
    cmd = input().split()
    a, b = map(int, cmd[1:3])
    if cmd[0] == "print":
        print(str[a:b+1])
    elif cmd[0] == "reverse":
        str = str[:a] + str[a:b+1][::-1] + str[b+1:]
    elif cmd[0] == "replace":
        str = str[:a] + cmd[3] + str[b+1:]
