import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    m = {}
    
    results = []
    pointer = 1
    for _ in range(q):
        query_type = input_data[pointer]
        
        if query_type == '0':
            # 挿入
            key = input_data[pointer + 1]
            x = input_data[pointer + 2]
            m[key] = x
            pointer += 3
        else:
            key = input_data[pointer + 1]
            results.append(m[key])
            pointer += 2
            
    sys.stdout.write("\n".join(results) + "\n")

solve()
