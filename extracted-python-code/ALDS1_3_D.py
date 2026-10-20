from collections import deque

def calculate_water_puddles(diagram):
    # 用于记录下降的斜线位置
    down_slopes = deque()
    # 用于存储每个水坑的面积
    puddles = deque()
    
    # 总面积
    total_area = 0
    
    for i, char in enumerate(diagram):
        if char == '\\':
            # 记录下降的位置
            down_slopes.append(i)
        elif char == '/' and down_slopes:
            # 找到一对匹配的斜线
            start = down_slopes.pop()
            area = i - start
            total_area += area
            
            # 合并嵌套的水坑
            while puddles and puddles[-1][0] > start:
                area += puddles.pop()[1]
            
            # 记录当前水坑的起始位置和面积
            puddles.append((start, area))
    
    # 输出总面积和每个水坑的面积
    print(total_area)
    if puddles:
        print(len(puddles), " ".join(str(p[1]) for p in puddles))
    else:
        print(0)

# 输入处理
diagram = input()
calculate_water_puddles(diagram)

