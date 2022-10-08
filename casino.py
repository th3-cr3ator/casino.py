import random
import math

#Lobby
print("Welcome to the 'Gold Casino And Resort' ")
print("Please enjoy your stay!")
print(" ")

while True:
    print('Choose a a game to play')
    print('Options: Slots, Craps, Roulette')
    game_choice = input(">>> ")

    #Exit
    if game_choice == "exit":
        break
    
    #Slots game
    if game_choice == "Slots":
        while True:
            
            #Code for the slots game
            one = random.randint(1, 5)
            two = random.randint(1, 5)
            three = random.randint(1, 5)
            print("|" + str(one) + "|" + str(two) + "|" + str(three) + "|")
            if one == two == three == 1:
                print("You won $100")
                print("You made a profit of $75")
            if one == two == three == 2:
                print("You won $200")
                print("You made a profit of $175")
            if one == two == three == 3:
                print("You won $300")
                print("You made a profit of $275")
            if one == two == three == 4:
                print("You won $400")
                print("You made a profit of $375")
            if one == two == three == 5:
                print("You won $500")
                print("You made a profit of $475")
            else:
                print("You lost $25")
            
            #Code for a retry function
            print("Want to play again?")
            retry_slots = input(">>> ")
            if retry_slots == "yes":
                continue
            if retry_slots == "no":
                break
            
    #craps game
    if game_choice == "Craps":
        while True:
            
            #Code for craps game
            craps_bet = input("Place a bet: ")
            craps_nr = input("Choose a number: ")
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1, 6)
            dice_number = first_dice + second_dice
            print("The numbers were: " + str(first_dice) + " and " + str(second_dice))
            if dice_number == craps_nr:
                print("You won" + craps_bet)
            if dice_number != craps_nr:
                print("You lost" + craps_bet)
            
            #Code for retry function    
            print("Want to play again?")
            retry_slots = input(">>> ")
            if retry_slots == "yes":
                continue
            if retry_slots == "no":
                break
            
    #Roulette game
    if game_choice == "Roulette":
        while True:
            
            #Code for roulette game
            roulette_bet = input("Place a bet: ")
            print("Choose what you will bet on")
            print("Colour or number")
            bet_choice = input(">>> ")
            if bet_choice == "Colour":
                print("Which colour?")
                print("Black or red")
                colour_bet = input(">>> ")
                colour = random.randint(1, 2)
                if colour == 1:
                    print("It was black")
                if colour == 2:
                    print("It was red")
                if colour == 1 and colour_bet == "Black":
                    print("You won " + roulette_bet)
                elif colour == 1 and colour_bet != "Black":
                    print("You lost " + roulette_bet)
                elif colour == 2 and colour_bet == "Red":
                    print("You won " + roulette_bet)
                elif colour == 2 and colour_bet != "Red":
                    print("You lost " + roulette_bet)
            if bet_choice == "Number":
                print("What number between 0 and 36")
                number_bet = input(">>> ")
                number = random.randint(0, 36)
                print("The number was " + str(number))
                if number_bet == number:
                    print("You won " + roulette_bet)
                else:
                    print("You lost " + roulette_bet)        
                        
            #Code for retry function    
            print("Want to play again?")
            retry_slots = input(">>> ")
            if retry_slots == "yes":
                continue
            if retry_slots == "no":
                break
                        
                