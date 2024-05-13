import random

def update_score(outcome, scores):
  if outcome == "You won!":
    scores["user"] += 1
  elif outcome == "You lost.":
    scores["computer"] += 1

scores = {"user": 0, "computer": 0}

def print_score(scores):
  print("Scoreboard:")
  print("You:", scores["user"])
  print("Computer:", scores["computer"])

while True:
  items = ["rock", "paper", "scissors"]
  actions = random.choice(items)

  user = input("enter your name: ")

  print("Welcome to Rock, Paper, Scissors, " + user + "!")

  user2 = input("select rock, paper, or scissors: ")

  print('you chose ' + user2)

  print("The computer chose " + actions)

  if actions == user2:
    print("It's a tie!")
  elif (user2 == "rock" and actions == "scissors") or \
     (user2 == "paper" and actions == "rock") or \
     (user2 == "scissors" and actions == "paper"):
    outcome = ("You won!")
  else:
    outcome = ("You lost.")
    
    print(outcome)
    update_score(outcome, scores)
    print_score(scores)
  


  
  
  play_again = input("play again? (y/n): ")
  if play_again.lower() !="y":
    break



          