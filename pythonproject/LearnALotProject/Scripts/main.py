# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
from randomgame import random_game
from random import randint
#import sys
#import pyjokes


if __name__ == '__main__':
    while True:
        try:
            user_int = int(input("Enter your lucky number between 1 to 10 both inclusive. "))
        except ValueError:
            print("Please enter an integer number ")
            continue
        else:
            break
        finally:
            pass

    #    # gaward = random_game(user_int, int(sys.argv[1]),int(sys.argv[2]))
    gaward: int = random_game( user_int, 1, 10 )
#
if gaward == 1:
    print('Great!!! you entered the number in lucky number range, but not the exact number')
    print(f"You won lucky range award of 300$, Your token is", randint(1,100))
    print("Show this token to the token window to collect your prize")
elif gaward == 2:
     print("You are lucky Hero of our game. You won 1000$ award. ... Congratulations!!!")
else:
     print("Better luck next time")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
