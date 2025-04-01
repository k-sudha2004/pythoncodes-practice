#APPS MEMORY
t = int(input())  

for _ in range(t):
    S, X, Y, Z = map(int, input().split()) 
    unused_memory = S - (X + Y)  

    if unused_memory >= Z:
        print(0) 
    elif (unused_memory + X) >= Z:
        print(1)  
    elif (unused_memory + X + Y) >= Z:
        print(2)  
