# Print a Rectangle:縦Hと横Wを入力し、＃で長方形を描く
"""
Sample Input
3 4
5 6
2 2
0 0
Sample Output
####
####
####

######
######
######
######
######

##
##
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
        hash_n = "#" * HW_list[i][1]
        print(hash_n)

    if i  < len(HW_list) -1:
        print()

