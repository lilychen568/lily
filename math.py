num=10
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")


a = 0.1 + 0.2 - 0.3
print(a)
print("%.2f" % round(a, 2))

import random

print(random.randint(0,9))
