import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        print(0)
        return
        
    n = int(data[0])
    activities = []
    index = 1
    for i in range(n):
        s = int(data[index])
        t = int(data[index+1])
        index += 2
        activities.append((s, t))
        
    activities.sort(key=lambda x: x[1])
    
    count = 0
    last_end = -1
    
    for s, t in activities:
        if s > last_end:
            count += 1
            last_end = t
            
    print(count)

if __name__ == "__main__":
    main()
