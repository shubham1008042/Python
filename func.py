# Functions in python
def abc(a,b,c):
    print(a+b+c)

abc(1,3,4)    

print("...............................................")

def xyz(*num):
    sum=0
    for n in num:
        sum=sum+n
    print("sum is:",sum)

xyz(4,5)
xyz(1,2,3,4,5,6,7,7,8)

print(".................................................")


def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

print(".........................................................")

def summer(**sss):
    '''print(type(sss))'''

    for key, value in sss.items():
        print("{} is {}".format(key,value))

summer(Firstname="ram",lastname="lakhan",Age=22)
summer(Firstname="sita",lastname="gita",Age=32)

print("......................................................")

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Sharma", Age=22, Phone=1234567890)
intro(Firstname="John", Lastname="Wood")
