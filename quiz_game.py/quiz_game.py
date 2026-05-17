print("Welcome to computer quiz!") 

starting = input("Do u wanna play now ? ").lower()

if(starting) != "yes":
    quit()

score = 0

print("Welcome to the Quiz.......")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct answer")
    score +=1
else:
    print("In Correct answer")


answer = input("What does GPU stand for? ")

if answer == "grpahics processing unit":
    print("Correct answer")
    score +=1
else:
    print("In Correct answer")

answer = input("What does RAM stand for? ").lower()

if answer == "Random access memory":
    print("Correct answer")
    score +=1
else:
   print("In Correct answer")

print ("Done!!!")
print ("Your score is " + str(score))
print("Score Percentage " + str(score/3*100) + "%" )
