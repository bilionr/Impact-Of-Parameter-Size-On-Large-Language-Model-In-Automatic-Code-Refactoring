alf = [0] * 26

while True:
    try:
        str = input().lower()
    except:
        break
    for i in str:
        if 'a' <= i and i <= 'z':
            alf[ord(i) - ord('a')] += 1
    
for i in range(26):
    print(chr(ord('a') + i), ':', alf[i])
