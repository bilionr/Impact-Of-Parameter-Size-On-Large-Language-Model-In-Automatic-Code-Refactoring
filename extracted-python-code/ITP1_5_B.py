# Print a Frame
"""
以下のような、たてH cm よこ W cm の枠を描くプログラムを作成して下さい。

Sample Input
3 4
5 6
3 3
0 0
Sample Output
####
#..#
####

######
#....#
#....#
#....#
######

###
#.#
###
"""
HW_list = []
while True:
    H, W = (int(x) for x in input().split())
    HW_list.append([H, W])

    if HW_list[-1] == [0, 0]:
        HW_list[-1].pop()
        break

for i in range(len(HW_list)):
    for j in range(HW_list[i][0]):
        if j == 0 or j == (HW_list[i][0] - 1):
            hash_n = "#" * HW_list[i][1]
        else:
            hash_n = "#" + "." * (HW_list[i][1] -2) + "#"
        
        print(hash_n)

    if i  < len(HW_list) -1:
        print()
