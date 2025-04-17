# bus deck
t=int(input())
for i in range(t):
    a=int(input())
    if a<=10:
        print("lower double")
    elif a<=15:
        print("lower single")
    elif a<=25:
        print("upper double")
    elif a<=30:
        print("upper single")
        