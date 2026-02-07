#generate a random number
import random
print(random.randint(0,9))

#check even or odd
num=int(input("Enter a number :"))
if(num%2)==0: 
  print("{0} is even ",format(num))
else:
  print("{0} is odd",format(num))

#factorial in python
import math
n=3
print(math.factorial(n))
