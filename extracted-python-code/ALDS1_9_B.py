#これはPythonの標準ライブラリであるheapqモジュールからheapifyという関数をインポートしています。heapifyはリストをヒープ構造（特定の順序で並べられた木構造）に変換します。ヒープは、特に最小値や最大値を効率的に取り出すためのデータ構造です。
from heapq import heapify
#map(lambda x: -int(x), ...)：リスト内の各要素を整数に変換し、それを負の数に変換しています。lambdaは無名関数を定義する方法で、ここではx（入力された各値）をintで整数に変換し、-をつけて負にしています。
#list(...)：上記のmapオブジェクトをリストに変換します。
input()
a = list(map(lambda x: -int(x), input().split()))
#この行は、リストaを「ヒープ構造」に変換します。heapqを使うと、リスト内の要素がヒープの性質（部分木のルートがその部分木内の最小値）を満たすように並び替えられます。
heapify(a)
print("", *list(map(lambda x: -x, a)))

