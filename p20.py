#water buckets
t=int(input())
for i in range(t):
    X,Y=map(int,input().split())
    water=X//(Y*2)
    if X<Y*2:
         print(0)
    else:
         print(water)