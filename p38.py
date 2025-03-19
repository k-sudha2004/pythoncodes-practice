#EXPERT SETTER
t=int(input())
for i in range(t):
    a,b=map(int, input().split())
    expert=a-b
    if expert<=b:
        print("yes")
    else:
        print("no")