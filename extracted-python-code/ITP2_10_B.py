[a,b] = list(map(int,input().split()))
AND = a&b
print(''.join(list(map(str,f'{AND:032b}'))))
OR = a|b
print(''.join(list(map(str,f'{OR:032b}'))))
XOR = a^b
print(''.join(list(map(str,f'{XOR:032b}'))))

