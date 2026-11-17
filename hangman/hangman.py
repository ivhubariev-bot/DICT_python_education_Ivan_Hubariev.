import random

print("HANGMAN")

words = ["python", "java", "javascript", "php"]

while True:
    option = input('Type "play" to play the game, "exit" to quit: ')

    if option == "exit":
        break
    elif option == "play":
        word = random.choice(words)
        guessed_word = ["-"] * len(word)
        guessed_letters = set()
        attempts = 8

        while attempts > 0:
            letter = input("Input a letter: ")

            if len(letter) != 1:
                print("You should input a single letter")
            elif letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
            elif letter in guessed_letters:
                print("You've already guessed this letter")
            else:
                guessed_letters.add(letter)

                if letter in word:
                    for i in range(len(word)):
                        if word[i] == letter:
                            guessed_word[i] = letter
                else:
                    print("That letter doesn't appear in the word")
                    attempts -= 1

            print("".join(guessed_word))

            if "-" not in guessed_word:
                print(f"You guessed the word {word}!")
                print("You survived!")
                break

        if attempts == 0 and "-" in guessed_word:
            print("You lost!")
