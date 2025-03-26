#chessboard
def chessboard_distance(X1, Y1, X2, Y2):
    return max(abs(X1-X2), abs(Y1-Y2))

T = int(input())  # Number of test cases

for _ in range(T):
    X1, Y1, X2, Y2 = map(int, input().split())
    print(chessboard_distance(X1,Y1,X2,Y2))
