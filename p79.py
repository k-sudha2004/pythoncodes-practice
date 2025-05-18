#ALTERNATE EVEN NUMBERS
a,b=map(int, input(). split ())
count=0
for i in range(a+1,b):
   if i % 2 == 0:
     if count%2 == 0:
       print (i,end=" ")
     count += 1