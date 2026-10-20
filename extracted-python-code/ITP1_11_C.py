class Dice:
    def __init__(self, state):
        self.state = state


    def face(self, i):
        return self.state[i]


    def tf_r(self, t, f):
        data = [
        [1, 2, 4, 3, 1],
        [0, 3, 5, 2, 0],
        [0, 1, 5, 4, 0],
        [0, 4, 5, 1, 0],
        [0, 2, 5, 3, 0],
        [1, 3, 4, 2, 1],
        ]
        for i in range(6):
            for j in range(4):
                if self.state[data[i][j]] == t and self.state[data[i][j + 1]] == f:
                    return self.state[i]


    def is_identical_to(self, d):
        try:
            return\
            self.tf_r(self.face(0), self.face(1)) == d.tf_r(self.face(0), self.face(1)) and\
            self.tf_r(self.face(0), self.face(2)) == d.tf_r(self.face(0), self.face(2)) and\
            self.tf_r(self.face(0), self.face(3)) == d.tf_r(self.face(0), self.face(3)) and\
            self.tf_r(self.face(1), self.face(5)) == d.tf_r(self.face(1), self.face(5))
        except:
            return False


def main():
    d1 = Dice([int(s) for s in input().split()])
    d2 = Dice([int(s) for s in input().split()])
    if d1.is_identical_to(d2):
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()

