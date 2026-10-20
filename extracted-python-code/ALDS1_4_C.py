def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    n = int(data[0])  # 命令の数
    commands = data[1:]  # 命令リスト

    dictionary = set()  # 辞書としての集合

    result = []
    for command in commands:
        op, string = command.split()  # 操作と文字列に分割
        if op == "insert":
            dictionary.add(string)  # 文字列を辞書に追加
        elif op == "find":
            # 文字列が辞書に存在するか確認
            result.append("yes" if string in dictionary else "no")
    
    # 結果を出力
    print("\n".join(result))

if __name__ == "__main__":
    main()

