q = int(input())
xy_list = [list(map(int,input().split())) for i in range(q)]

for i in range (len(xy_list)):
    a_1 = xy_list[i][1] - xy_list[i][3]
    a_2 = xy_list[i][5] - xy_list[i][7]
    b_1 = xy_list[i][2] - xy_list[i][0]
    b_2 = xy_list[i][6] - xy_list[i][4]
    c_1 = xy_list[i][0] * (xy_list[i][3] - xy_list[i][1]) - xy_list[i][1] * (xy_list[i][2] - xy_list[i][0])
    c_2 = xy_list[i][4] * (xy_list[i][7] - xy_list[i][5]) - xy_list[i][5] * (xy_list[i][6] - xy_list[i][4])
    
    
    x = (c_2 * b_1 - c_1 * b_2)/(a_1 * b_2 -a_2 * b_1)
    y = (c_2 * a_1 - c_1 * a_2)/(b_1 * a_2 -b_2 * a_1)
    print(x,y)
