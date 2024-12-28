import random
import hangman_art
import hangman_words


word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
display = []
lives = 6


print(hangman_art.logo)
for _ in range(len(chosen_word)):
    display += "_"
print(display)


end_of_game = False
while not end_of_game:
    guess = input("Please guess a letter: ").lower()
    if guess in display:
        print(f"The letter {guess} is already guessed ")

    for i in range(len(chosen_word)):
        letter = chosen_word[i]
        if letter == guess:
            display[i] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        lives -= 1

    if lives == 0:
        end_of_game = True
        print(f"You lose.\nThe word was {chosen_word}")
    print(hangman_art.stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You won")
