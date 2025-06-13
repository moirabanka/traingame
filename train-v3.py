from sys import exit
import json, textwrap, shutil, time, sys


# this function handles starting the game, and checks if you want to load a save before starting the turn cycle
def start_game():
    from game_data import main_menu, help_text, intro, name_load_prompt, loaded_character, identity
    global name, location, worldstate
    menu_action = input(main_menu)
    match menu_action:
        case '1' | 'n' | 'new game':
            create_character()
            print(help_text)
            context = intro['dining car']['dark']
            narrate(context.format(name))
            turn_cycle()
        case '2' | 'l' | 'load game':
            filename = input(name_load_prompt) + '.json'
            load_character(filename)
            narrate(loaded_character.format(name, location))
            condition = worldstate[location]
            context = intro[location][condition]
            narrate(context.format(name))
            turn_cycle()
        case '3' | 'q' | 'quit game':
            exit()
        

def create_character():
    from game_data import name_prompt, default_worldstate
    global name, filename
    name = input(name_prompt)
    # assembling a library of initial character data and dumping it to a .json file
    filename = name + '.json'
    character_info = {
        'name': name, 
        'location': 'dining car', 
        'inventory': [],
        'traits':[],
        'joy': 0,
        'trust': 0,
        'fear': 0,
        'surprise': 0,
        'sadness': 0,
        'disgust': 0,
        'anger': 0,
        'curiosity': 0,
        'confidence': 10,
        'clues':[],
        'mysteries':{},
        'worldstate': default_worldstate,
        'history':{}
    }
    with open(filename, 'w') as character_file:
        json.dump(character_info, character_file, indent=4)
    # loading the newly made save file into global variables and returning to the start_game() function
    load_character(filename)

# this function loads a character file into global variables, preparing the character for play.
def load_character(file):
    global name, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, curiosity, confidence, worldstate, history, traits, clues, mysteries
    with open(file) as character_file:
        character_data = json.load(character_file)
        name = character_data['name']
        location = character_data['location']
        inventory = character_data['inventory']
        traits = character_data['traits']
        joy = character_data['joy']
        trust = character_data['trust']
        fear = character_data['fear']
        surprise = character_data['surprise']
        sadness = character_data['sadness']
        disgust = character_data['disgust']
        anger = character_data['anger']
        curiosity = character_data['curiosity']
        confidence = character_data['confidence']
        clues = character_data['clues']
        mysteries = character_data['mysteries']
        worldstate = character_data['worldstate']
        history = character_data['history']
        
# saves current character values held in global variables to a file
def save_game(save_file):
    global name, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, curiosity, confidence, worldstate, history, traits, clues, mysteries
    with open(save_file, 'w') as character_file:
        character_info = {
            'name': name,
            'location': location, 
            'inventory': inventory,
            'traits': traits,
            'joy': joy,
            'trust': trust,
            'fear': fear,
            'surprise': surprise,
            'sadness': sadness,
            'disgust': disgust,
            'anger': anger,
            'curiosity': curiosity,
            'confidence': confidence,
            'clues': clues,
            'mysteries': mysteries,
            'worldstate': worldstate,
            'history': history
            }
        json.dump(character_info, character_file, indent=4)


# this function manages the overall continuity of gameplay, looping until the player quits the game.
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
    global location, name
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
    global location, command, target, joy, sadness, anger, fear, trust, disgust, surprise, curiosity, name
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
    elif 'mind palace' in command_validity:
        mind_palace_handler(interpreted_input)
        return False
    else:
        print(invalid_command)
        return False



# this function will take the validated gameplay command from the 'act' function,
# then it will retrieve all the player action's consequences and carry them out.
# after retrieving the value, this function will check which flags are present, then carry out the indicated consequences.
# flags: narration, stat change, location change, inventory change, goals change, clues change, mysteries change
# condition change, check stat, check inventory, check knowledge, check history, game over

def resolve(player_input):
    if player_input != False:
        global command, target, name, location, inventory, joy, trust, fear, surprise, sadness, disgust, anger, curiosity, worldstate
        consequence_library = condition_handler(command, target)
        consequence_handler(consequence_library, False)




# UTILITY FUNCTIONS

