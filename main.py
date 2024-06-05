import random  
# Import the random module to use for generating random choices

def update_score(outcome, scores):
    # Update the scores dictionary based on the outcome of the game
    if outcome == "You won!":
        scores["user"] += 1  # Increment user's score
    elif outcome == "You lost.":
        scores["computer"] += 1  # Increment computer's score

# Initialize the scores dictionary with initial scores
scores = {"user": 0, "computer": 0}

def print_score(scores):
    # Print the current scores
    print("Scoreboard:")
    print("You:", scores["user"])
    print("Computer:", scores["computer"])

while True:  # Start an infinite loop for the game
    items = ["rock", "paper", "scissors"]  # List of possible actions
    actions = random.choice(items)  # Randomly choose an action for the computer

    user = input("Enter your name: ")  # Get the user's name
    print("Welcome to Rock, Paper, Scissors, " + user + "!")  # Greet the user

    user2 = input("Select rock, paper, or scissors: ")  # Get the user's choice
    print('You chose ' + user2)  # Print the user's choice

    print("The computer chose " + actions)  # Print the computer's choice

    if actions == user2:
        print("It's a tie!")  # If both choices are the same, it's a tie
    elif (user2 == "rock" and actions == "scissors") or \
         (user2 == "paper" and actions == "rock") or \
         (user2 == "scissors" and actions == "paper"):
        outcome = "You won!"  # Determine if the user won
    else:
        outcome = "You lost."  # Determine if the user lost

    print(outcome)  # Print the outcome of the game
    update_score(outcome, scores)  # Update the scores based on the outcome
    print_score(scores)  # Print the updated scores

    play_again = input("Play again? (y/n): ")  # Ask the user if they want to play again
    if play_again.lower() != "y":
        break  # Exit the loop if the user does not want to play again