#CHEF GAMES
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    game=a+b+c+d
    if game==0:
        print("in")
    else:
        print("out")