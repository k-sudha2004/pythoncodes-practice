#BLACK JACK
t=int(input())
for i in range(t):
    a,b=map(int,input().split())
    game=a+b
    if game<=10:
        print(-1)
    else:
        print(21-game)