class A:
    def printA(self):
        print("A")

class B:
    def printB(self):
        print("B")

class C:
    def printC(self):
        print("C")

class D(A, B, C):
    def printD(self):
        print("D")

    def printAll(self):
        self.printA()
        self.printB()
        self.printC()
        self.printD()

obj = D()   # クラスDのインスタンスを作成
obj.printA()    # クラスAのprintA()メソッドを実行
obj.printB()    # クラスBのprintA()メソッドを実行
obj.printC()    # クラスCのprintA()メソッドを実行
obj.printD()    # クラスDのprintA()メソッドを実行
obj.printAll()    # クラスAのprintA()メソッドを実行
