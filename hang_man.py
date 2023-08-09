import random
from hangman_word_list import word_list
from hangman_art import stages
from hangman_logo import logo


chosen_word = random.choice(word_list)
print(logo)
print(f"The chosen word is {chosen_word}")

guess_list = []
for _ in chosen_word:
    guess_list.append('_')

word_lenght = len(chosen_word)
end_of_game = False

lives = 6

while not end_of_game:
    guess = input("Guess a Letter\n").lower()

    if guess in guess_list:
        print(f"You've already guessed {guess}")
        print(guess_list)

    for position in range(word_lenght):
        if guess == chosen_word[position]:
            guess_list[position] = guess
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(f"{' '.join(guess_list)}")

    if "_" not in guess_list:
        end_of_game = True
        print("You Win!")
    
    print(stages[lives])
