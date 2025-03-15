#CANDY DISTRIBUTION
t=int(input())
for i in range(t):
    N,M=map(int,input().split())
    CANDIES=N/M
    if CANDIES%2==0:
        print("yes")
    else:
        print("NO")