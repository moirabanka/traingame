from sys import exit
import json


# this function handles starting the game, and checks if you want to load a save before starting the turn cycle
def start_game():
    from game_data import main_menu, help_text, intro, name_load_prompt, loaded_character, identity
    global name, status, background, location, worldstate
    menu_action = input(main_menu)
    match menu_action:
        case '1' | 'n' | 'new game':
            create_character()
            print(help_text)
            print(identity.format(name, status, background))
            context = intro['dining car']['dark']
            print(context.format(name))
            turn_cycle()
        case '2' | 'l' | 'load game':
            filename = input(name_load_prompt) + '.json'
            load_character(filename)
            print(loaded_character.format(name, status, background, location))
            condition = worldstate[location]
            context = intro[location][condition]
            print(context.format(name))
            turn_cycle()
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
                      'worldstate': default_worldstate,
                      'history':{},
                      'active goals':{},
                      'finished goals':{}
                      }
    with open(filename, 'w') as character_file:
        json.dump(character_info, character_file, indent=4)
    # loading the newly made save file into global variables and returning to the start_game() function
    load_character(filename)

# this function loads a character file into global variables, preparing the character for play.
def load_character(file):
    global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation, worldstate, history, active_goals, finished_goals
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
        history = character_data['history']
        active_goals = character_data['active goals']
        finished_goals = character_data['finished goals']
        
# saves current character values held in global variables to a file
def save_game(save_file):
    global name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation, worldstate, history, active_goals
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
                      'worldstate': worldstate,
                      'history': history,
                      'active goals':active_goals,
                      'finished goals':finished_goals}
        json.dump(character_info, character_file, indent=4)


# this function manages the overall continuity of ganeplay, looping until the player quits the game.
# eventually should also contain a time counter and ways to trigger events and possibly the actions of other characters
def turn_cycle():
    global time_elapsed
    time_elapsed = 0
    while True:
        start_turn()
        time_elapsed += 1



# this function handles the process of the player turn.
# this should eventually be looped in a different function also handling threat turns

# this function now loops itself to account for incorrect input
def start_turn():
    global location, status, name
    while True:
        player_action = act()
        if player_action:
            resolve(player_action)
            break


# this function will handle asking for player input, checking its validity,
# and will pass a value to the 'resolve' function
# can now handle single word input and reset on empty input

#some of this really needs to be partitioned off into other functions for cleanliness
def act():
    from game_data import prompt, invalid_command, invalid_target, too_many_words, command_aliases, target_aliases
    global location, command, target, joy, sadness, anger, fear, trust, disgust, surprise, anticipation, name, status, background, active_goals, finished_goals
    action = input(prompt)
    if len(action) != 0:
        interpreted_input = action.split()
        command = interpreted_input[0]
        if command in command_aliases:
            command = command_aliases[command]
        command_validity = command_checker(command)
    else:
        command_validity = 'invalid'
    if command_validity == 'valid':
        match len(interpreted_input):
            case 1:
                target = 'other'
                return [command, target]
            case 2:
                target = interpreted_input[1]
                if target in target_aliases[location]:
                    target = target_aliases[location][target]
                target_validity = target_checker(target)
                if target_validity is True:
                    return [command, target]
                else:
                    print(invalid_target)
                    return False
            case _ if len(interpreted_input) > 2:
                print(too_many_words)
                return False
    elif 'system' in command_validity:
        sys_command_handler(interpreted_input)
        return False                         
    else:
        print(invalid_command)
        return False



# this function will take the validated gameplay command from the 'act' function,
# then it will retrieve all the player action's consequences and carry them out.
# after retrieving the value, this function will check which flags are present, then carry out the indicated consequences.
# flags: narration, special narration, stat change, location change, inventory change, goals change
# condition change, check stat, check inventory, check knowledge, check history, game over

def resolve(player_input):
    if player_input != False:
        global command, target, name, background, status, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, anticipation, worldstate
        consequence_library = condition_handler(command, target)
        consequence_handler(consequence_library, False)




# UTILITY FUNCTIONS

