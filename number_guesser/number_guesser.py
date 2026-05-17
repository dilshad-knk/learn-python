import random

top_number = input("Type the max number ")

if top_number.isdigit():
    top_number = int(top_number)
    
    if top_number <= 0:
        print("Please type a number larger than 0")
        quit()
else:
    print("Pleae type a number next time")
    quit()

random_number =  random.randint(0, top_number)

guesses = 0
while (True):
    guesses += 1
    user_guess = input("Guess a number ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please Guess a number next time!!!")
        continue

    if (random_number == user_guess):
        print ("Got it!!!!")
        break
    elif user_guess > random_number:
        print("Wrong!!!!")
        print("Your guess greater than random number")
    else:
        print("Your guess less than random number")

print("You got it in", guesses,"guesses")
        
        