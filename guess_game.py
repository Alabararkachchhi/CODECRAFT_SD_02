# use random module for get random numbers:
import random

number = random.randint(1, 100)
attempts = 0

# use loop for run continuously 
while True:
    guess = int(input("guess any numbers between 1 - 100:"))
    attempts += 1

    if guess == number:
        print("You Win!")
        print("Attempts:",attempts)
        break

    elif guess > number:
        print("Too High!")
    
    else:
        print("Too Low")
