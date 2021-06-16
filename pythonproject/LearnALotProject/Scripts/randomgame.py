# generate a number 1 ~ 10
# Get input from user
# check that input number falling in 1 to 10
# check that if the number matching to the generated number. Number is the right guess.
# Otherwise ask again
from random import randint


def random_game(lucky_number=1, rand_start=1, rand_end=10):
    """ This function is for random game generation."""
    award = 0
    gen_int = randint(rand_start, rand_end)
    print(gen_int)
    if rand_start <= lucky_number <= rand_end:
        # print('Great!!! you entered the number in lucky number range, but not the exact number')
        award = 1
        if lucky_number == gen_int:
            # print("you are really lucky")
            award = 2
    return award
