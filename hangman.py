import random
import hangman_words
import hangman_art

def generate_number():
    random_index = random.randint(0, len(hangman_words.word_list) - 1)
    return random_index

secret_word = hangman_words.word_list[generate_number()]
blank_list = []
guessed_list = []

for i in range(0, len(secret_word)):
    blank_list.append('_')

lives = 6
end_of_game = False
letter_found = False

print(hangman_art.logo)

while end_of_game == False:
    for i in range(0, len(blank_list)):
        print(blank_list[i], end='')
        print(' ', end='')

    print('\n')
    user_guess = input('Guess a letter: \n')

    print('\n')

    if len(user_guess) != 1 or not user_guess.isalpha():
        if len(user_guess) > 1:
            print('Only guess 1 letter!')
        if not user_guess.isalpha():
            print('Only enter a letter!')
        continue
    
    if user_guess not in guessed_list:
        guessed_list.append(user_guess)
    else:
        print(f'You already guessed {user_guess}')
        continue    

    for i in range(0, len(secret_word)):
        if user_guess == secret_word[i]:
            blank_list[i] = secret_word[i]
            letter_found = True
    
    if not letter_found:
        lives -= 1
        print(f'Lives remaining = {lives}')

    for i in range(0, len(blank_list)):
        print(blank_list[i], end='')
        print(' ', end='')
    print('\n')
    
    print(hangman_art.stages[lives])
    letter_found = False

    if '_' not in blank_list or lives <= 0:
        if lives <= 0:
            print(f'You lose. The word was {secret_word}\n')
        else:
            print('You win!')
        end_of_game = True