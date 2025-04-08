
#MONOPOLY
t=int(input())
for i in range(t):
    a,b,c,d=map(int, input().split())
    p=b+c+d
    q=a+c+d
    r=a+b+d
    s=a+b+c
    if a>p or b>q or c>r or d>s:
        print("yes")
    else:
        print("no")