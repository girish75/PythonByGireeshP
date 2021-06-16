#1.	What is the output of following code:
#if __name__ = '__main--':

s1 = "Welcome to Python"
print(len(s1))
#output 17

s2= "It's my string"
print(len(s2)) #output 14

s3= "It's \tmy string\n"
print(len(s3)) #output 16

s4= r"It's \tmy string\n"
print(len(s4)) #output 18

str1 = "this is string example in Python!!!";
str2 = "exam";
print(str1.find(str2)); # Returns -1 in case of error
#output 15
print(str1.find(str2, 10));
#output 15, because string.find(value, start, end) start 	Optional. Where to start the search. Default is 0

print(str1.find(str2, 10, 50))
#output 15, because string.find(value, start, end)
print(str1.find(str2, 16));
#output -1, because no other occurance of this string after 16th character.

str3="is"
print(str1.find(str3));
#ouput = 2
print(str1.rfind(str3)); # Returns -1 in case of error
#Searches the string for a specified value and returns the last position of where it was found
#ouput = 5, ?????????????????
s1="abc123"
print("123".isdigit()) #output = True
print(s1.isdigit()) #output = False
print("123".isnumeric()) #output = True
print(s1.isalpha()) #output = False
print(s1.isnumeric()) #ouput = False.

