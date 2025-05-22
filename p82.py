a = list(map(str,input().split()))
result =[]
for i in range(len(a)):
    for j in range(0,len(a)):
        if i != j:
            b = a[i] + a[j]
            r = b[::-1]
            if b == r:
                result.append([i,j])
for pair in result:
     print(f"{pair[0]} {pair[1]}",end=' ')