from sys import exit
import json

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
    from game_data import main_menu, help_text, intro, name_load_prompt, loaded_character, identity
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
    from game_data import backgrounds, background_info, name_prompt, background_prompt, default_worldstate
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
                      'anticipation': 0,
                      'worldstate': default_worldstate}
    with open(filename, 'w') as character_file:
        json.dump(character_info, character_file, indent=4)
    # loading the newly made save file into global variables and returning to the start_game() function
    load_character(filename)

# this function is loads a character file into global variables, preparing the character for play.
def load_character(file):
    global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation, worldstate
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
        worldstate = character_data['worldstate']
        
# saves current character values held in global variables to a file
def save_game(save_file):
    global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation, worldstate
    with open(save_file, 'w') as character_file:
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
                      'anticipation': anticipation,
                      'worldstate': worldstate}
        json.dump(character_info, character_file, indent=4)

# this function should be called into play whenever the character's stats are changed
# called in the 'resolve' function
# this can probably be refactored
def stat_change(stat, value):
    from game_data import stat_changed
    global joy, trust, fear, surprise, sadness, disgust, anger, anticipation
    match stat:
        case 'joy':
            joy = joy + value
            new_value = joy
        case 'trust':
            trust = trust + value
            new_value = trust
        case 'fear':
            fear = fear + value
            new_value = fear
        case 'surprise':
            surprise = surprise + value
            new_value = surprise
        case 'sadness':
            sadness = sadness + value
            new_value = sadness
        case 'disgust':
            disgust = disgust + value
            new_value = disgust
        case 'anger':
            anger = anger + value
            new_value = anger
        case 'anticipation':
            anticipation = anticipation + value
            new_value = anticipation
    if value >= 0:
        print(stat_changed.format(stat, 'increased', new_value))

# does this really need to be its own function?
def condition_change(environment, new_condition):
    global worldstate, location
    worldstate[location] = new_condition



# this function handles the process of the player turn.
# this should eventually be looped in a different function also handling threat turns

# this function now loops itself to account for incorrect input
def start_turn():
    from game_data import valid_targets, prompt
    global location, status, name, time_passed, current_turn
    while True:
        player_action = act()
        if player_action is True:
            resolve(player_action)
            break


# this function will handle asking for player input, checking its validity,
# and will pass a value to the 'resolve' function
# can now handle single word input and reset on empty input
def act():
    from game_data import prompt, invalid_command, invalid_target, too_many_words
    action = input(prompt)
    if action:
        interpreted_input = action.split()
        command = interpreted_input[0]
        command_validity = command_checker(command)
    else:
        command_validity = False
    if command_validity:
        match len(interpreted_input):
            case 1:
                target = 'other'
                return [command, target]
            case 2:
                target = interpreted_input[1]
                target_validity = target_checker(target)
                if target_validity:
                    return [command, target]
                else:
                    print(invalid_target)
                    return False
            # this needs to be written better, the whole game crashes if you input even more words.
            case _ if len(interpreted_input) > 2:
                print(too_many_words)
                return False
    else:
        print(invalid_command)
        return False



# function for checking if a user command is valid (returns True/False)
def command_checker(checked_command):
    from game_data import valid_commands
    if checked_command in valid_commands:
        return True
    else:
        from game_data import error
        print(error)
        return False


# function for checking if a target is valid (returns True/False)
def target_checker(checked_target):
    from game_data import valid_targets
    global location
    local_targets = valid_targets[location]
    if checked_target in local_targets:
        return True
    else:
        from game_data import error
        print(error)
        return False



# this function will take the validated command from the 'act' function,
# then it will retrieve all the player action's consequences and carry them out.
# the 'resolve' function will check if a condition is needed.
# if it is, check if the condition is fulfilled.
# if the condition is fulfilled or no condition is needed, retrieve the corresponding value in the form of a list.
# after retrieving the value, this function will check which flags are present, then carry out the indicated consequences.
# flags: N, SN, SC, location change, inventory change, condition change, check stat, check inventory, check knowledge, D

#CURRENT ISSUE: I NEED TO PASS THIS FUNCTION A LOCAL CONDITION FOR THE LOCATION THE PLAYER IS IN.
#HOW DOES THE PROGRAM DEcheck inventoryDE WHAT CONDITION IT NEEDS.
#   working compromise: only one local condition can be active at once.
#   the current local condition for each area can be stored in a global variable that holds the current worldstate
def resolve(player_input):
    if player_input != False:
        from game_data import narration_library, item_acquired, item_expended
        global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation, worldstate
        command = player_input[0]
        target = player_input[1]
        condition = worldstate[location]
        consequences = narration_library[location][command][target][status][condition]
        if 'narration' in consequences:
            print(consequences['narration'])
        if 'stat change' in consequences:
            stat = consequences['stat change'][0]
            value = consequences['stat change'][1]
            stat_change(stat, value)
        if 'location change' in consequences:
            location = consequences['location change']
        if 'inventory change' in consequences:
            if consequences['inventory change'][1]:
                inventory.append(consequences['inventory change'][0])
                print(item_acquired)
            else:
                inventory.remove(consequences['inventory change'][0])
                print(item_expended)
        if 'condition change' in consequences:
            target_location = consequences['condition change'][0]
            worldstate[target_location] = consequences['condition change'][1]
        # Need to work out how contextual narration works for checks to function
        if 'check stat' in consequences:
            worldstate[consequences['check stat'][2]] = check_stat(consequences['check stat'][0], consequences['check stat'][1])
        if 'check inventory' in consequences:
            worldstate[consequences['check inventory'][2]] = check_inventory(consequences['check inventory'][0], consequences['check inventory'][1])
        if 'check knowledge' in consequences:
            player_knowledge = input(consequences['check knowledge'][0])
            if player_knowledge == consequences['check knowledge'][1]:
                worldstate[consequences['check knowledge'][2]] = True
            else:
                worldstate[consequences['check knowledge'][2]] = False


# this function checks a stat and determines if it meets the DC
def check_stat(stat, dc):
    if stat >= dc:
        return True
    else:
        return False

# this function checks the inventory for an item
def check_inventory(item):
    global inventory
    if item in inventory:
        return True
    else:
        return False

        

start_game()
