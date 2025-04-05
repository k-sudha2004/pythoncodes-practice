#MINIMUM COINS
t = int(input())  

for _ in range(t):
    x = int(input())

    if x % 5 != 0:
        print(-1)  
    else:
        print(x // 10 + (1 if x % 10 == 5 else 0))
