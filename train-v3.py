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

#this function handles starting a new game,
def start_game():
    from narration import help_text
    #eventually replace all instances of print with the speak() function
    print(help_text)
    saveload = input('\nWould you like to load a saved character? (y/n)\n')
    if 'y' in saveload:
        premade_character = input('\nEnter the name of the character to be loaded\n > ') + '.json'
        load_character(premade_character)
    else:
        create_character()
        

def create_character():
    from narration import backgrounds, background_info
    global name, background, filename
    name = input("\nEnter your character's name\n > name: ")
    background = None
    while background is None:
        print(backgrounds)
        background_choice = input("\nChoose your character's background.\nFor more detail, type 'info'\n > background: ")
        if '1' in background_choice:
            background = 'malcontent'
        elif '2' in background_choice:
            background = 'utilitarian'
        elif '3' in background_choice:
            background = 'gourmond'
        elif '4' in background_choice:
            background = 'reactionary'
        elif 'info' in background_choice:
            print(background_info)
        else:
            print('please try again')
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
    load_character(filename)


def load_character(file):
    from narration import loaded_character
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
        print(loaded_character.format(name, status, background, location))
        start_turn()


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


def acquire(item):
    placeholder = True



    
    

        
    


def start_turn():
    print('this is a placeholder')

start_game()
