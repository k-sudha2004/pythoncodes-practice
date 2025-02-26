# MAXIMUM TASTE
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    first=max(a,b)
    second=max(c,d)
    print(first+second)