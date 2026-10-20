import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    a = []
    
    current = 1
    results = []
    
    for _ in range(q):
        query_type = input_data[current]
        
        if query_type == '0':
            x = input_data[current + 1]
            a.append(x)
            current += 2
        elif query_type == '1':
            p = int(input_data[current + 1])
            results.append(a[p])
            current += 2
        elif query_type == '2':
            a.pop()
            current += 1
            
    sys.stdout.write('\n'.join(results) + '\n')

solve()
