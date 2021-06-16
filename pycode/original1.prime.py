

def is_prime(num):
  
    """Function to calculate prime""" # doc string
    if num % 2 == 0 and num>2:
            return False
           
    for n in range(3,int(math.sqrt(num))+1, 2):
                if num %n == 0:
                    return False
                               
    return True
    
    
Import math
print(is_prime(13))
