T = int(input())
for _ in range(T):
    X, Y, Z = map(int, input().split())
    total_students = X * Y
    if 2 * Z > total_students:
        print("YES")
    else:
        print("NO")
