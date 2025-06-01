num=int(input())
if num<=1:
    print("prime")
for i in range(2,num):
    if num % i == 0:
        print("it is not prime ")
        break
else:
    print("prime")