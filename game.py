import time  # importing modules to pause the code temporary,
import random  # randomize tracks
import sys  # and exit the game


# this function pauses the code temporary to make it easier to read
# second parameter gives the ability to control pause time
def print_pause(text_to_print, pause_time):
    print(text_to_print)
    time.sleep(pause_time)


# separating the intro text in this function
def intro():
    print_pause("Loading...", 3)
    print_pause("Welcome to my adveture game", 2)
    print_pause("Ahmed Aboalasaad edition", 2)
    print_pause("Now, you are lost in a cold forest..", 2)
    print_pause("trying to find shelter to stay alive", 2)
    print_pause("and finally you find an abandoned city...", 2)
    print_pause("in front of you an abandoned palace ", 2)
    print_pause("and on your left a cottage", 2)


# a function contains choices and tracks in the palace
# with 3 parameters to guaranteed the data flow
def choose_in_palace(random_beast, items, beasts):
    print_pause("would you like to run ??", 1)
    print_pause("please Enter 'yes' or 'no'", 1)
    # usung .lower() to be sure of the input case
    run_or_face = input("--> ").lower()
    if run_or_face == 'yes':
        if random_beast == "Dragon":
            print_pause("you are right.. you can't face a dragon", 2)
            print_pause("getting out..", 2)
            out(items, beasts)
        elif random_beast == "ghost":
            print_pause("you are right.. you can't face a ghost", 2)
            print_pause("getting out..", 2)
            out(items, beasts)
        elif random_beast == "thief":
            print_pause("you Lose.. you should kill him", 2)
            print_pause("Game Over!", 2)
            again()

    elif run_or_face == 'no':
        if random_beast == "Dragon":
            print_pause("you Lose.. you can't face a dragon", 2)
            print_pause("Game Over!", 2)
            again()
        if random_beast == "ghost":
            print_pause("you Lose.. you can't face a ghost", 2)
            print_pause("Game Over!", 2)
            again()
        if random_beast == "thief":
            if 'knife' in items:
                print_pause("Eup, you can kill him with the knife", 2)
                print_pause("getting out..", 2)
                out(items, beasts)
            else:
                print_pause("you Lose.. you should kill him ", 2)
                print_pause("but you don't have a weapon", 2)
                print_pause("search in the cottage for one next time", 2)
                print_pause("Game Over!", 2)
                again()
    else:
        # to be sure of the taken input
        val_pal_inp(random_beast, run_or_face, 'yes', 'no', items, beasts)


# this one contains everything in the palace
def palace(items, beasts):
    # choosing a random Circumstance (beast)
    random_beast = random.choice(beasts)
    print_pause("getting into the palace..", 2)
    print_pause("I think I'm hearing a sound..", 2)
    print_pause("OMG .. It's a " + random_beast, 2)
    choose_in_palace(random_beast, items, beasts)


# this function contains everything in the cottage
def cottage(items, beasts):
    print_pause("getting in the cottage ..", 2)
    if "knife" not in items:
        print_pause("you found a knife and took it !!", 2)
        items.append("knife")
        print_pause("getting out of the cottage...", 2)
        out(items, beasts)
    else:
        print_pause("you have already come here and taken the stuff", 2)
        print_pause("there is nothing to do here", 2)
        print_pause("getting out of the cottage...", 2)
        out(items, beasts)


# this one validates the input for out() function
def validate_out_input(out_input, option1, option2, data_flow1, data_flow2):
    if out_input != option1 and out_input != option2:
        print_pause("Sorry, I don't understand you", 2)
        out(data_flow1, data_flow2)


# this one validates the input for again() function
def validate_again_input(again_input, option1, option2):
    if again_input != option1 and again_input != option2:
        print_pause("Sorry, I don't understand you", 2)
        again()


# this one validates the input for palace() function
# it's a little bit abbreviated to avoid the too long line error
def val_pal_inp(random_beast, palace_input, option1, option2, data1, data2):
    if palace_input != option1 and palace_input != option2:
        print_pause("Sorry, I don't understand you", 2)
        choose_in_palace(random_beast, data1, data2)


# this function contains everything out of the cottage and the palace
# and asks where to go next
def out(items, beasts):
    print_pause("Enter 1 to get into the palace ", 1)
    print_pause("Enter 2 to get into the cottage ", 1)
    # usung .lower() to be sure of the input case
    response = input("--> ").lower()
    if response == '1':
        palace(items, beasts)
    elif response == '2':
        cottage(items, beasts)
    else:
        # to be sure of the taken input
        validate_out_input(response, '1', '2', items, beasts)


# this one sets the lists to the default and starting the game from out
def action():
    items = []
    beasts = ["Dragon", "ghost", "thief"]
    out(items, beasts)


# this function is the most general one
# so that I can control the game with one function
def game():
    intro()
    action()


# and finally, the function which asks if the player want to play again or exit
def again():
    print_pause("would you like to play again ??", 1)
    print_pause("please Enter 'yes' or 'no'", 1)
    # usung .lower() to be sure of the input case
    play_again = input("--> ").lower()
    if play_again == 'yes':
        game()
    elif play_again == 'no':
        print_pause("ok .. goodbye!", 2)
        sys.exit()
    else:
        validate_again_input(play_again, 'yes', 'no')


game()
