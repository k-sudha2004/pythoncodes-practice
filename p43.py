#problems list
T = int(input())

for _ in range(T):
    # Read the number of problems in the to-do list
    N = int(input())
    # Read the difficulty ratings for each problem
    difficulties = list(map(int, input().split()))
    
    # Count the number of problems with difficulty rating >= 1000
    to_remove = sum(1 for d in difficulties if d >= 1000)
    
    # Output the count of problems that need to be removed
    print(to_remove)
