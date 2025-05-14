aimport random

def validate_guess(guess):
    """Validate user's letter guess."""
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        return False
    return True

def play_hangman():
    """Main Hangman game logic."""
    word_list = ["apple", "codealpha", "college"]
    chosen_word = random.choice(word_list)
    
    # Hide the word during actual gameplay
    # print(f'Debug: Chosen word is {chosen_word}')
    
    display = ['_' for _ in range(len(chosen_word))]
    lives = 6
    guessed_letters = set()
    
    while lives > 0:
        print(' '.join(display))
        print(f'Lives remaining: {lives}')
        
        guess = input('Guess a letter: ').lower()
        
        if not validate_guess(guess):
            continue
        
        if guess in guessed_letters:
            print('You already guessed that letter. Try again.')
            continue
        
        guessed_letters.add(guess)
        
        if guess in chosen_word:
            for position in range(len(chosen_word)):
                if chosen_word[position] == guess:
                    display[position] = guess
        else:
            lives -= 1
            print(f'Wrong guess! {stages[6 - lives]}')
        
        if '_' not in display:
            print('Congratulations! You won!')
            print(f'The word was: {chosen_word}')
            return
    
    print(f'Game over! The word was: {chosen_word}')

if __name__ == '__main__':
    play_hangman()