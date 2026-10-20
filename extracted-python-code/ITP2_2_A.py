import sys

def main():
    input = sys.stdin.readline
    n, q = map(int, input().split())
    
    stacks = [[] for _ in range(n)]
    out_lines = []
    
    for _ in range(q):
        parts = input().split()
        cmd = parts[0]
        t = int(parts[1])
        
        if cmd == '0':
            x = int(parts[2])
            stacks[t].append(x)
        elif cmd == '1':
            if stacks[t]:
                out_lines.append(str(stacks[t][-1]))
        else:
            if stacks[t]:
                stacks[t].pop()
    
    sys.stdout.write('\n'.join(out_lines) + '\n')

if __name__ == "__main__":
    main()