# this function carries out the consequences contained in the consequence library it is supplied with.
# it now calls itself recursively when circumstances call for additional branching consequences.
#this should probably be broken into pieces to keep things visually simple
def consequence_handler(consequences, recursive_mode):
    from game_data import narration_library, item_acquired, item_expended, mystery_change, mystery_library, clue_added, theory_unlocked, trait_acquired, trait_replaced
    global command, target, location, inventory, worldstate, mysteries, clues, traits
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
        narrate(consequences['narration'])
    if 'stat change' in consequences:
        stat = consequences['stat change']['stat']
        value = consequences['stat change']['value']
        stat_change(stat, value)
    if 'location change' in consequences:
        location = consequences['location change']
    # I want to add code that provides different pickup narration for different items
    if 'inventory change' in consequences:
        if consequences['inventory change']['add/subtract']:
            inventory.append(consequences['inventory change']['item'])
            narrate(item_acquired)
        else:
            inventory.remove(consequences['inventory change']['item'])
            narrate(item_expended)
    if 'trait change' in consequences:
        trait_name = consequences['trait change']['trait']
        replaces = consequences['trait change']['replaces']
        if replaces == None:
            traits.append(consequences['trait change']['trait'])
            narrate(trait_acquired.format(trait_name))
        elif replaces is True:
            traits.remove(replaces)
            traits.append(trait_name)
            narrate(trait_replaced.format(trait_name, replaces))
    if 'condition change' in consequences:
        target_location = consequences['condition change']['target location']
        worldstate[target_location] = consequences['condition change']['new condition']
    if 'mystery change' in consequences:
        mystery_name = consequences['mystery change']['name']
        mystery_progress = consequences['mystery change']['new progress']
        if mystery_name not in mysteries:
            preunlocked_theories = []
            for clue in clues:
                if clue in mystery_library[mystery_name]['decisive evidence']:
                    quick_solved = True
                else:
                    quick_solved = False
                for theory, related_clues in mystery_library[mystery_name]['theories'].items():
                    if clue in related_clues:
                        preunlocked_theories.append(theory)
            if quick_solved:
                mystery_progress = 'solved'
                narrate(mystery_change['solved'].format(mystery_name))
            else:
                narrate(mystery_change['new mystery acquired'].format(mystery_name))
            recorded_mystery = {mystery_name:{'current progress':mystery_progress, 'unlocked theories':preunlocked_theories, 'hunch': 'none'}}
            mysteries.update(recorded_mystery)
        elif mystery_name in mysteries and mysteries[mystery_name]['current progress'] == 'solved':
            pass
    if 'clue change' in consequences:
        clue_name = consequences['clue change']
        if clue_name not in clues:
            clues.append(clue_name)
            narrate(clue_added.format(clue_name))
            for mystery in mysteries:
                theories = mystery_library[mystery]['theories']
                for theory, theory_contents in theories.items():
                    if clue_name in theory_contents['supporting clues'] and theory not in mysteries[mystery]['unlocked theories']:
                        mysteries[mystery]['unlocked theories'].append(theory)
                        narrate(theory_unlocked.format(theory, mystery))
                if clue_name in mystery_library[mystery]['decisive evidence']:
                    mysteries[mystery]['current progress'] = 'solved'
                    narrate(mystery_change['solved'].format(mystery))
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
    global mysteries
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
            narrate(saved_game)
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
            print(identity.format(name))
            print(character_status.format(joy, sadness, anger, fear, disgust, trust, surprise, curiosity))
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
    return False

# this is kinda messy
def mind_palace_handler(player_input):
    from game_data import mind_palace_prompt, hunch, hunch_prompt, current_hunch, preexisting_hunch, theory_header, no_theories_unlocked, arg_2_invalid, arg_2_NaN, outside_range, select_header, no_active_mysteries, mystery_format, mystery_header, mystery_library, no_solved_mysteries, invalid_command
    global mysteries, clues
    command = player_input[0]
    if len(player_input) == 2:
        arg_2 = player_input[1]
    else:
        arg_2 = False
    match command:
        case 'mysteries':
            if mysteries == {}:
                print(no_active_mysteries)
            else:
                mystery_label = 1
                print(mystery_header.format('Unsolved'))
                for mystery in mysteries:
                    print(mystery_format.format(mystery_label, ')  ', mystery))
                    mystery_label += 1
        case 'solved':
            solved_mysteries = []
            for mystery, mystery_contents in mysteries.items():
                if mystery_contents['current progress'] == 'solved':
                    solved_mysteries.append(mystery)
            if solved_mysteries == []:
                print(no_solved_mysteries)
            else:
                print(mystery_header.format('Solved'))
                for mystery in solved_mysteries:
                    print(mystery_format.format('', '-', mystery))
        case 'select' if arg_2:
            try:
                arg_2 = int(arg_2)
            except:
                print(arg_2_NaN)
            if type(arg_2) == int and arg_2 <= len(mysteries):
                arg_2 -= 1
                mystery_index = list(mysteries)
                selection = mystery_index[arg_2]
                print(select_header.format(selection))
                if mysteries[selection]['hunch'] != 'none':
                    print(current_hunch.format(mysteries[selection]['hunch']))
                theory_label = 1
                if len(mysteries[selection]['unlocked theories']) == 0:
                    print(no_theories_unlocked.format(selection))
                else:
                    print(theory_header, end='')
                for theory in mysteries[selection]['unlocked theories']:
                    print(mystery_format.format(theory_label, ')  ', theory), end='')
                    theory_label += 1
                    clue_list = []
                    print('        Supporting clues: ', end='')
                    for clue in clues:
                        if clue in mystery_library[selection]['theories'][theory]['supporting clues']:
                            clue_list.append(clue)
                    clue_list = ', '.join(clue_list)
                    print(clue_list)
                    clue_list = []
                    print('\n', end='')
                while True:
                    mp_action = input(mind_palace_prompt.format(selection)).split()
                    mp_command = mp_action[0]
                    if len(mp_action) > 1:
                        mp_arg_2 = mp_action[1]
                    else:
                        mp_arg_2 = False
                    match mp_command:
                        case 'info':
                            #eventually make a longer description and/or a journal/log
                            narrate(mystery_library[selection]['description'])
                        case 'quit' | 'exit' | 'q' | 'x' | 'back':
                            break
                        case 'commit' |'hunch' if mp_arg_2:
                            try:
                                mp_arg_2 = int(mp_arg_2)
                            except:
                                print(arg_2_NaN)
                            if mysteries[selection]['hunch'] == 'none' and type(mp_arg_2) == int:
                                mp_arg_2 -= 1
                                mp_selection = mysteries[selection]['unlocked theories'][mp_arg_2]
                                formatted_prompt = hunch_prompt.format(mp_selection)
                                if check_consent(formatted_prompt):
                                    print(hunch.format(mp_selection, selection))
                                    mysteries[selection]['hunch'] = mp_selection
                            elif mysteries[selection]['hunch'] != 'none':
                                print(preexisting_hunch.format(mysteries[selection]['hunch']))
                            elif mp_arg_2 > len(mysteries[selection]['unlocked theories']):
                                print(outside_range.format(mp_arg_2, 1, len(mysteries[selection]['unlocked theories'])))
                            elif len(mysteries[selection]['unlocked theories']) == 0:
                                print(no_theories_unlocked.format(selection))
                        case _:
                            print(invalid_command)

