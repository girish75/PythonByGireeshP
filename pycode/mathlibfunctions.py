import math
degree = input("enter degree to calculate trignomatric values ")
print("You entered " + str(type(degree)), "value")
degree = math.ceil(int(degree))
print("converted into "+ str(type(degree)), "value")

print ("Cos", degree , " = ", math.cos(degree))
print ("Sin", degree , " = ", math.sin(int(degree)))
print ("tan", degree , " = ", math.tan(int(degree)))
print ("Sqrt", degree , " = ", math.sqrt(int(degree)))
print("Factorial " + str(math.factorial(degree)))





