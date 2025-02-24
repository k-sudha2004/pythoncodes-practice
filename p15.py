#JENGA NIGHT
t=int(input())
for  i in range(t):
    N,X=map(int,input().split())
    d=X%N
    if d==0:
        print("yes")
    else:
        print("no")