def slow_print(input_text):
    for character in input_text:
        sys.stdout.write(character)
        sys.stdout.flush()
        match character:
            case ',' | '.' | '!' | '?' |';':
                time.sleep(.2)
            case ' ':
                continue
            case _:
                time.sleep(.025)

def wait_for_keypress(prompt="    (Press any key to continue)"):
    print(prompt, end='', flush=True)
    if sys.platform.startswith('win'):
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
        msvcrt.getch()
    else:
        import termios, tty
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        termios.tcflush(fd, termios.tcgetattr(fd))
        # this try/finally probably is not necessary and can be simplified
        try:
            tty.setraw(fd)
            sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def narrate(narration_object):
    terminal_width = shutil.get_terminal_size(fallback = 70).columns
    if terminal_width >= 74: 
        terminal_width = 70
    else:
        terminal_width -= 4
    if type(narration_object) == str:
        narration_object = {1:narration_object}
    for sequence, text in narration_object.items():
        formatted_narration = textwrap.fill(
            text,
            width=terminal_width,
            initial_indent='       ',
            subsequent_indent='    ',
            replace_whitespace=True,
            drop_whitespace=True,
            break_long_words=False,
            break_on_hyphens=False
        )
        if sequence == 1:
            print('\n', end='')
            slow_print(formatted_narration)
            print('\n')
        else:
            sys.stdout.write('\r' + '                               ' + '\r')
            sys.stdout.flush()
            slow_print(formatted_narration)
            print('\n')
        if int(sequence) < len(narration_object):
            wait_for_keypress()


# this function handles condition-agnostic consequences 
def condition_handler(current_command, current_target):
    from game_data import narration_library
    global location, worldstate
    condition = worldstate[location]
    condition_tree = narration_library[location][current_command][current_target]
    if len(condition_tree) == 1 and 'any' in condition_tree:
        return narration_library[location][current_command][current_target]['any']
    else:
        return narration_library[location][current_command][current_target][condition]

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
    global joy, trust, fear, surprise, sadness, disgust, anger, curiosity, confidence
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
        case 'curiosity':
            curiosity = curiosity + value
            new_value = curiosity
        case 'confidence': 
            confidence += value
            new_value = confidence
    match value:
        case int():
            if value > 0:
                narrate(stat_changed.format('+', value, stat, 'increased', new_value))
            elif value < 0:
                narrate(stat_changed.format('-', value, stat, 'decreased', new_value))

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
def check_consent(proposed_action):
    from game_data import prompt
    while True:
        response = input(proposed_action+ prompt)
        if 'y' in response:
            return True
        elif 'n' in response:
            return False
        else:
            from game_data import error
            print(error)
            continue

def check_knowledge(question, answer):
    from game_data import confirmation_prompt, prompt
    while True:
        response = input(question + prompt)
        confirmation = check_consent(confirmation_prompt)
        if confirmation:
            if response == answer:
                return True
            else:
                return False


# function for checking if a user command is a valid, invalid, or system command
def command_checker(checked_command):
    from game_data import valid_commands, system_commands, mind_palace_commands
    if checked_command in valid_commands:
        return 'valid'
    elif checked_command in system_commands:
        return 'system'
    elif checked_command in mind_palace_commands:
        return 'mind palace'
    else:
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
