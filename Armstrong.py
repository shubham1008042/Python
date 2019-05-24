num=int(input("Enter no."))
sum=0
temp=0
digit=0

temp=num
while temp>0:
    digit=temp%10
    sum +=digit ** 3
    temp //= 10

if num==sum:
    print("armstrong")
else:
    print("NOPE")

