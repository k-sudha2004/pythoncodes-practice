#AIR LINES
import math
t=int(input())
for i in range(t):
    x,n=map(int,input().split())
    air_craft=n/100
    if x>=air_craft:
        print(0)
    else:
        print(math.ceil(air_craft)-x)