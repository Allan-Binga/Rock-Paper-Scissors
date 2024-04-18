#Rock, Paper, Scissors, Lizard, Spock game
# Feel free to run this on the command line.
import random

game_choices = ["rock", "paper", "scissors", "lizard", "spock"]
player = None
computer = random.choice(game_choices)

print("Let's play Rock, Paper, Scissors, Lizard, Spock")

player = input("Enter your choice:")

print(f"Computer chooses {computer}")

player = player.lower()

if player not in game_choices:
    print("Invalid choice. Please enter rock, paper, scissors, lizard or spock.")

if player == computer:
    
    print("It's a tie!")
    
elif player == "rock":
    if computer == "paper":
        print("Paper covers Rock! Computer wins!")
        
elif computer == "scissors":
    print("Rock crushes Scissors! You win!")
    
elif computer == "lizard":
    print("Rock crushes Lizard! You win!")          
    
elif computer == "spock":  
    print("Spock vaporizes Rock! Computer wins!")       
    
elif player == "paper":
    if computer == "scissors":
        print("Scissors cuts Paper! Computer wins!")
        
    elif computer == "rock":
        print("Paper covers Rock! Computer wins!")
        
    elif computer == "lizard":
        print("Lizard eats Paper! Computer wins")     
        
    elif computer == "spock":
        print("Paper disproves Spock. You win!")    
        
        #Checks and determines the value that the player inputs and returns the computer choice
elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts Paper! Computer wins!")
        
    elif computer == "rock":
        print("Rock crushes scissors! Computer wins!")
        
    elif computer == "lizard":
        print("Scissors decapitates Lizard! You win!")     
        
    elif computer == "spock":
        print("Spock smashes Scissors. Computer wins!")
              
    #Checks and determines the value that the player inputs and returns the computer choice.        
elif player == "lizard":
    if computer == "paper":
        print("Lizard eats Paper! You win!")
        
    elif computer == "rock":
        print("Rock crushes lizard! Computer wins!")
        
    elif computer == "scissors":
        print("Scissors decapitates Lizard! Computer wins")     
        
    elif computer == "spock":
        print("Lizard poisons Spock! You win!")  
     
     #Checks and determined the value that the player inputs and returns the computer choice.
elif player == "spock":
    if computer == "paper":
        print("Paper disproves Spock! Computer wins!")
        
    elif computer == "rock":
        print("Spock vaporizes Rock! You win!")
        
    elif computer == "scissors":
        print("Spock smashes Scissors. You win!")     
        
    elif computer == "lizard":
        print("Lizard poisons Spock! You win!")  
                
print("Thanks for playing!")        

#That's all : )
        
        