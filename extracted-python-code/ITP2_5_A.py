import sys

def main():
    input = sys.stdin.readline
    n = int(input())
    
    points = [tuple(map(int, input().split())) for _ in range(n)]
    
    points.sort()
    
    out = []
    for x, y in points:
        out.append(f"{x} {y}")
    sys.stdout.write("\n".join(out) + "\n")

if __name__ == "__main__":
    main()

