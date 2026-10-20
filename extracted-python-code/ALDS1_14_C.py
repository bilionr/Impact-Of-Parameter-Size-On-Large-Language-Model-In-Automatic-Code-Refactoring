import sys
class KMP2D:
    def __init__(self, pattern, R):
        self.pattern_l = R
        self.table = [0] * (self.pattern_l + 1)
        self.table[0] = -1
        c = 0
        for k in range(1, self.pattern_l):
            if pattern[k] == pattern[c]:
                self.table[k] = self.table[c]
            else:
                self.table[k] = c
                c = self.table[c]
                while c >= 0 and pattern[k] != pattern[c]:
                    c = self.table[c]
            c += 1
        self.table[self.pattern_l] = c
        self.pattern = pattern

    def match(self, target, target_height, target_width, pattern_width):
        rec = []
        for k in range(target_width - pattern_width + 1):
            i = j = 0
            while i < target_height:
                if target[i][k:k + pattern_width] == self.pattern[j]:
                    i += 1
                    j += 1
                    if j == self.pattern_l:
                        rec.append((i - j, k))
                        j = self.table[j]
                else:
                    j = self.table[j]
                    if j < 0:
                        i += 1
                        j += 1
        return rec

# 读取输入
H, W = map(int, sys.stdin.readline().split())
TM = [sys.stdin.readline().rstrip() for _ in range(H)]
R, C = map(int, sys.stdin.readline().split())
PM = [sys.stdin.readline().rstrip() for _ in range(R)]

# 创建 KMP2D 对象并进行匹配
kmp = KMP2D(PM, R)
rec = kmp.match(TM, H, W, C)

# 排序并输出结果
rec.sort()
for item in rec:
    print(*item)
