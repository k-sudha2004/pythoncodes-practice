#CYCLIC QUADRILATERAL
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if a+c==180 or b+d==180:
        print("yes")
    else:
        print("no")