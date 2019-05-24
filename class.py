'''class and object'''
class shub:
    def abc(self):
        print("ustad jiiii")

oj=shub()
oj.abc()

print("...........................................")

'''Single Inheritence'''
class A:
    def xyz(self):
        print("Aaila")
class B(A):
    def xy(self):
        print("Jaadu")

ob=B()
ob.xy()
ob.xyz()

print("............................................")

'''multilevel'''
class Z:
    def klol(self):
        print("gulu gulu")
class M(Z):
    def jol(self):
        print("aaii ja gavat")
class J(M):
    def lol(self):
        print("kya bat")

ob=J()
ob.lol()
ob.jol()
ob.klol()

print("..............................................")

'''multiple inheritence'''
class AB:
    def pyar(self):
       print("Love Yourself")
class BC:
    def pyar(self):
        print("Love All")
class CD(Love,Lust):
    def pyar(self):
        print("ab kya")
    super().pyar('Love')
ob=CD()
ob.pyar()
