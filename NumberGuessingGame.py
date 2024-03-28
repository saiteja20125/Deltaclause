import random

def guess_number():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Introduction
    print("Welcome to the Guess the Number game!")
    print("I have chosen a number between 1 and 100. Can you guess what it is?")
    
    # Initialize guess variable
    guess = None
    
    # Start the game loop
    while guess != secret_number:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue
        
        # Check if the guess is too high, too low, or correct
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the correct number:", secret_number)
            break

# Call the function to start the game
guess_number()
