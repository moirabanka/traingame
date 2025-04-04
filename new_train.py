from sys import exit

# current major problem to be fixed: circular import issue
# the narrative file wants to pull the character name from this file,
# but this file is referencing the narration
# ???
# fixed!! (for now)

# maybe... I could insert the name into the narration using the .format() method on the narration string
# this would prevent variable names from this script being referenced in narration
# this was indeed the solution (for now)



# function for starting the game
# resets status, location, and name, and prints all introductory and help texts
def start():
    from narration import help_text, intro
    print(help_text)
    global status, name
    status = 'normal'
    name = input("Enter your character's name:\n> ")
    print(intro.format(name))
    car1()
     
# function for ending the game
# displays a given reason for death, the game over text, and asks if the player would like to try again
# if they do, run the start function. if they don't, exit the program without indicating an error
def die(why):
    from narration import game_over, error
    print(why)
    print(game_over[0].format(name))
    while True:
        try_again = input("> ")
        if "y" in try_again:
            start()
        elif "n" in try_again:
            print(game_over[1])
            exit(0)
        else:
            print(error)

def state_checker(checked_state, active_state, inactive_state):
    if checked_state == True:
        state_name = active_state
    elif checked_state == False:
        state_name = inactive_state
    else:
        exit(1)
    return state_name

# function for checking if a user command is valid
def command_checker(checked_command):
    valid_commands = ['touch', 'taste', 'sniff', 'look', 'listen', 'go']
    if checked_command not in valid_commands:
        from narration import error
        print(error)
        return False
    else:
        return True

# function for checking if a target is valid
def target_checker(checked_target):
    from narration import valid_targets
    local_targets = valid_targets[location]
    if checked_target not in local_targets:
        from narration import error
        print(error)
        return False
    else:
        return True

# function for interpreting user inputs, turning them from strings to lists
def interpreter():
    choice = input("> ")
    interpreted_input = choice.split()
    return interpreted_input

# function for interactions with targets with single outcomes
def simple_narrate(command, target):
    from narration import normal, wizard, cursed
    global location, name
    if status == 'normal':
        print(normal[location][command][target])
    elif status == 'wizard':
        wizard_script = wizard[location][command][target]
        print(wizard_script.format(name))
    elif status == 'cursed':
        print(cursed[location][command][target])
    else:
        #move this text and the other instance to error dictionary
        print("Unknown status! What in the hell's going on??")
        exit(1)

# function for governing interactions with targets that have multiple outcomes
def conditional_narrate(command, target, condition):
    from narration import normal, wizard, cursed
    global location, name
    if status == 'normal':
        print(normal[location][command][target][condition])
    elif status == 'wizard':
        wizard_script = wizard[location][command][target][condition]
        print(wizard_script.format(name))
    elif status == 'cursed':
        print(cursed[location][command][target][condition])
    else:
        print("Unknown status! What in the hell's going on??")
        exit(1)



# this is the function that contains all the special outcomes for interactions in car 1
# and serves narration for all interactions based on a number of conditions.
# Something about the simple narration is not functioning.
# for example, the command "touch blood" throws a typeerror, saying that lists are unhashable
# chatgpt says that this is occurring because I am trying to use a list as a dictionary key.
# chatgpt was right!!! using the .join() method on the list let me turn it back into a string, which could be used as a key

# New problem: getting a typeerror when trying to access wizard narration.
# apparently some list is being indexed with a string instead of an integer
# however, after reassigning status to wizard, it printed the narration for wizard touch tome

# Now it's breaking even earlier!
# break upon transformation into wizard.
# "IndexError: Replacement index 1 out of range for positional args tuple"
# it's because of how i tried to format the wizard narration
# nope, same problem
# the problem was actually that i was importing strings of wizard narration that had multiple placeholders for the name
# but I was only giving .format() one parameter
# currently working around the problem (not fixed) by only ever using the character's name only once per string in wizard narration


def car1():
    global status, location
    location = 'car1'
    lights = False
    while location == 'car1':
        # player input parsing and failsafes
        # probably turn this into its own function somehow?
        terms = interpreter()
        if not len(terms) == 0:
            command = terms.pop(0)
        else:
            continue

        if not command_checker(command):
            continue
        
        if len(terms) == 0:
            target = 'other'
        else:
            target = "".join(terms)

        #context dependent narration and multiple input narration

        # something is going on here that isn't good, causing the wrong narration to be displayed
        # for some reason, the variable {target} seems to always return as 'blood'
        # this is why using 'look' by itself was returning a type error
        # because it is not possible to look at the blood in the dark
        # Fixed!!

        if (command == 'touch' or command == 'taste') and 'switch' in target:
            if status == 'wizard':
                lights = False
            else:
                lights = not lights

        if 'surfaces'  in target or 'puddle' in target:
            target = 'blood'

        if 'items' in target:
            target = 'tables'
        
        if command == 'touch' and ('tome' in target or 'thing' in target) and status == 'normal':
            if target == 'thing':
                target = 'tome'
            conditional_narrate(command, target, "influence")
            check = input('> ')
            if check == 'xoglfotz':
                conditional_narrate(command, target, 'success')
                status = 'wizard'
                continue
            else:
                conditional_narrate(command, target, 'failure')
                status = 'cursed'
                continue
        elif command == 'touch' and status == 'cursed':
            from narration import cursed
            print(cursed['car1']['touch']['other'].format(target))
            continue

        # now that the target has been transformed, check if it's valid
        if not target_checker(target):
            continue

        # local area state dependent narration or universal narration
        if command == 'look' and status == 'normal':
            car1_state = state_checker(lights, 'light', 'dark')
            conditional_narrate(command, target, car1_state)
        else:
            simple_narrate(command, target)

def car0():
    pass

def car2():
    pass

#start()
# currently using the script to debug!
status = 'cursed'
name = 'Moira'
car1()
