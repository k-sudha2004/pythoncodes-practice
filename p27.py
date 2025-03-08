# MARIO TRANSFORMATION
t=int(input())
for i in range(t):
    X=int(input())
    if X % 3 == 0:
        print("NORMAL")
    elif X % 3 == 1:
        print("HUGE")
    else:
        print("SMALL")
