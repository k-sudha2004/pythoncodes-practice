#second largest
t=int(input())
for i in range(t):
    a,b,c=map(int,input().split())
    numbers=[a,b,c]
    numbers.sort()
    print(numbers[1])