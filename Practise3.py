import random

# Welcome message
print("Welcome to Hangman")

# 2. List of words
word_list = ['python', 'hangman', 'computer', 'developer', 'keyboard']

# Randomly select a word from the list
word_to_guess = random.choice(word_list)

# 3. Display the word as underscores
guessed_word = ['_'] * len(word_to_guess)
attempts_left = 10
guessed_letters = []

print("The word to guess: ", ' '.join(guessed_word))

# Main game loop
while attempts_left > 0 and '_' in guessed_word:
    print(f"\nAttempts left: {attempts_left}")
    print("Current word: ", ' '.join(guessed_word))
    
    guess = input("Guess a letter: ").lower()
    
    # 3.4. Check for valid input (alphabet only)
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid Character. Please enter a single alphabet.")
        continue
    
    # 3.6. Check if the letter was already guessed
    if guess in guessed_letters:
        print("You've already guessed this letter. Try a different one.")
        continue
    
    guessed_letters.append(guess)

    # 3.8. Correct guess
    if guess in word_to_guess:
        print("Correct guess!")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                guessed_word[i] = guess
    else:
        # 3.7. Incorrect guess, decrease attempts
        print("Wrong guess!")
        attempts_left -= 1

# End of game
if '_' not in guessed_word:
    print("\nAwesome! You guessed the word correctly:", word_to_guess)
    print("Thank you for playing. See you next time!")
else:
    print("\nYou've run out of attempts. The word was:", word_to_guess)
    print("Thank you for playing. Better luck next time!")