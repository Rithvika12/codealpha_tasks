import random

words = ["python", "apple", "robot", "chair", "house"]

word = random.choice(words)
guessed_word = ["_"] * len(word)
incorrect_guesses = 0

print("Welcome to Hangman Game!")

while incorrect_guesses < 6 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", 6 - incorrect_guesses)

    guess = input("Guess a letter: ").lower()

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong Guess!")

if "_" not in guessed_word:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)