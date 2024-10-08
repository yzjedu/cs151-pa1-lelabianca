# Programmers:  Leif LaBianca
# Course:  CS151, Professor Zee
# Due Date: October 9, 23:59
# Programming Assignment:  PA1
# Problem Statement:  This code has the user play a game about designing a piece of clothing to sell. Given a set of questions and user inputs, the code will determine the success of the product and what it ultimately sells for
# Data In: Type of clothing, count of specific detail on clothing, thickness of the clothing item, a "yes" or "no" input
# Data Out:  Price the clothing sold for and how much more their clothing item could have sold for
# Credits: All original code

# presets values to placeholder values
high_street_win = "blank"
chosen_clothing = "blank"
# sets variables to "no" so by default the while loops will
# continue looping unless another value is set
pass_thru1 = "no"
pass_thru2 = "no"
# explains game to user
print("Welcome to the fashion adventure game.\nYou will design either a jacket, pair of pants, or scarf.\nThe goal is to create a piece of clothing you think designers and customers will like.\nYou will get to see what your item sold for at the end.\n")
# requests the user select one of the three clothing options continuously until a valid input is detected
while pass_thru1 == "no":
    chosen_clothing = str.lower(input("Would you like to design a jacket, pants, or scarf? "))
    if chosen_clothing == "pants":
        print(f'You have chosen to design some {chosen_clothing}!\n')
        pass_thru1 = "yes"
    elif chosen_clothing == "scarf" or chosen_clothing == "jacket":
        print(f'You have chosen to design a {chosen_clothing}!\n')
        pass_thru1 = "yes"
    else:
        print("This value is not accepted. Please input 'jacket' 'pants' or 'scarf'\n")
# based on the input clothing item, the user is prompted with a variety of questions
# that will determine the outcome of the product. If the user input meets both criteria,
# it was a smash hit. If it met just one of the criteria, it did well. If it met neither, it did poorly
if chosen_clothing == "jacket":
    jacket_buttons = int(input("How many buttons will your jacket have? "))
    jacket_thickness = float(input("How thick will your jacket be in inches? "))
    if jacket_buttons <= 5 and jacket_thickness <= 2.0:
        print('Your jacket was a smash hit!\n')
        win_status = 'Full win'
    elif jacket_buttons <= 5 or jacket_thickness <= 2.0:
        print('Your jacket was pretty well liked, but it could be improved upon.\n')
        win_status = 'Half win'
    else:
        print('Your jacket did not do well and needs major adjustments.\n')
        win_status = 'Loss'
elif chosen_clothing == "pants":
    pants_pockets = int(input("How many pockets will your pants have? "))
    pants_thickness = float(input("How thick will your pants be in inches? "))
    if pants_pockets <= 4 and pants_thickness <= 0.5:
        print('Your pants were a smash hit!\n')
        win_status = 'Full win'
    elif pants_pockets <= 4 or pants_thickness <= 0.5:
        print('Your pants were pretty well liked, but they could be improved upon.\n')
        win_status = 'Half win'
    else:
        print('Your pants did not do well and need major adjustments.\n')
        win_status = 'Loss'
elif chosen_clothing == "scarf":
    scarf_threads = int(input("How many threads will your scarf be made of? "))
    scarf_thickness = float(input("How thick will your scarf be in inches? "))
    if scarf_threads >= 10 and scarf_thickness >= 1.0:
        print('Your scarf was a smash hit!\n')
        win_status = 'Full win'
    elif scarf_threads >= 10 or scarf_thickness >= 1.0:
        print('Your scarf were pretty well liked, but it could be improved upon.\n')
        win_status = 'Half win'
    else:
        print('Your scarf did not do well and needs major adjustments.\n')
        win_status = 'Loss'
# if the user met both criteria, the code prompts them on whether they wish to enter a high street
# fashion competition. If they enter, they win only if they meet both of the below criteria. Note that
# entrance is not mandatory to continue the game
if win_status == "Full win":
    while pass_thru2 == "no":
        high_street_query = str.lower(input(f"Your {chosen_clothing} qualified for a high street fashion contest!\nWould you like to enter your {chosen_clothing} to it? "))
        if high_street_query == "yes":
            pass_thru2 = "yes"
            if chosen_clothing == "jacket":
                if jacket_buttons == 3 and (jacket_thickness <= 2.0 and jacket_thickness >= 1.0):
                    print('Your jacket won the high street fashion contest!\n')
                    high_street_win = 'Win'
                else:
                    print('Sadly, your jacket did not win the high street fashion contest.\n')
                    high_street_win = 'Loss'
            elif chosen_clothing == "pants":
                if pants_pockets == 2 and (pants_thickness <= 0.25 and pants_thickness >= 0.1):
                    print('Your pants won the high street fashion contest!\n')
                    high_street_win = 'Win'
                else:
                    print('Sadly, your pants did not win the high street fashion contest.\n')
                    high_street_win = 'Loss'
            elif chosen_clothing == "scarf":
                if scarf_threads == 20 and (scarf_thickness <= 1.5 and scarf_thickness >= 1.0):
                    print('Your scarf won the high street fashion contest!\n')
                    high_street_win = 'Win'
                else:
                    print("Sadly, your scarf did not win the high street fashion contest.\n")
                    high_street_win = 'Loss'
        elif high_street_query == "no":
            pass_thru2 = "yes"
            print("Understood.\n")
        else:
            print("You did not enter a valid option. Please enter 'yes' or 'no'.\n" )
# determines the shelf price of the users design clothing item given the amount of criteria met. Note
# that if the user met both criteria and participated in the high street fashion competition, the
# price will raise with a win and lower with a loss as such
if win_status == "Full win":
    sell_price = 200
    if high_street_win == "Win":
        sell_price = sell_price + 100
    elif high_street_win == "Loss":
        sell_price = sell_price - 50
elif win_status == "Half win":
    sell_price = 100
elif win_status == "Loss":
    sell_price = 25
# prints the end shelf price and the distance they were from the maximum price, encouraging them to
# play again regardless of outcome
profit_potential = 300 - sell_price
print(f'Your {chosen_clothing} is now on the shelves for ${sell_price}!')
if sell_price < 300:
    print(f'Unfortunately, your {chosen_clothing} could have been sold for ${profit_potential} more.\nRun the program again to see if you can get the maximum price!')
else:
    print(f'Wow! You sold your {chosen_clothing} for the maximum price!\nCongratulations! Try to do it with other clothing options next time!')
