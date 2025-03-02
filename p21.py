#Greater average
t = int(input())  # Read the number of test cases
for i in range(t):  # Loop through each test case
    a,b,c = map(int, input().split())
    average=(a+b)/2
    if average>c:
        print('yes')
    else:
        print('no')
        