import sys

def main():
    input = sys.stdin.readline
    write = sys.stdout.write

    line = input()
    if not line:
        return
    n = int(line)
    
    max_mask = 1 << n
    for d in range(max_mask):
        elems = []
        x = d
        while x:
            lsb = x & -x
            pos = lsb.bit_length() - 1
            elems.append(str(pos))
            x ^= lsb
        
        if elems:
            write(f"{d}: {' '.join(elems)}\n")
        else:
            write(f"{d}:\n")

if __name__ == "__main__":
    main()

