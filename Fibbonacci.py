limit=14
count=0

a=0
b=1

if limit<=0:
    print("0")

elif limit==1:
    print("series",limit,":")
    print(a)

else:
    print("series upto",limit,":")
    while count<limit:
        print(a,end=',')
        c=a+b
        a=b
        b=c
        count +=1
