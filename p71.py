#PASS OR FAIL
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    total=a-b
    marks=b*3-total*1
    if marks>=c:
        print("pass")
    else:
        print("fail")