class Huffman_Tree:
    def __init__(self, left_child, right_child, value):
        self.value = value
        self.left_child = left_child
        self.right_child = right_child

class Huffman_Leaf:
    def __init__(self, letter, value):
        self.value = value
        self.letter = letter

def generate_huffman_tree(huffman_leaf_list):
    huffman_leaf_list.sort(key=lambda leaf:leaf.value, reverse=True)
    # print(huffman_leaf_list)
    while len(huffman_leaf_list) > 1:
        left_child = huffman_leaf_list.pop()
        right_child = huffman_leaf_list.pop()
        new_tree_value = left_child.value + right_child.value
        new_tree = Huffman_Tree(left_child, right_child, new_tree_value)
        huffman_leaf_list.append(new_tree)
        huffman_leaf_list.sort(key=lambda leaf:leaf.value, reverse=True)
    return huffman_leaf_list[0]

def generate_huffman_code(huffman_tree, huffman_code, string):
    if type(huffman_tree) is Huffman_Leaf:
        leaf = huffman_tree
        huffman_code[leaf.letter] = string
        return huffman_code 
    else:
        huffman_code = generate_huffman_code(huffman_tree.left_child, huffman_code, string+"0")
        return generate_huffman_code(huffman_tree.right_child, huffman_code, string+"1")



def main():
    string = str(input())
    # string = 45*"a"+"b"*13+12*"c"+16*"d"+"e"*9+"f"*5
    # 文字とその出現回数をまとめる & huffman_codeの準備
    letter_count = {}
    huffman_code = {} # letter -> length
    for letter in string:
        huffman_code[letter] = 0
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    # huffman leafのリストを作成&
    huffman_leaf_list = []
    for letter, count in letter_count.items():
        new_leaf = Huffman_Leaf(letter,count)
        huffman_leaf_list.append(new_leaf)

    huffman_tree = generate_huffman_tree(huffman_leaf_list)
    # huffman_code[*] = 0
    if len(huffman_code) != 1:
        huffman_code = generate_huffman_code(huffman_tree, huffman_code, "")
    else:
        for letter, _ in huffman_code.items():
            huffman_code[letter] = "0"

  
    # print(huffman_code)
    # 答えを生成
    ans = 0
    for letter, count in letter_count.items():
        ans += count * len(huffman_code[letter])

    print(ans)

if __name__=="__main__":
    main()
