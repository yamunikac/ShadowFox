import random
words = ["python", "developer", "internship", "programming"]
word = random.choice(words)
guessed = []
tries = 6
while tries > 0:
    display = ""
    for letter in word:
        display += letter if letter in guessed else "_"
    print(display)
    if "_" not in display:
        print("You won")
        break
    guess = input("Guess a letter: ").lower()
    if guess in guessed:
        print("Already guessed")
        continue
    guessed.append(guess)
    if guess not in word:
        tries -= 1
        print("Wrong guess, tries left:", tries)
if tries == 0:
    print("You lost. Word was:", word)
