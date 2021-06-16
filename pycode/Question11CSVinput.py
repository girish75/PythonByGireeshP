# Q 11 Assignment
import math

C = 50
H = 30
d = input("enter comma separated decimal input")
list1 = d.split(',')
length = len(list1)
print(d)
print(list1)
print(length)

for i in list1:
 print(i)
 D = int(i)
 Q = math.sqrt((2 * C * D)/H)
  
 print("Q = ", int(Q))
