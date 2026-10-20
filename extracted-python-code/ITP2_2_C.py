import sys
import heapq

lines = sys.stdin.readlines()
n, q = map(int, lines[0].split())

queues = {str(i): [] for i in range(n)}
for i in range(n):
    heapq.heapify(queues[str(i)])

for line in lines[1:]:
    lo = line.split()
    if lo[0] == '0':
        heapq.heappush(queues[lo[1]], -int(lo[2]))
    elif lo[0] == '1':
        if len(queues[lo[1]]) > 0:
            print(-queues[lo[1]][0])
    else:
        if len(queues[lo[1]]) > 0:
            heapq.heappop(queues[lo[1]])


