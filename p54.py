#car or bike
t=int(input())
for i in range(t):
    x,y=map(int,input().split())
    if x<y:
        print("bike")
    elif x>y:
        print("car")
    elif x==y:
        print("same")