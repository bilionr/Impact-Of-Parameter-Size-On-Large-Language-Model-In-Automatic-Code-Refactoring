import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    q = int(input_data[0])
    s = set()
    
    results = []
    pointer = 1
    for _ in range(q):
        query_type = input_data[pointer]
        x = input_data[pointer + 1]
        
        if query_type == '0':
            s.add(x)
            results.append(str(len(s)))
        else:
            if x in s:
                results.append("1")
            else:
                results.append("0")
        pointer += 2

    sys.stdout.write("\n".join(results) + "\n")

solve()
