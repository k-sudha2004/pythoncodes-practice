#n=input()
#sum = 0
#for i in n:
    #sum= sum + int(i)
#print(sum)
n=int(input())
sum = 0
while n!=0:
    digit = int(n%10)
    sum += digit
    n = n/10
print(sum)




