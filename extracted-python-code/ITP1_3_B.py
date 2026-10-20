import sys
a = []
for l in sys.stdin:
    if(l != "0\n"):
        a.append(int(l))

for i,l in enumerate(a,start=1):
        print(f'Case {i}: {l}')





    

