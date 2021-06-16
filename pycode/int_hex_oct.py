# Accept user input as integer (decimal), print its equivalent in octal, decimal and hexa-decimal.
decimal = int(input("Enter an integer (decimal)"))
print(decimal,  oct(decimal), hex(decimal))
#print(decimal, int(decimal, 8), int(decimal, 16))- int() can't convert non-string with explicit base

#Repeat this with user input as integer (octal), print its equivalent in octal, decimal and hexa-decimal
octal = int(input("Enter an integer (octal)"), 8)
print(octal, oct(octal), hex(octal))

#Repeat this with user input as integer (hexa-decimal), print its equivalent in octal, decimal and hexa-decimal.
num = int(input("Enter an integer (hex)"), 16)

print(hex(num), num, oct(num))
          

