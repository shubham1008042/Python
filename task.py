#"to print table of given no."

n=11
x=2
for i in range(1,n):
    print("|",x ,"*", i,"|",x*i,"|")

print("....................................")

#Write a function called fizz_buzz that takes a number.If the number is divisible by 3, it should return “Fizz”.
#If it is divisible by 5, it should return “Buzz”.If it is divisible by both 3 and 5, it should return “FizzBuzz”.
#Otherwise, it should return the same number

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

#To find leap year

def leap(year):
    if(year%4==0):
        print("leap")
    else:
         print("nii h")
leap(2000)
leap(2016)
leap(2018)
    
