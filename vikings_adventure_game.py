import time
import random

from random import *

pause = 5

def print_pause (text_to_print, seconds):
    print(text_to_print)
    time.sleep(seconds)

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 in response:
            break
        elif option2 in response:
            break
        else:
            print_pause("The decision you entered is incorrect. " 
                        "Please enter a valid response.", pause - 2)
    return response

def intro():
    player_name = input("Welcome to The Siege of Pairs! " 
                        "Please enter your name as the "
                        "leader of the fearless Viking army. ")
    print_pause("The fate of Paris lies with, " + player_name + 
                ", the leader of the Vikings. "
                "The year is 845 and it's Easter Sunday... ", pause)
    print_pause("Sailing down the river Seine are 5,000 of your "
                "strongest warriors, waiting for orders.", pause)
    print_pause("A victory for your people means bringing home "
                "as many riches as possible from your raid.", pause )
    print_pause("On one hand, Paris has been unbreachable. "
                "It has the finest army and defenses you've ever seen.", pause - 2)
    print_pause("On the other... You stand with the largest army ever "
                "assembled in Viking history.", pause - 1)

def battle_decision():
    response = valid_input("Do you want to talk with the Frankish king or fight? "
                            "Please type 'talk' or 'fight'.\n", "talk", "fight")
    if "talk" in response:
        battle_talk()
    elif "fight" in response:
        battle_fight()

def battle_fight():
    print_pause("Your entire fleet continues to sail towards Paris.", pause - 2)
    print_pause("Your fleet finds a weakness in the city's defenses and "
                "your warriors begin destroying the city.", pause - 2)
    print_pause("The Frankish king, Charles the Bald, sees the devastation "
                "caused and offers to pay a ransom of 7,000 francs of silver and gold.", pause + 1)
    response = valid_input("Do you want to accept the king's offer? Please type 'y' or 'n'.\n", "y", "n")
    if "y" in response:
        print_pause("Your warriors agree that this ransom is fair.", pause - 2)
        print_pause("You and your people return home in victory, preparing "
                    "to attack Paris again in the future.", pause - 2)
        win_game()
    elif "n" in response:
        print_pause("Because you have denied the king's offer, you choose to set "
                    "up camp outside the city to return later to fight.", pause)
        print_pause("Over time, a plague infects your camp and your great army rapidly dies off.", pause)
        print_pause("You are left defenseless and the Frankish troops destroy what's left of your army.", pause)
        lose_game()

def battle_talk():
    print_pause("You and a select group of warriors sail to Paris flying a "
                "white flag to begin peaceful negotiations.", pause)
    print_pause("When you arrive you are greeted by the Frankish king, Charles the Bald.", pause)
    print_pause("Because it is a holy day, the king is willing to pay you a ransom. The ransom is...", pause - 1)
    print(randint(1, 2000)) 
    response = valid_input("Do you want to accept the king's offer? Please type 'y' or 'n'.\n", "y", "n")
    if "y" in response:
        print_pause("Your warriors do not agree with your decision. "
                    "Deep down they knew you could bring more riches back to the kingdom.", pause)
        print_pause("As you sail back to camp, the group of warriors surround you.", pause - 2)
        print_pause("You try to explain yourself, but alas!", pause - 3)
        print_pause("You feel a solider push you overboard.", pause - 3)
        lose_game()
    elif "n" in response:
        print_pause("Charles the Bald is extremely insulted that you denied his generous offer.", pause - 2)
        print_pause("You hear a horn blow!", pause - 4) 
        print_pause("Before you know it, a swarm of Frank soldiers surround you.", pause - 3) 
        print_pause("You blink and see a sword coming close to your chest...", pause - 3)
        lose_game()

def win_game():
    print_pause("CONGRATULATIONS! You will forever go down in history is the greatest Viking ruler!", pause - 2)
    response = valid_input("Would you like to play again? Please type 'y' or 'n'.\n", "y", "n")
    if "y" in response:
        intro()
    elif "n" in response:
        print_pause("Thank you for playing!", pause - 3)
        exit()

def lose_game():
    print_pause("Unfortunately you have let your people down.", pause - 2)
    print_pause("GAME OVER", pause - 3)
    response = valid_input("Would you like to play again? Please type 'y' or 'n'.\n", "y", "n")
    if "y" in response:
        while True:
            battle_decision()
    elif "n" in response:
        print_pause("Thank you for playing!", pause - 3)
        exit()

def play_game():
    intro()
    battle_decision()

play_game()
