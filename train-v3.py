from sys import exit
import json

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

# this function handles starting the game, and checks if you want to load a save
def start_game():
    from narration import main_menu, help_text, intro, load_prompt, name_load_prompt, loaded_character, identity
    global name, status, background, location
    #eventually replace all instances of print with the speak() function
    menu_action = input(main_menu)
    match menu_action:
        case '1' | 'n' | 'new game':
            create_character()
            print(help_text)
            print(identity.format(name, status, background))
            print(intro.format(name))
            start_turn()
        case '2' | 'l' | 'load game':
            filename = input(name_load_prompt) + '.json'
            load_character(filename)
            print(loaded_character.format(name, status, background, location))
            start_turn()
        case '3' | 'q' | 'quit game':
            exit()
        

def create_character():
    from narration import backgrounds, background_info, name_prompt, background_prompt
    global name, background, filename

    # choosing your character's name and background
    name = input(name_prompt)
    background = None
    print(backgrounds)
    while background is None:
        background_choice = input(background_prompt)
        match background_choice:
            case '1' | 'malcontent':
                background = 'malcontent'
            case '2' | 'utilitarian':
                background = 'utilitarian'
            case '3' | 'gourmond':
                background = 'gourmond'
            case '4' | 'reactionary':
                background = 'reactionary'
            case 'info':
                print(background_info)
            case _:
                print('\nplease try again')

    # assembling a library of initial character data and dumping it to a .json file
    filename = name + '.json'
    character_info = {'name': name, 
                      'background': background, 
                      'status': 'normal', 
                      'location': 'dining car', 
                      'inventory': [],
                      'joy': 0,
                      'trust': 0,
                      'fear': 0,
                      'surprise': 0,
                      'sadness': 0,
                      'disgust': 0,
                      'anger': 0,
                      'anticipation': 0}
    with open(filename, 'w') as character_file:
        json.dump(character_info, character_file, indent=4)

    # loading the newly made save file into global variables and returning to the start_game() function
    load_character(filename)


# this function is now configured to ONLY load the character's saved state into global variables
# this no longer starts the game
def load_character(file):
    global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation
    with open(file) as character_file:
        character_data = json.load(character_file)
        name = character_data['name']
        background = character_data['background']
        status = character_data['status']
        location = character_data['location']
        inventory = character_data['inventory']
        joy = character_data['joy']
        trust = character_data['trust']
        fear = character_data['fear']
        surprise = character_data['surprise']
        sadness = character_data['sadness']
        disgust = character_data['disgust']
        anger = character_data['anger']
        anticipation = character_data['anticipation']
        


def save_game():
    global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation
    with open(filename, 'w') as character_file:
        character_info = {'name': name, 
                      'background': background, 
                      'status': status, 
                      'location': location, 
                      'inventory': inventory,
                      'joy': joy,
                      'trust': trust,
                      'fear': fear,
                      'surprise': surprise,
                      'sadness': sadness,
                      'disgust': disgust,
                      'anger': anger,
                      'anticipation': anticipation}
        json.dump(character_info, character_file, indent=4)

def emotion_change(emotion, value):
    global joy, trust, fear, surprise, sadness, disgust, anger, anticipation
    match emotion:
        case 'joy':
            joy = joy + value
        case 'trust':
            trust = trust + value
        case 'fear':
            fear = fear + value
        case 'surprise':
            surprise = surprise + value
        case 'sadness':
            sadness = sadness + value
        case 'disgust':
            disgust = disgust + value
        case 'anger':
            anger = anger + value
        case 'anticipation':
            anticipation = anticipation + value
    




def acquire(item):
    from narration import item_acquired
    inventory.append(item)
    print(item_acquired)




def start_turn():
    print('this is a placeholder')

start_game()
