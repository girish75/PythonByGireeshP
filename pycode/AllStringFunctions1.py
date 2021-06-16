#capitalize()	Converts the first character to upper case
string = input("What is your name? ")
if string.isalnum():
    print("Your name is alphanumeric")
    
capitalize_str = string.capitalize()
print(capitalize_str)

string1 = string.upper()
#casefold()	Converts string into lower case
print(string1)
casefold_str =string1.casefold()
print(casefold_str)

print(string.rjust(7, "*"))


#center()	Returns a #centered string
print(string.center(20,"*"))

print(string.replace("i", "e"))  #string.replace(oldvalue, newvalue, count) 

print("    world    ".strip())

pivot = len(string)//2

# string are immutable

newstring = string[:pivot]+ " superb " + string[pivot +1:]     #s = s[:index] + newstring + s[index + 1:]
print(newstring)

#count()	Returns the number of times a specified value ocurs in a string
print("Count occurance of \"i = \"" , string.count("i"))

#encode()	Returns an encoded version of the string. If no encoding is specified, UTF-8 will be used.
print ("Encoded string = ",string.encode())

#endswith()	Returns true if the string ends with the specified value
v = input("Enter ending character of your name")

if string.endswith(v):
     print("ending with right value")
else:
     print("not ending with right value")

     
    
#expandtabs()	Sets the tab size of the string. You need a tabed string.
print("H\te\tl\t\l\to")
print("H\te\tl\tl\l\to".expandtabs(2))
     
#find()	Searches the string for a specified value and returns the position of where it was found
print("find example - printing occurance of entered value", string.find(v))

#index()	Searches the string for a specified value and returns the position of where it was found

print("Index example - printing occurance of entered value", string.index(v))
      
#format()	Formats specified values in a string
age = input("What is your age ?")
firstformat= "Hello {name}, your age is {agevalue}"
print(firstformat.format(name = string, agevalue = age))

