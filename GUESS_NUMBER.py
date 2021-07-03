from random import randint
from math import *

def computer_guess(limit_1,limit_2):
    return randint(limit_1,limit_2)

def user_guess(something):
  while True:
    try:
       u_guess = int(input(something))       
    except ValueError:
       print("Please enter an integer value")
       continue
    else:
       return u_guess
       break 
     

def play():
    score = 0
    game_set_limit = user_guess("How many times you wanna play ?")
    print("so,we're gonna play"+" "+str(game_set_limit)+" "+"sets\nif you win atleast"+" "+str(ceil((game_set_limit)/2)+1)+" " +"sets or more,you win the game")
    print("Remember,You have 3 chances to guess in each set :")
    
    for i in range(game_set_limit):
        lower = user_guess("Enter lower limit:")
        upper = user_guess("Enter upper limit:")
        if upper < (lower+12):
            upper = lower+12
            print("upper limit needs to be atleast 12 more than lower,\nso i chose it for you")
        print("So the limits are"+" "+str(lower)+" "+"and"+" "+str(upper)+":")
        computer_number = computer_guess(lower,upper)
        user_number = user_guess("Choose a number")
        guess_count = 0
        out_of_guesses = False
        guess_limit = 2
        
    
        while user_number != computer_number and not (out_of_guesses) :
            if guess_count < guess_limit:
                if user_number > upper or user_number < lower:
                    user_number = user_guess("Please choose a number between"+" "+str(lower)+" "+"and"+" "+ str(upper)+":")
                else:
                    if user_number > computer_number:
                        user_number = user_guess("your choice is larger,pick a smaller one:")
                        guess_count += 1
                    elif user_number < computer_number:
                        user_number = user_guess("your choice is smaller,pick a larger one:")
                        guess_count += 1
            else:
                out_of_guesses = True
        if out_of_guesses:
            score += 0
            print("sorry,you're out of guesses,we'll win next set...yay !")
        else:
            score += 1
            print("you guessed it right, yay !")
    
    if score > (game_set_limit)/2:
        print("Wow, .... You won this !")
    else:
        print("oh...sorry dear,you lost maximum sets,next time !")

play()