# this function carries out the consequences contained in the consequence library it is supplied with.
# it now calls itself recursively when circumstances call for additional branching consequences.
#this should probably be broken into pieces to keep things visually simple
def consequence_handler(consequences, recursive_mode):
    from game_data import narration_library, item_acquired, item_expended
    global command, target, location, inventory, worldstate, active_goals, finished_goals
    if consequences == False:
        target = 'other'
        consequences = condition_handler(command, target)
    # History management
    if 'check history' in consequences:
        condition = worldstate[location]
        result = check_history([command, target, condition])
        if result:
            if len(consequences['check history']) > 1:
                consequence_handler(consequences['check history'][result], True)
                return
            elif len(consequences['check history']) == 1:
                consequence_handler(consequences['check history'][1], True)
                return
    if not recursive_mode:
        history_recorder([command, target])
    # Immediate consequences
    if 'narration' in consequences:
        print(consequences['narration'].format(name))
    if 'stat change' in consequences:
        stat = consequences['stat change']['stat']
        value = consequences['stat change']['value']
        stat_change(stat, value)
    if 'location change' in consequences:
        location = consequences['location change']
    if 'inventory change' in consequences:
        if consequences['inventory change']['add/subtract']:
            inventory.append(consequences['inventory change']['item'])
            print(item_acquired)
        else:
            inventory.remove(consequences['inventory change']['item'])
            print(item_expended)
    if 'condition change' in consequences:
        target_location = consequences['condition change']['target location']
        worldstate[target_location] = consequences['condition change']['new condition']
    # objective management
    if 'goal change' in consequences:
        from game_data import goal_change
        goal_name = consequences['goal change']['goal name']
        goal_progress = consequences['goal change']['progress']
        recorded_goal = {goal_name:goal_progress}
        # the logic here is not working quite right
        if goal_progress in ('completed', 'failed') and (goal_name not in finished_goals) and (goal_name in active_goals):
            finished_goals.update(recorded_goal)
            del active_goals[goal_name]
            print(goal_change[goal_progress].format(goal_name))
            if 'completed' in consequences['goal change'] or 'failed' in consequences['goal change']:
                consequence_handler(consequences['change goal'][goal_progress])
        elif goal_progress == 'in progress' and goal_name not in active_goals and goal_name not in finished_goals:
            active_goals.update(recorded_goal)
            print(goal_change[goal_progress].format(goal_name))
            if 'in progress' in consequences['goal change']:
                consequence_handler(consequences['goal change']['in progress'])
    # Checks
    if 'check consent' in consequences:
        player_yesno = check_consent(consequences['check consent']['prompt'])
        if player_yesno:
            consequence_handler(consequences['check consent']['yes'], True)
        else:
            consequence_handler(consequences['check consent']['no'], True)
    if 'check stat' in consequences:
        result = check_stat(consequences['check stat']['stat'], consequences['check stat']['dc'])
        if result:
            consequence_handler(consequences['check stat']['success'], True)
        else:
            consequence_handler(consequences['check stat']['failure'], True)
    if 'check inventory' in consequences:
        result = check_inventory(consequences['check inventory']['item'], True)
        if result:
            consequence_handler(consequences['check inventory']['success'], True)
        else:
            consequence_handler(consequences['check inventory']['failure'], True)
    if 'check knowledge' in consequences:
        result = check_knowledge(consequences['check knowledge']['prompt'], consequences['check knowledge']['answer'])
        if result:
            consequence_handler(consequences['check knowledge']['success'], True)
        else:
            consequence_handler(consequences['check knowledge']['failure'], True)

def sys_command_handler(player_input):
    global active_goals, finished_goals
    command = player_input[0]
    if len(player_input) == 2:
        arg_2 = player_input[1]
    else:
        arg_2 = False
    match command:
        case 'save':
            from game_data import saved_game
            filename = name + '.json'
            save_game(filename)
            print(saved_game)
            if arg_2 and ((arg_2 == 'quit') or (arg_2 == 'exit')):
                from game_data import quit_message
                print(quit_message)
                exit()
        case 'quit' | 'exit':
            from game_data import quit_message
            print(quit_message)
            exit()
        case 'status':
            from game_data import character_status, identity
            print(identity.format(name, status, background))
            print(character_status.format(joy, sadness, anger, fear, trust, disgust, surprise, anticipation))
        case 'help':
            if arg_2:
                from game_data import help_library
                match arg_2:
                    case 'commands':
                        from game_data import valid_commands, system_commands
                        print(help_library['commands'].format(', '.join(valid_commands), ', '.join(system_commands)))
                    case _:
                        print(help_library['_'])
            else:
                from game_data import help_text
                print(help_text)
        case 'goals':
            if not arg_2 and active_goals == {}:
                from game_data import no_active_goals
                print(no_active_goals)
            elif arg_2 == 'completed' and finished_goals =={}:
                from game_data import no_finished_goals
                print(no_finished_goals)
            else:
                if arg_2 and (arg_2 == 'completed'):
                    [print('\n' + f"    {key}: {value}") for key, value in finished_goals.items()]
                else:
                    [print('\n' + f"    {key}: {value}") for key, value in active_goals.items()]

    return False

# this function handles condition-agnostic consequences 
def condition_handler(current_command, current_target):
    from game_data import narration_library
    global location, status, worldstate
    condition = worldstate[location]
    condition_tree = narration_library[location][current_command][current_target][status]
    if len(condition_tree) is 1 and 'any' in condition_tree:
        return narration_library[location][current_command][current_target][status]['any']
    else:
        return narration_library[location][current_command][current_target][status][condition]

def history_recorder(event):
    global history, worldstate, location
    condition = worldstate[location]
    event.append(condition)
    recorded_event = ' '.join(event)
    if check_history(event):
        occurrences = history[recorded_event]
        occurrences += 1
    else:
        occurrences = 1
    history.update({recorded_event:occurrences})

def check_history(event):
    global history, worldstate, location
    checked_event = ' '.join(event)
    if checked_event in history and history[checked_event] >= 1:
        return history[checked_event]
    else:
        return False
    
# this can probably be refactored
def stat_change(stat, value):
    from game_data import stat_changed
    global joy, trust, fear, surprise, sadness, disgust, anger, anticipation, status
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
        case 'status':
            status = value
    match value:
        case int():
            if value >= 0:
                print(stat_changed.format(stat, 'increased', new_value))
            elif value <= 0:
                print(stat_changed.format(stat, 'decreased', new_value))
        case str():
            print(stat_changed.format(stat, 'changed', value))

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

# this function checks if the player wants to perform a subsequent action (Y/n)
def check_consent(prompt):
    while True:
        response = input(prompt)
        if 'y' in response:
            return True
        elif 'n' in response:
            return False
        else:
            from game_data import error
            print(error)
            continue

def check_knowledge(prompt, answer):
    from game_data import confirmation_prompt
    while True:
        response = input(prompt)
        confirmation = check_consent(confirmation_prompt)
        if confirmation:
            if response == answer:
                return True
            else:
                return False


# function for checking if a user command is a valid, invalid, or system command
def command_checker(checked_command):
    from game_data import valid_commands, system_commands
    if checked_command in valid_commands:
        return 'valid'
    elif checked_command in system_commands:
        return 'system'
    else:
        from game_data import error
        print(error)
        return 'invalid'


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


start_game()
