import random
import time
from helper import *
def rock_paper_scissor():
    print("Welcome to the rock paper and scissors game")
    time.sleep(2)
    print(rocks)
    time.sleep(2)
    print(paper)
    time.sleep(2)
    print(scissors)
    time.sleep(2)
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
            print(rocks)
            time.sleep(1)
            if computer_choice == "paper":
                print(paper)
                time.sleep(1)
                print(loose)
                time.sleep(1)
                computer_score += 1
            elif computer_choice == "scissors":
                print(scissors)
                time.sleep(1)
                print(win)
                time.sleep(1)
                human_score += 1
            else:
                print(rocks)
                time.sleep(1) 
                print(tied)
                time.sleep(1)

        elif human_choice == "paper":
            print(paper)
            time.sleep(1)
            if computer_choice == "paper":
                print(paper)
                time.sleep(1)
                print(tied)
                time.sleep(1)
            elif computer_choice == "scissors":
                print(scissors)
                time.sleep(1)
                print(loose)
                time.sleep(1)
                computer_score += 1
            else:
                print(rocks)
                time.sleep(1)
                print(win)
                time.sleep(1)
                human_score += 1

        elif human_choice == "scissors":    
            print(paper)
            time.sleep(1)
            if computer_choice == "paper":
                print(paper)
                time.sleep(1)
                print(win)
                time.sleep(1)
                human_score += 1
            elif computer_choice == "scissors":
                print(scissors)
                time.sleep(1)
                print(tied)
                time.sleep(1)
            else:
                print(rocks)
                time.sleep(1)
                print(loose)
                time.sleep(1)
                computer_score += 1
        else:
            print("Incorecct response, try again")
        rounds -= 1
        print(score)
        time.sleep(1)
        print("Total computer score: ", computer_score)
        time.sleep(1)
        print("Total human score: ", human_score)
        time.sleep(1)
        print(round_break)
        time.sleep(1)
    print(bye)

rock_paper_scissor()