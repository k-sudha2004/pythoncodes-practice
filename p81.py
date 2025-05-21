#CHECK LIST IS EVEN OR NOT
n = list(map(int,input().split()))
for i in range(len(n)):
    if n[i] % 2 == 1:
        print(" not even")
        break
else:
    print("Even")