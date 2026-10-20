w=input().lower()
count=0

while True:
    s= input()
    if s == "END_OF_TEXT":
        break
    p=s.lower()
    b=p.split()
    for ti in b:
        if ti == w:
            count+=1

print(count)
