num=9
factorial=1
if num < 0:
    print("no factorial")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("factorial is:",factorial)
