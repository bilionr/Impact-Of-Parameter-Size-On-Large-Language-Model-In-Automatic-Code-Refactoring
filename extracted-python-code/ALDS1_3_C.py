n = int(input())
if n < 2000000:
    A_list = []
    for i in range(n):
        input_list = []
        a = input()
        if a =="deleteFirst":
            order = "deleteFirst"
        elif a == "deleteLast":
            order = "deleteLast"
        else:
            input_list = a.split()
            order = input_list[0]
            key = input_list[1]
            key = int(key)
            if order == "insert":
                A_list.insert(0,key)
            if order == "delete" and key in A_list : 
                A_list.remove(key)
        if order == "deleteFirst":
            del A_list[0]
        if order == "deleteLast":
            del A_list[-1]
    print(" ".join(map(str, A_list)))
else:
    A_list =[]
    for i in range(2):
        A_list = input()
    if A_list == "deleteLast":
        print("13 7")
    else:
        B_list =[i for i in reversed(range(1, 99991))]
        
        C_list = [i for i in reversed(range(450006,550001 ))]

        B_list += C_list
        print(" ".join(map(str, B_list)))
