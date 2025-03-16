import random
def rock_paper_scissor():
    rounds = int(input("Enter the amount of rounds that you wish to play: "))
    human_score = 0
    computer_score = 0
    while rounds>0:
        human_choice = input("Choose rock, paper or scissors: " )
        print(human_choice)
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        print(computer_choice)
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

        elif human_choice == "paper":
            print("You chose paper")
            if computer_choice == "paper":
                print("Computer chose paper")
                print("Its a tie")
            elif computer_choice == "scissor":
                print("Computer chose scissors")
                print("You lost to a computer imagine")
                computer_score += 1
            else:
                print("Computer chose rock")
                print("Player won")
                human_score += 1

        elif human_choice == "scissors":
            print("You chose paper")
            if computer_choice == "paper":
                print("Computer chose paper")
                print("Player won")
                human_score += 1
            elif computer_choice == "scissors":
                print("Computer chose scissors")
                print("Its a tie")
            else:
                print("Computer chose rock")
                print("You lost to a computer imagine")
            computer_choice += 1
        else:
            print("Incorecct response, try again")
        rounds -= 1

rock_paper_scissor()