# Accept user input as integer (decimal), print its equivalent in octal, decimal and hexa-decimal.
#decimal = int(input("Enter an integer (decimal)"))

decimal = 5
print(decimal,  oct(decimal), hex(decimal))

#Repeat this with user input as integer (octal), print its equivalent in octal, decimal and hexa-decimal
#octal = int(input("Enter an integer (octal)"), 8)
octal = 0o5
print(octal, oct(octal), hex(octal))

#Repeat this with user input as integer (hexa-decimal), print its equivalent in octal, decimal and hexa-decimal.
#num = int(input("Enter an integer (hex)"), 16)

num = 0x16

print(hex(num), num, oct(num))
          

