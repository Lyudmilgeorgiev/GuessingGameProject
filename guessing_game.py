import random

computer_choice = random.randint(1, 100)
while True:
    player_choice = input("Guess the number (1-100): ")

    if not player_choice.isdigit():
        print("Invalid input. Try again...")
        continue

    player_number = int(player_choice)
    if player_number == computer_choice:
        print("You guess it!")
        break
    elif player_number > computer_choice:
        print("Too high!")
    elif player_number < computer_choice:
        print("Too low")