import random

print("Welcome to Guess that Roll!")
print("The game is very simple to play. All you have to do is to enter a number ranging from 1 to 6")
print("Then the computer will roll a dice and a random number will be generated.")
print("If the number entered by you matches the one rolled by the computer you will win a point!")
print("If not, you lose!")
print("Have Fun Playing!")


input_num = int(input("Enter a Number between 1&6 or 0 to exit: "))
score = 0 #Initial Score


while True:
    dice_num = random.randint(1,6)  #A random number between 1 and 6 is generated.


    if input_num<0 or 6<input_num:
        input_num = int(input("Please only enter a number between 1 and 6 or 0 to exit: "))

    else:
        if input_num != 0:
            if input_num == dice_num:
                print("Bingo! :) The dice did roll on:", dice_num)
                print("")
                score += 1

            else:
                print("Better Luck Next Time! :( The Dice rolled on:", dice_num)
                print("")

            
            input_num = int(input("Enter a Number between 1&6 or 0 to exit: "))


        elif input_num == 0:
            print("Thanks For Playing!")
            print("Your Final Score was:",score)
            break
