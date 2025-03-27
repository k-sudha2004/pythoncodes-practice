#LAST LEVELS
def total_game_time(x, y, z):
    total_time = x * y  # Time taken to complete all levels
    breaks = (x - 1) // 3  # Number of breaks taken
    total_time += breaks * z  # Add break time
    return total_time

# Read number of test cases
T = int(input())

for _ in range(T):
    X, Y, Z = map(int, input().split())
    print(total_game_time(X, Y, Z))
