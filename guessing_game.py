import random
print("The computer choose a number between 1-100. You have [5] tries to guess the number!")
number_tries = 5

computer_number = random.randint(1, 100)
print(computer_number)
print()
player_number = int(input(f"Guess the number! You have left [{number_tries}] tries: "))

while True:
    if number_tries == 1:
        print(f"You lost the game! The numbers is [{computer_number}] ")
        break

    if computer_number < player_number < 100:
        print()
        print("The computer number is lower!")
    elif player_number < computer_number:
        print()
        print("The computer numbers is higher")
    elif player_number > 100:
        print()
        print("ERROR! You can choose a number between 1-100")
        player_number = int(input(f"Guess the number! You have left [{number_tries}] tries: "))
        continue

    elif player_number == computer_number:
        print()
        print(f"Congratulations! You guessed the number!")
        break

    print()
    number_tries -= 1
    player_number = int(input(f"Guess the number! You have left [{number_tries}] tries: "))
