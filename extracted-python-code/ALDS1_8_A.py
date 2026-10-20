import sys

#この部分は Node というクラスを定義しています。Node は二分探索木の各ノードを表すための設計図のようなものです。
class Node():
  #__slots__ = ['key', 'left', 'right']: メモリ効率を向上させるために、各ノードが持つ属性を key, left, right のみに制限しています。
    __slots__ = ['key', 'left', 'right']
    #__init__(self, key): Node オブジェクトが作成されるときに呼ばれるコンストラクタです。新しいノードの key を設定し、左右の子ノードを None (何もない) に初期化します。
    def __init__(self, key):
        self.key = key
        self.left, self.right = None, None
    #__str__(self): ノードを表示する際に、key の値を文字列として返すように定義しています。   
    def __str__(self):
        return self.key

#root は二分探索木の根 (root) ノードを指す変数です。最初は木が空なので None に設定されています。
root = None
#この関数は、新しいキー z を持つノードを二分探索木に挿入します。
#global root: 関数内で root 変数を変更するため、global キーワードでグローバル変数として扱うことを宣言しています
def insert(z):
    global root
    #x, y = root, None: x は挿入位置を探すための現在ノード、y は x の親ノードを保持します。
    x, y = root, None
    #x が None になるまで（つまり、挿入位置が見つかるまで）ループします。
    #。ループ内で、zの値と現在のノードxのkeyを比較し、zがx.keyより小さければ左の子ノードへ、大きければ右の子ノードへと移動します。
    while x:
      #y に現在の x を保存し、z の値と x.key を比較して左の子ノード(x.left)または右の子ノード(x.right)に移動します
        y = x
        if z < x.key:
            x = x.left
        else:
            x = x.right
    
    #y == None: 木が空の場合、root に新しいノードを作成します。
    if y == None:
        root = Node(z)
    #z < y.key: y の左の子ノードとして新しいノードを挿入します。
    elif z < y.key:
        y.left = Node(z)
    #それ以外: y の右の子ノードとして新しいノードを挿入します。
    else:
        y.right = Node(z)

#現在のノード (x) -> 左部分木 -> 右部分木の順に処理します。
def preorder(x):
    return f" {x.key}" + preorder(x.left) + preorder(x.right) if x else ""

#左部分木 -> 現在のノード (x) -> 右部分木の順に処理します。
def inorder(x):
    return inorder(x.left) + f" {x.key}" + inorder(x.right) if x else ""

#input(): 入力の最初の行を読み飛ばします (この行は使われないようです)。     
input()
#node = {}: この変数は宣言されていますが、コード内で使用されていません。
node = {}
#for s in sys.stdin:: 標準入力から1行ずつ読み込みます。
for s in sys.stdin:
  #if s[0] == "p": 行の先頭が "p" の場合、inorder と preorder を使って木を出力します。
    if s[0] == "p":
        pass
        print(inorder(root))
        print(preorder(root))
    #それ以外: 行の7文字目以降を整数に変換し、insert 関数を使って木に挿入します。これは入力形式が "insert 10" のような形だと想定しているためです。
    else:
        insert(int(s[7:]))

