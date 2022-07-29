#!/usr/bin/env python
# coding: utf-8


import random 

user_wins = 0
computer_wins = 0
choices  = ["rock","paper","scissors"]

while True:
    user_input = input("Welcome to Rock, Paper, Scissors! Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
        
    if user_input not in choices:
        print("Please select a valid choice!")
        continue 
        
    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_guess = choices[random_number]
    print("Computer chooses", computer_guess + "!")
    
    if user_input == "rock" and computer_guess == "scissors":
        print("YOU WIN! YOU GET A POINT")
        user_wins += 1 
        
    elif user_input == "paper" and computer_guess == "rock":
        print("YOU WIN! YOU GET A POINT")
        user_wins += 1
        
    elif user_input == "scissors" and computer_guess == "paper":
        print("YOU WIN! YOU GET A POINT")
        user_wins += 1
    
    else:
        print("YOU LOST! COMPUTER GETS A POINT!")
        computer_wins += 1
        
print("You won", user_wins, "times.")
print("computer has won", computer_wins, "times.")
print("Goodbye!")


