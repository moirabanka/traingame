from sys import exit 
#at some point, move strings used for prompts into narration.py to be imported


#text printing functions
#def speak(text, speed):
#    #choose narration speed
#    if 'fast' in speed:
#        delay = .01
#    elif 'med' in speed:
#        delay = .05
#    elif 'slow' in speed:
    #     delay = .1
    # elif 'slower' in speed:
    #     delay = .25
    # elif 'slowest' in speed:
    #     delay = .5
    
    #not sure if this is good or not
#    for char in text:
#        sys.stdout.write(char)
#        sys.stdout.flush()
#        time.sleep(delay)

#this function handles starting a new game,
def start_game():
    from narration import help_text
    #eventually replace all instances of print with the speak() function
    print(help_text)
    saveload = input('\nWould you like to load a saved character? (y/n)\n')
    if 'y' in saveload:
        premade_character = input('\nEnter the name of the character to be loaded\n > ')
        load_character(premade_character)
    else:
        create_character()

def load_character(name):
    filename = name + '.txt'
    current_character = open(filename, 'a')
    print(current_character)


def create_character():
    from narration import backgrounds, background_info, savegame_format
    global name, background, status, location, inventory, current_character
    name = input("\nEnter your character's name\n > name:")
    background = None
    while background is None:
        print(backgrounds)
        background_choice = input("\nChoose your character's background.\nFor more detail, type 'info'\n > background:")
        if '1' or 'malcontent' in background_choice:
            background = 'malcontent'
        elif '2' or 'utilitarian' in background_choice:
            background = 'utilitarian'
        elif '3' or 'gourmond' in background_choice:
            background = 'gourmond'
        elif '4' or 'reactionary' in background_choice:
            background = 'reactionary'
        elif 'info' in background_choice:
            print(background_info)
        else:
            print('pleae try again')
    status = 'normal'
    location = 'car1'
    inventory = {}
    filename = name + '.txt'
    current_character = open(filename, 'w')
    current_character.write(savegame_format.format(name, background, status, location, inventory))
    start_turn()



    
    

        
    


def start_turn():
    print('this is a placeholder')

start_game()