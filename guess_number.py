number = 10
max_guesses = 3
guesses_left = max_guesses

print("I'm thinking of a number...")
while guesses_left > 0:
    print(f"You have {guesses_left} guesses left.")
    guess = input("What number am I thinking of? (Enter 'q' to quit) ")
    if guess.lower() == 'q':
        print(f"The number was {number}.")
        break
    guess = int(guess)
    if guess == number:
        print("Congratulations! You guessed the right number.")
        break
    elif guess < number:
        print("Too low! Try again.")
    else:
        print("Too high! Try again.")
    guesses_left -= 1
else:
    print(f"Sorry! You've run out of guesses. The number was {number}.")