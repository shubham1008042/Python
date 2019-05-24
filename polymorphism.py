class A:
    def Zap1(self):
        print("apna time aayega")
    def Zap2(self):
        print("Sher aaya Sher")

class B(A):
    def Zap3(self):
        print("kaa lalla")

class C(A):
    def Zap4(self):
        print("Boht hard")

ob1=A()
ob2=B()
ob3=C()

ob1.Zap1()
ob1.Zap2()
ob2.Zap1()
ob2.Zap3()
ob3.Zap1()
ob3.Zap4()
