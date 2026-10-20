INF = 10**20
n = int(input())
nlist = []
all_mat = []
for i in range(n):
    a,b = map(int, input().split())
    all_mat.append((a,b))
    if (i == 0):
        nlist = [a,b]
    else:
        nlist.append(b)
        
def cost1(nlist):
    if len(nlist) == 0:
        return 0
    m = min(nlist)
    cost = 0
    mid = nlist.index(m)
    a = nlist[:mid]
    b = nlist[mid+1:]
    while (len(a)>1 and len(a) !=0):
        for i in range(len(a)-1):
            cost += a.pop()*a[-1]
            #print(a)
    while (len(b)>1 and len(b) !=0):
        b.reverse()
        for i in range(len(b)-1):
            cost += b.pop()*b[-1]
            #print(b)
    if (len(a) == 1 and len(b) == 1):
        cost += a.pop()*b.pop()
        #print(a,b)
    cost *= m
    return cost
#[34, 44, 13, 30]
def cost2(nlist, mm):
    if len(nlist) == 0:
        return 0
    m = min(nlist)
    cost = 0
    mid = nlist.index(m)
    a = nlist[:mid+1]
    #print(a)
    b = nlist[mid:]
    #print(b)
    while (len(a)>1 and len(a) !=0):
        a.reverse()
        for i in range(len(a)-1):
            cost += a.pop()*a[-1]
            #print(a)
    while (len(b)>1 and len(b) !=0):
        for i in range(len(b)-1):
            cost += b.pop()*b[-1]
            #print(b)
    if (len(a) == 1 and len(b) == 1):
        cost += m*mm
        #print(a,b)
    cost *= mm
    return cost

copy = nlist[:]
m = min(nlist)
#print(nlist)
c = nlist.count(m)
cost = 0
if (c == 1):
    cost = cost1(nlist)
elif (c >= 2):
    cc = 1
    cut_index = [0]
    mcount = nlist.count(m)
    for i in range(mcount):
        cut_index.append(nlist.index(m))
        nlist.remove(m)
    cut = []
    for i in range(mcount):
        cut.append(nlist[cut_index[i]:cut_index[i+1]])
    cut.append(nlist[cut_index[-1]:])
    #print(cut)
    co1 = cut[0] +[m]+ cut[-1]
    cost += cost1(co1)
    for co2 in cut[1:-1]:
        #print(co2)
        cost += cost2(co2,m)
    co3 = cut[0]+cut[-1]
    if (len(co3)>1):
        cost += (len(cut)-2)*m*min(co3)
print(cost)

