#4棟3階建て、各階に10部屋をもつ大学の校舎がある
#入居者・退去者(v)の情報がn回入力される
#入力情報は、棟番号(b)、階数(f)、部屋番号(r),入居者・退去者(v)である
#入力後の滞在者数の情報を視覚化せよ
n=int(input())
#滞在者情報を初期化　A~D棟を0~3に番号付け
L=[[[0 for i in range(10)] for j in range(3)] for k in range(4)]
for _ in range(n):
    b,f,r,v=map(int,input().split())
    L[b-1][f-1][r-1]+=v
for i in range(4):
    for j in range(3):
        print(' ',end='')
        print(' '.join(map(str,L[i][j])))
    if not i==3:
        print('####################')
