n=int(input()) #持っているトランプの枚数
cards=[] #持ってるトランプの組み合わせ
t=0
#スペードの1~13は1~13,ハートは14~26,クローバーは27~39,ダイヤは40~52
#という風に各カードに番号付けする
for _ in range(n):
    Mrk,Num=map(str,input().split()) #Mrkはトランプのマーク,Numは数字
    Num=int(Num)
    if Mrk=='S': #マークがスペードの時
        t=Num
    elif Mrk=='H':
        t=13+Num
    elif Mrk=='C':
        t=26+Num
    elif Mrk=='D':
        t=39+Num
    cards.append(t)
for i in range(1,53):
    if not(i in cards):
        if i<14:
            print('S',i)
        elif i<27:
            print('H',i-13)
        elif i<40:
            print('C',i-26)
        else:
            print('D',i-39)
