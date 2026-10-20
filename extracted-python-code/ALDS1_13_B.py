adjacent = (
    (1, 3),       # 0
    (0, 2, 4),    # 1
    (1, 5),       # 2
    (0, 4, 6),    # 3
    (1, 3, 5, 7), # 4
    (2, 4, 8),    # 5
    (3, 7),       # 6
    (4, 6, 8),    # 7
    (5, 7)        # 8
)

GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]

# Bidirectional search using breadth-first search
def solve(start):
    if start == GOAL:
        return 0
    # 0: forward, 1: backward
    generated_state = {tuple(start): 0, tuple(GOAL): 1}
    step = {tuple(start): 0, tuple(GOAL): 0}
    s = 0
    state1 = [(start, 0), (GOAL, 1)]
    while state1:
        state2 = state1[:]
        state1 = []
        s += 1
        for s2, d in state2:
            i = s2.index(0)
            for p in adjacent[i]:
                s1 = s2[:]
                s1[i], s1[p] = s1[p], 0
                key = tuple(s1)
                if key in generated_state:
                    if generated_state[key] != d:
                        return s + step[key]
                    continue
                state1.append((s1, d))
                generated_state[key] = d
                step[key] = s

import sys

start = list(map(int, sys.stdin.read().split()))

print(solve(start))

