# ２点を直線ベクトルに変換
def zen(xp0,yp0,xp1,yp1,xp2,yp2,xp3,yp3):
	p0p1=[xp1-xp0,yp1-yp0] # 直線p0p1
	p2p3=[xp3-xp2,yp3-yp2] # 直線p2p3
	return p0p1,p2p3
# 直行しているか内席で確認
def zen1(vp0p1,vp2p3):
	return vp0p1[0]*vp2p3[0]+vp0p1[1]*vp2p3[1]==0
# 直行しているか内席で確認
def zen2(vp0p1,vp2p3):
	return vp0p1[0]*vp2p3[1]-vp0p1[1]*vp2p3[0]==0

n=int(input())
for _ in range(n):
	a,b,c,d,e,f,g,h=map(int,input().split())
	p1,p2=zen(a,b,c,d,e,f,g,h)
	# print(p1,p2)
	if zen1(p1,p2):
		print(1)
	elif zen2(p1,p2):
		print(2)
	else:
		print(0)

