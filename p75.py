#A and B CONTEST
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    
    # Attempting A first, then B
    score_A_first = (500 - X * 2) + (1000 - (X + Y) * 4)
    
    # Attempting B first, then A
    score_B_first = (1000 - Y * 4) + (500 - (X + Y) * 2)
    
    # Take the maximum of both strategies
    print(max(score_A_first, score_B_first))
