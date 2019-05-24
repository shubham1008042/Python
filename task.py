n=11
x=2
for i in range(1,n):
    print("|",x ,"*", i,"|",x*i,"|")

print("....................................")

def fizzbuzz(num):
    if(num%3==0 and num%5==0):
        print("FizzBuzz")
    elif(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    
fizzbuzz(15)
fizzbuzz(12)
fizzbuzz(21)

print("......................................")

def leap(year):
    if(year%4==0):
        print("leap")
    else:
         print("nii h")
leap(2000)
leap(2016)
leap(2018)
    
