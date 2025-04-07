#SELF DEFENCE
t = int(input()) 

for _ in range(t):
    n = int(input()) 
    ages = list(map(int, input().split()))
    eligible = sum(1 for age in ages if 10 <= age <= 60)
    
    print(eligible)
