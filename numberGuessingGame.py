import random

def main():
    randomNumber = random.randint(1, 10)

    for i in range(3):
        guess = int(input("Please guess a number between 1 and 10: "))

        if guess == randomNumber:
            print("Congratulations, you're right! The number is indeed", str(randomNumber))
            return

        elif guess < randomNumber:
            print("Aim higher!")

        else:
            print("Aim lower!")

    print("Sorry, you ran out of guesses!")

main()