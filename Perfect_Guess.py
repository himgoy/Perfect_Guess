import random

randNo = random.randint(1, 100)
count = 1
i = 1
print("This is a Guessing Game. You will need to guess a number between "
      "\n1 and 100 which is same as that of the Computer\n")
while i == 1:
    userGuess = int(input("Enter Your Guess : "))
    if userGuess == randNo:
        print(f"********\nYou Guessed the CORRECT value "
              f"in {count} tries\n********")
        break
    else:
        count += 1
        if userGuess > randNo:
            print("Your guess is too high")
        else:
            print("Your guess is too low")

with open("HighScore", 'r') as f:
    CurrHigh = int(f.read())

if CurrHigh > count:
    with open("HighScore", 'w') as f:
        print("\n************\nCongratulations!!! You have created a new HIGH SCORE\n************")
        f.write(str(count))




