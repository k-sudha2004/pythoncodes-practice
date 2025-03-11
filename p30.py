#CRED COINS
t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    c=a*b
    d=c//100
    if c<100:
        print("0")
    elif c==100:
        print("1")
    else:
        print(d)