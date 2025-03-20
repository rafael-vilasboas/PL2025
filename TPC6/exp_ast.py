class Exp:
    def __init__(self, type, exp1, op, exp2):
        self.type = type
        self.exp1 = exp1
        self.op = op
        self.exp2 = exp2

    def pp(self):
        self.exp1.pp()
        self.op.pp()
        self.exp2.pp()

class Num:
    def __init__(self, type, num):
        self.type = type
        self.num = num

    def pp(self):
        print(self.num, end="")

class Op:
    def __init__(self, type, op):
        self.type = type
        self.op = op

    def pp(self):
        print("", self.op, "", end="")

class Vazio:
    def __init__(self, type):
        self.type = type

    def pp(self):
        print(end="")
