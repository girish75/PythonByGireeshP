def hello():
    print("This is hello function")
    
# function to find factorial

def fact(n):
    """ function to find factorial value"""
   # print("Factorial function called" )
    if n == 1:
     return 1
    else:
      return (n * fact(n-1))
  
   

# Define `main()` function
def main():
  hello()
  print("This is a main function")
  
# Execute `main()` function 
if __name__ == '__main__':
    main()


#function to check positive or Negative

def check_num(a)->int:
    """ function to check positive or negative number"""
    if a > 0:
        print(a, " is a positive number ")
    elif a == 0:
        print (a, "is a zero")
    else:
        print (a, " is a negative number")

	
