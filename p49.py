t = int(input())
for _ in range(t):
    A, B, X, Y = map(int, input().split())
    if A == B:
        print("YES")
    elif B > A:  # Need to increase the temperature
        if (B - A) <= X:
            print("YES")
        else:
            print("NO")
    else:  # B < A, need to decrease the temperature
        if (A - B) <= Y:
            print("YES")
        else:
            print("NO")
