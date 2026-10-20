import sys
input=sys.stdin.readline
write=sys.stdout.write

class TreapNode:
    __slots__ = ('key','pri','left','right')
    def __init__(self,key:int,pri:int):
        self.key = key
        self.pri = pri
        self.left = None
        self.right = None

def right_rotate(t:TreapNode) -> TreapNode:
    s = t.left
    t.left = s.right 
    s.right = t 
    return s 

def left_rotate(t:TreapNode) -> TreapNode:
    s = t.right
    t.right = s.left 
    s.left = t 
    return s         

def insert(t : TreapNode,key:int,pri:int) -> TreapNode:
    if t is None:
        return TreapNode(key,pri)
    if key < t.key:
        t.left = insert(t.left,key,pri)
        if t.left.pri > t.pri:
            t = right_rotate(t)
    elif key > t.key:
        t.right = insert(t.right,key,pri)
        if t.right.pri >t.pri:
            t = left_rotate(t)
    return t 

def find(t : TreapNode,key:int) -> bool:
    while t:
        if key == t.key:
            return True
        t= t.left if key < t.key else t.right
    return False        

def delate(t:TreapNode,key:int) -> TreapNode:
    if t is None:
        return None
    if key < t.key:
        t.left = delate(t.left,key)
    elif key > t.key:
        t.right = delate(t.right,key)
    else:
        if t.left is None:
            return t.right
        if t.right is None:
            return t.left
        if t.left.pri < t.right.pri:    
            t = left_rotate(t)
        else: 
            t = right_rotate(t)    
        t = delate(t,key)
    return t

def inorder(t: TreapNode,res:list):
    if not t:return
    inorder(t.left,res)
    res.append(t.key)
    inorder(t.right,res)

def preorder(t: TreapNode,res:list):
    if not t:return
    res.append(t.key)
    preorder(t.left,res)
    preorder(t.right,res)    

def main():
    m = int(input())
    root = None

    out = []
    for _ in range(m):
        cmd = input().split()
        if cmd[0] == 'insert':
            k = int(cmd[1])
            p = int(cmd[2])
            root = insert(root,k,p)
        elif cmd[0] == 'find':
            k = int(cmd[1])
            out.append('yes' if find(root,k) else 'no')
        elif cmd[0] == 'delete':
            k = int(cmd[1])
            root = delate(root,k)
        elif cmd[0] == 'print':
            a = []            
            b = []
            inorder(root,a)
            preorder(root,b)
            out.append(''.join(f' {x}' for x in a))
            out.append(''.join(f' {x}' for x in b))

    for line in out:
        write(line + '\n') 

if __name__== "__main__":
    main()        
