import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

computer_move = ""

# Request user input
player_move = input("Choose [r]ock, [p]aper or [s]cossors: ")

# Validate Player Move
if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move == paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

# Generate a random number
computer_random_number = random.randint(1, 3)

# Validate Computer Move
if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
else:
    computer_move = scissors

# Check moves
if (player_move == rock and computer_move == scissors) or \
        (player_move == paper and computer_move == rock) or \
        (player_move == scissors and computer_move == paper):
    print(f"The computer chose {computer_move}")
    print("You win!")
elif player_move == computer_move:
    print(f"The computer chose {computer_move}")
    print("Draw!")
else:
    print(f"The computer chose {computer_move}")
    print("You lose!")

