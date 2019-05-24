'''single inheritence'''
class fruit:
    def eat(self):
        print("eat that fruit")

class mango(fruit):
    def juice(self):
        print("mango juice")

ob=mango()
ob.eat()
ob.juice()

print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

'''multiple'''
class A:
    def Zap(self):
        print("A for apple")

class B:
    def Zap1(self):
        print("B for balls")

class C(B,A):
    def Zap2(self):
        print("C for Chcha")

ob= C()
ob.Zap2()
ob.Zap1()
ob.Zap()
    
