stack=[]
for a in input().split(' '):
    if a.isdigit():
        stack.append(int(a))
    else:
        stack.append(eval(str(stack.pop(-2))+a+str(stack.pop(-1))))

print(stack[0])
