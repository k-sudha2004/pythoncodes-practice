#FILL CANDIES   
import math
t=int(input())
for i in range(t):
    N,K,M=map(int,input().split())
    chocklate=(K*M)
    pockets=N/chocklate
    print(math.ceil(pockets))