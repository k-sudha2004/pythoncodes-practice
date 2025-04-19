#FINDING SHOES
T=int(input())
for i in range(T):
    N,M=map(int,input().split())
    shoes=N-M
    bought_shoes=shoes+N
    if M>=N:
        print(N)
    elif N>M:
        print(bought_shoes)