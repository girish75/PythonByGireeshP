# objective : 1. Understand how to create user defined packages and modules.
# objective : 2 . Understand system defined random module and its functions.
# objective : 3 Understand system defined sys module and its functions.
import random
import sys
import randomization
import funclib



if __name__ == '__main__':
    mylst = ['apple', 'orange']
    guestlst = ['abc']
    print(funclib.divide(4, 2))
    print(__name__)
    print(randomization)
    #help(random)
    #print(dir(random))
    # Using randrange() to generate numbers from 0-100
    print("Random number from 0-100 is : ", end="")
    print(random.randrange(100))
    # Using randrange() to generate numbers from 50-100
    print("Random number from 50-100 is : ", end="")
    print(random.randrange(50, 100))



    # Using randrange() to generate numbers from 50-100
    # skipping 5
    print("Random number from 50-100 skip 5 is : ", end="")
    print(random.randrange(50, 100, 5))
    print("Rand range = ", random.randrange(0, 100, 20))
    print(random.choice([1, 2, 3, 4, 5, 6]))
    print(random.choice([1, 2, 3, 4, 5, 6]))
    lst = [1, 2, 3, 4, 5, 6]
    print(lst)
    random.suffle(lst) # inplace shuffling.
    print(lst)
