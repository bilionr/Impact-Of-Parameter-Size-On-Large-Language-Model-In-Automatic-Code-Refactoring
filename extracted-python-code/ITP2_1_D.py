A = input().split()
My_list = [[] for _ in range(int(A[0]))]
for _ in range(int(A[1])):
    orders = input().split()
    if orders[0] == '0':
        My_list[int(orders[1])].append(orders[2])
    elif orders[0] == '1':
        print(*My_list[int(orders[1])])
    elif orders[0] == '2':
        My_list[int(orders[1])] = []
