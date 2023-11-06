from random import randint


EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# function to check users guess against the answer
def check_answer(guess, answer, turns):
    """ checks answer aganst guess. Returns the number of turns remaining"""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


# make function to set difficulty
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():
    # choosing random number between 1 and 100
    print("Welcome to the Number Guessing Game.\nI'm thinking of a number between 1 and 100.")
    answer = randint(1,100)

    turns = set_difficulty()
    
    # repeat the guessing functionality if they get wrong
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        # let user guess the number
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if turns == 0:
            print("You've out of guesses, you lose")
            return
        elif guess != answer:
            print("Guess again.")

game()