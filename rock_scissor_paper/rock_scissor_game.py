import random

user_wins = 0
computer_wins = 0

options = ['rock','scissors','paper']

while True:
    user_select = input('Choose from Rock / Scissors/ Paper or type "q" to exit ').lower()

    if user_select == "q":
        break

    if user_select not in options:
        continue

    computer_select = options[random.randint(0,2)]

    print(computer_select)

    if user_select == computer_select:
        print("Its a draw")
        continue

    if user_select == options[0] and computer_select == options[1] :
        user_wins += 1
        print("You got one point")
    elif user_select == options[1] and computer_select == options[2]:
        user_wins += 1
        print("You got one point")
    elif user_select == options[2] and computer_select == options[0]:
        user_wins +=1
        print("You got one point")
    else:
        computer_wins += 1
        print("Computer got one point")

if user_wins > computer_wins:
    print("You Wonnnnnnn!!!!!!!!!!!")
elif user_wins < computer_wins:
     print("You Looost!!!!!!!!!!!")
else:
    print ("Drawwww!!!")

print("Your Score :",user_wins)
print("Computer Score :",computer_wins)

    

    
    





