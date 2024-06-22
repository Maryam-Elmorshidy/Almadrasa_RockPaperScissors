"""
Changes made:

    Added clearer and concise introduction to the game.
    Reformatted and simplified input validation.
    Changed variable names to be more descriptive.
    Improved readability of the code.
    Added a prompt to play again after each round.


"""

import random

# Introduction to the game
print("Welcome to the Rock-Paper-Scissors game!\n")
print("In this game, you'll choose between rock, paper, or scissors.")
print("The computer will make its choice too.")
print("Let's see who wins!\n")

# Game loop
while True:
    # Player's input
    player_choice = input("Please choose (rock (r), paper (p), or scissors (s)): ").strip().lower()
    
    # Validate player's input
    if player_choice not in ['r', 'p', 's']:
        print("Invalid choice, please try again.")
        continue

    # Computer's choice
    computer_choice = random.choice(['r', 'p', 's'])
    
    # Display choices
    print(f"\nYour choice: {player_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == 'r' and computer_choice == 's') or \
         (player_choice == 's' and computer_choice == 'p') or \
         (player_choice == 'p' and computer_choice == 'r'):
        print("You win!")
    else:
        print("Computer wins!")

    # Ask for replay
    play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break
