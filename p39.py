#expert setter
T = int(input())

for _ in range(T):
    A, B, X, Y = map(int, input().split())
    
    # Calculate total required power and total power available
    required_power = A * B
    available_power = X * Y
    
    # If available power is at least the required power, funding is possible.
    if available_power >= required_power:
        print("Yes")
    else:
        print("No")