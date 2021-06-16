# 1.	Accept user input of two complex numbers (total 4 inputs, 2 for real and 2 for imaginary part). 
# Perform complex number operations (c1 + c2, c1 - c2, c1 * c2)

a = int(input("For first complex number, enter real number"))
b = int(input("For first complex number, enter imaginary number"))

a1 = int(input("For second complex number, enter real number"))
b1 = int(input("For second complex number, enter imaginary number"))

c1 = complex(a,b)
print(c1)
c2 = complex(a1,b1)
print(c2)

print("Addition of two complex number =", c1 + c2)

#Subtraction
print("Subtraction of two complex number =", c1 - c2)

#Multiplication
print("Multiplication of two complex number =", c1 * c2)

#Division
print("Division of two complex number =", c1 / c2)

c = (3 + 6j)

print('Complex Number: Real Part is = ', c. real)
print('Complex Number: Imaginary Part is = ', c. imag)
print('Complex Number: conjugate Part = ', c. conjugate())

