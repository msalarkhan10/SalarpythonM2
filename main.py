import random
human_choice = input("Choose rock, paper or scissors: " )
print(human_choice)
human_score = 0
choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
print(computer_choice)
computer_score = 0
if human_choice == "rock":
    print("You chose rock")
    if computer_choice == "paper":
        print("Computer chose paper")
        print("You lost to a computer imagine")
        computer_score += 1
    elif computer_choice == "scissor":
        print("Computer chose scissors")
        print("Player won")
        human_score += 1
    else:
        print("Computer chose rock") 
        print("Its a tie")         