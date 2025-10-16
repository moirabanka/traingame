main_menu = r"""


                  Welcome to...

      ______   _      _____    ______    ______
     / /  \_\ | |    / / \ \  | |__) \  | |__) \
    ( (  ____ | |   ( (   ) ) |  _  _/  |  ____/
     \ \__/ / | |___ \ \_/ /  | | \ \   | |
      \____/  |____/  \___/   |_|  \_\  |_|

      
       1) New game
       2) Load game
       3) Quit

 > """

invalid_command= """
    This is not a recognized command.
"""

invalid_target= """
    This is not a valid target.
"""

too_many_words = """
    Your command has too many terms!
    A valid command should only have two terms.
    E.G: 'sniff glue' or 'get item'
"""

load_prompt = """
    Would you like to load a saved character? (y/n)

 > """

name_load_prompt = """
    Enter the name of the character to be loaded.

 > """


name_prompt = """
    Enter your character's name.

 > """

background_prompt = """
    Choose your character's background.
    For more detail, type 'info'

 > """

confirmation_prompt = """
    Are you sure?
    (y/n)

 > """

help_text = """
    ------------------------------------------------
    
    The basic commands:
        "touch", "taste", "sniff", "look", and "listen"

    Use the basic commands to perceive your environment with your character's senses.
    Either type them on their own, or add a target if you want to examine it in particular.
    Valid targets will be written in CAPITALIZED TEXT.

    (E.G: the command 'look window' will instruct your character to look at the window, but
    the command 'look' by itself causes your character to observe their overall environment)

    
    System commands:
        "save", "exit", "help", and "status"

    You can also use the command "help _" to list the topics that can be queried for more info.

    ------------------------------------------------
"""

mind_palace_help_text = """
    ------------------------------------------------
    
    You are now in your mind palace. Use the command 'exit' to resume normal gameplay.
    Here, you can see the mysteries you are solving as well as the clues you have acquired so far.

    Clues can be assigned to open mysteries by using the 'add' command.
    Mysteries' titles must be typed out in full within quotes or referenced by number.
    Use syntax: add [clue] to "[mystery]"
    (E.G: add "blood" to "Who died?")

    You can also request information on any clue or mystery by using the 'info' command.
    use syntax: info [clue or mystery]

    Mind palace commands:
        "add", "remove", "info", "help" and "exit"

    Mind palace commands may also be used from normal gameplay without entering this mode.
    To do this, from normal gameplay prefix a mind palace command with 'mp'
    (E.G: mp add "blood" to "Who died?")

    ------------------------------------------------
"""

help_library = {
    '_':"""
    You can request help on the following topics:
    
    commands: displays all currently available commands
    targets: displays all currently targetable entities

    Example syntax:
        'help targets' 
    """,
    'commands':"""
    Game commands:
        {}
    
    System commands:
        {}
"""
}

prompt = """
 > """

mind_palace_prompt = """
 {}: """

identity = """
You are playing as {}, a master sleuth.
"""

intro = {
    'dining car': {
        'dark':"""
{} is standing in a darkened train car.
The carriage bumps and rattles.
What do you do?
    """,
        'light':"""
{} is standing in the dining car.
The walls are covered in blood.
The carriage bumps and rattles.
What do you do?
    """
    }
}

loaded_character = """
{} is currently located in the {}.
"""

stat_changed = """
{}{} {} ({} to {})
"""

item_acquired = """
You pocket the {}
"""

item_expended = """
{} removed from inventory
"""
trait_acquired = """
Added "{}" to traits
"""

trait_replaced = """
New trait "{}" replaces "{}"
"""
valid_commands = ['touch', 'taste', 'sniff', 'look', 'listen', 'go', 'get']

command_aliases = {
    'feel':'touch',
    'lick':'taste',
    'smell':'sniff',
    'see':'look',
    'hear':'listen'
}

system_commands = ['save', 'quit', 'exit', 'status', 'help',]

mind_palace_commands = ['mysteries', 'solved', 'select']

character_status = """
    joy........... {}      sadness....... {}
    anger......... {}      fear.......... {}
    disgust....... {}      trust......... {}
    surprise...... {}      curiosity..... {}
"""

default_worldstate = {
    'dining car': 'dark'
}


error = """
    Invalid entry! please try again
    """

saved_game= """
Game saved successfully!
"""

game_over = ["""
    {} cannot continue like this.
    Try again? (Y/n)
""", """
    Thanks for playing!
"""]

quit_message = """
    Thanks for playing!
"""

mystery_change = {
    'new mystery acquired':"""
"{}" has been added to your mysteries.
    """,
    'next step':"""
    {} advanced to {}
    """,
    'solved':"""
You solved "{}"
    """,
    'failed':"""
"{}" is no longer solvable!
    """
}

no_active_mysteries = """
    You do not have any active mysteries!
"""

no_solved_mysteries = """
    You haven't solved any mysteries yet!
"""
mystery_header = """
    {} mysteries:"""

select_header = """
    Mystery selected: "{}\""""

mystery_format = """
    {}{} "{}"
"""

arg_2_invalid = """
    Second argument "{}" is invalid.
    It should be a {}.
"""

outside_range = """
    Input {} is outside of expected range {} to {}
"""

arg_2_NaN = """
    Second argument must be a number.
"""

no_theories_unlocked = """    No theories unlocked for "{}"
"""

theory_header = """
    Theories:"""

hunch_prompt = """
    Are you sure you want to hunch {} theory? (Y/n)

 > """

hunch = """
Developing a hunch on {} theory for "{}"...
"""

preexisting_hunch = """
    You have already developed a hunch for {} theory.
"""

current_hunch = """    Current hunch: {} theory"""

clue_added = """
Added "{}" to clues.
"""

continue_prompt = """(enter) to continue..."""

theory_unlocked = """
Unlocked "{}" theory for "{}"
"""
# should be changed to:
# valid_targets[location][environment_state][target]
valid_targets = {
    'dining car': ['switch', 'blood', 'food', 'tables', 'tome', 'door1', 'door2', 'window', 'other']
    }

target_aliases = {
    'dining car':{
        'lightswitch':'switch',
        'puddles':'blood',
        'thing': 'tome',
        'stuff': 'food'

    }
}


mystery_library = {
    'Where am I?':{
            'description': """
You've awoken to darkness. 
What is this place?
    """,
            'theories':{
                'room': {
                    'description':"""
You are standing within a room, possibly contained within a larger building.
    """,
                    'supporting clues': ['tables', 'walls'],
                    'validity': False
                },
                'train':{
                    'description':"""
You are standing within a train car, most likely connected to others.
    """,
                    'supporting clues': ['Locomotion', 'Clunking sound'],
                    'validity': True
                }
            },
            'decisive evidence':['moved between cars']
    },
    'Whose blood is this?':{
            'description': """
You found quite a lot of blood where you woke up, but no bodies.
Whose could it have been?
    """,
            'theories':{
                'It\'s my blood': {
                    'description':"""
Could this blood be... Mine?
But I'm not injured. How could this be?
    """,
                    'supporting clues': ['bullet holes in blood-soaked clothing', 'coworker\'s testimony'],
                    'validity': True
                },
                'An unknown person\'s blood': {
                    'description': """
I awoke uninjured.
This blood must belong to someone I haven't encountered yet.
Could they still be alive after losing this much?
    """,
                    'supporting clues': ['no bodies present', 'lack of injuries'],
                    'validity': False
                }
            }
    }
}

# narration tree has been reorganized on the following principles:
# player actions will result in consequences, which will take several forms:
# narration:'', stat change:{stat, value}, location change:'', inventory change:{item, T/F})condition change:{target location, new condition}
# mystery change: {name, new progress}, clue change: clue name
# trait change: {'trait':'', 'replaces':'' or None, 'silent':T/F}
# check stat:{stat, dc, check name, success, failure}, check inventory:{item, success, failure},
# check knowledge:{prompt, answer, success, failure}, check consent:{prompt, yes:{}, no:{}}
# special consequences:{trigger:{consequence sublibrary}}, Death:'reason'
# not every action will have every type of consequence, so types of consequences should be checked for by flag
# condition-agnostic consequences are marked with 'any', and target-agnostic consequences return False

new_game = {
    'narration':{
        1:"""
You open your eyes to darkness.
Lying half on your side, half on your stomach, your cheek is pressed into what seems to be dirty carpet.
    """,
        2:"""
Last you knew, you were attending a fabulous masquerade thrown in the honor of the now-late Lord Borthwick.
You feigned the fear and anger felt by the rest of the onlookers who witnessed his wretched poisoning, but you were grinning heartily behind your mask.
    """,
        3:"""
There was a culprit to be caught. A mystery to be solved. A case to be cracked.
His Lordship wasn't much to your liking anyway. Pompous old fool...
    """,
        4:"""
But it's all gone now, and you don't know where.
    """,
        5:"""
Every few seconds, a tremor passes through the floor just strong enough to lift your head slightly and smack it down into the carpet again.
You stand up before the next one comes, rubbing at the stippled pattern pressed into your face by your uncomfortable resting position.
Perhaps some mysteries may yet be found here...
    """,
        6:"""
Where the hell are you, anyway?
"""},
    'mystery change':{
        'name': 'Where am I?',
        'new progress': 'in progress'
    },
    'check consent':{
        'prompt': """
Faced with a fresh mystery, you try to recall your sleuthing skills...
Would you care for a tutorial? (Y/n)
""",
        'yes':{
            'narration':{
                1:"""
As the finest investigator in all the Nine Territories, your sleuthing skills are your life's blood. They are your very essence.
There is no prey more succulent than the hard-won truth at the dark, twisted heart of a case cracked wide open.
""",
                2:"""
The act of solving a mystery revitalizes you, granting you the CONFIDENCE to go on investigating.
Without your CONFIDENCE, you are nothing, and will flee from this realm a harried, tortured soul.
""",
                2:"""
Unsure of yourself and your unknown surroundings, your confidence is dangerously low. Drink, sire, from the wealth of your many senses.
Take in the world and let its secrets burst forth!
""",
                3:"""
* To investigate the world and gather clues, you must use one your five senses to TOUCH, TASTE, SMELL, HEAR, or LOOK at your environment.
You may use the command "help commands" to display all the commands available to you.
Try using the 'look' command now. (type 'look' and hit 'enter' to submit the command)
"""
            },
            'trait change':{
                'trait': 'tutorial',
                'replaces': None,
                'silent': True
            }
        },
        'no':{
            'narration':"""
Of course you don't, my liege. After all, you *are* the finest investigator in all the Nine Territories. Where were we...
""",
            'stat change':{'stat':'confidence', 'value': 1}
        }
    }

}
narration_library = {
    'dining car': {
        'touch': {
            'switch': {
                # 'myself': {
                #     'light':{
                #         'narration':""""""
                #     },
                #     'dark':{
                #         'narration':""""""
                #     }
                # },
                'light': {
                    'narration': 
                    """
You flip the light SWITCH!
The train car is flooded with darkness.
You can't see the blood anymore...
But if anything, that's even scarier!  
                    """,
                    'stat change':{'stat':'fear', 'value':1},
                    'condition change':{'target location':'dining car', 'new condition':'dark'},
                    'check history': {
                        1:{
                            'narration':"""
You flip the light SWITCH off again.
""",
                            'condition change':{'target location':'dining car', 'new condition':'dark'}
                        }
                    }
                },
                'dark': {
                    'narration': """
You find a light SWITCH!
You flick it on, bathing the train car in light.
There's blood everywhere, and I mean *everywhere*.
                    """,
                    'stat change':{'stat':'fear', 'value':2},
                    'condition change':{'target location':'dining car', 'new condition':'light'},
                    'check history': {
                        1:{
                            'narration':"""
You flip the light SWITCH on again.
""",
                            'condition change':{'target location':'dining car', 'new condition':'light'}
                        }
                    }
                }
            },
            'blood': {
                'any': {
                    'narration':"""
It's a viscous, dark fluid. Tacky in places, and partially dried.
It seems to be only a few hours old.
""",
                    'clue change': 'Fresh Blood'
                }
            },
            'food': {
                'any': {
                    'narration':{
                        1:"""
You sift through the plates of rotten FOOD...
""",
                        2:"""
Eventually, you have to face the truth. there's nothing edible here.
You accidentally poke your finger through the soft exterior of a decaying fruit.
Gross...
"""
                    },
                    'stat change':{'stat':'disgust', 'value': 1}
                }
            },
            'tables': {
                'any': {
                    'narration':{
                        1:"""
Expecting the texture of wood, you discover that the tables are constructed with wood-imitation plastic paneling.
It's incredibly tacky. You can't abide by this.
""",
                        2:"""
You feel a number of objects on the tables.
There is a large TOME bound in some sort of leather, and heaping plates of FOOD.
"""        
                    },
                    'stat change':{'stat': 'anger', 'value':1}
                }
            },
            'tome': {
                'any': {
                    'narration':"""
You grab the TOME.
It seems to compel you to open it...
            """,
                    'check consent':{
                        'prompt':"""
Are you sure you want to open the TOME? (Y/n)
""",
                        'yes':{
                            'narration':"""
Your fate is sealed.
""",
                            'check knowledge':{
                                'prompt':"""
Can you resist the TOME's influence?
""",
                                'answer':'xoglfotz',
                                'success':{
                                    'narration':{
                                        1:"""
You speak the TOME's word of power!
""",
                                        2:"""
The TOME has no more power over you. It goes limp in your hands.
Your skin begins to emit a very soft glow...
"""},
                                    'trait change':{'trait': 'mana-touched', 'replaces': None}
                                },
                                'failure':{
                                    'narration':{
                                        1:"""
You are unable to resist the TOME's influence!
""",
                                        2:"""
The TOME chills your hands, freezing them in place!
You can't tell if the book contains pictures or words, but the ink writhes ceaselessly...
"""},
                                    'trait change':{'trait': 'cursed', 'replaces': None}
                                }
                            }
                        },
                        'no':{
                            'narration':"""
You withdraw from the TOME.
"""
                        },
                    },
                }
# this narration remains untouched until it is integrated into the history check
    #             'wizard': {
    #                 'any':{
    #                     'narration':"""
    # {} picks up the tome. It hangs limply in their grasp, defeated.
    # They and the tome now share the source of their powers.
    # For one to hurt the other is to hurt themselves.
    #         """
    #                 }
    #             },
    #             'cursed': {
    #                 'any':{
    #                     'narration':"""
    # Yeah, you're doing that.
    # Can't stop doing that, actually.
    # Your hands are starting to go numb...
    #         """
    #                 }
    #         }
            },
            'door1': {
                'any': {
                    'narration':{
                        1: """
You feel all around the door.
It feels like a normal door on a train.
""",
                        2:"""
Nonetheless, you find yourself compelled by the allure of the unknown...
"""
                    },
                    'stat change': {'stat': 'curiosity', 'value': 1}
                }
            },
            'door2': {
                'any': {
                    'narration':"""
You feel all around the door.
The handle feels warm.
""",
                    'clue change': 'Warm doorhandle'
                }
            },
            'window': {
                'any': {
                    'narration':{
                        1:"""
You touch the glass of the window...
""",
                        2:"""
It's cool, like the night outside.
You feel the vibrations of the train car as it rattles along the rails.
        """
                    }
                }
            },
            'other': {
                'any': {
                    'narration':{
                        1:"""
Unsure of what you're looking for, you grope around the carriage...
""",
                        2:"""
On the walls and floor, you find a number of PUDDLES and damp surfaces, 
what seems to be a light SWITCH, and a number of TABLES laden with items.
You feel the cool glass of a WINDOW inset into each wall.
There are doors (DOOR1 and DOOR2) at the front and rear of the carriage.
"""
                    }
                }
            },
        },
        'taste': {
            'switch': {
                'light': {
                    'narration':"""
It's difficult, but after a few moments of fumbling, you manage to turn the light switch back off.
Darkness once more envelops the room, and the coppery taste of all the fingers that may have once flipped that switch envelops your taste buds.
""",
                    'stat change':{'stat':'disgust', 'value': 1},
                    'condition change':{'target location':'dining car', 'new condition':'dark'},
                    'check history': {
                        1:{
                            'narration':"""
You flip the light SWITCH off, once again using nothing but your tongue.
You're really getting quite good at this.
""",
                            'condition change':{'target location':'dining car', 'new condition':'dark'}
                        }
                    }
                },
                'dark': {
                    'narration':{
                        1:"""
You lean in and lick the light SWITCH.
After a few seconds of fumbling, you manage to turn on the lights!""",
                        2:"""
That flavor, though...
You can't seem to get it to leave your taste buds.
"""
                    },
                    'stat change':{'stat':'disgust', 'value': 1},
                    'condition change':{'target location':'dining car', 'new condition':'light'},
                    'check history': {
                        1:{
                            'narration':"""
You flip the light SWITCH on again, using only your tongue.
You're discovering a real talent here.
""",
                            'condition change':{'target location':'dining car', 'new condition':'light'}
                        }
                    }
                }
            },
            'blood': {
                'any': {
                    'narration':"""
It tastes metallic...
Yep, that's definitely BLOOD.
"""
                }
            },
            'food': {
                'any': {
                    'narration':{
                        1:"""
You attempt to peel a rotting banana before you eat it,
but the stem sloughs off in your grasp.
""",
                        2:"""
You take a small bite, peel and all.
You feel gross...
"""
                    },
                    'stat change':{'stat':'disgust', 'value': 3}
                }
            },
            'tables': {
                'any': {
                    'narration':"""
The imitation-wood vinyl turns your stomach.
The nearby rotting FOOD doesnt help, either...
""",
                    'stat change':{'stat': 'disgust', 'value':1}
                }
            },
            'tome': {
                'any': {
                    'narration':{
                        1:"""
You lick the tome...
Ouch! You got a papercut on your tongue!
""",
                        2:"""
The blood seeps into the tome's pages, quickly disappearing before your eyes...
A word of power whispers itself into your mind...
""",
                        3:"""

"XOGLFOTZ"
"""
                    },
                    'stat change':{'stat':'fear', 'value':2}
                }
            },
            'door1': {
                'any': {
                    'narration':{
                        1:"""
Ouch! You get a huge splinter in your tongue!
""",
                        2:"""
However, the sliver is so big you kinda look like one of those cool guys with toothpicks.
You decide to keep it.
"""
                    },
                    'stat change':{'stat':'confidence', 'value':1}
                }
            },
            'door2': {
                'any': {
                    'narration':"""
Yep, it tastes like door.
"""
                }
            },
            'window': {
                'any': {
                    'narration':{
                        1:"""
You put your mouth on the window, breathing out to cause your cheeks to inflate.
""",
                        2:"""
If any four-year-olds were on the other side of the glass, they'd be cracking up.
Kinda unsanitary, though...
"""
                    }
                }
            },
            'other': {
                'any': {
                    'narration':"""
You lick the wall.
It tastes like BLOOD.
"""
                }
            },
        },
        'sniff': {
            'switch': {
                'any': False
            },
            'blood': {
                'any': {
                    'narration':"""
A metallic, rich aroma fills your nostrils...
Yep, that smells like BLOOD, alright.
"""
                }
            },
            'food': {
                'any': {
                    'narration':"""
You lean in to one of the platters and take a deep whiff...
You detect notes of rotting fruits and meats.
""",
                    'stat change':{'stat':'disgust', 'value':1}
                }
# I want this cursed narration to be preserved
    #             'cursed': {
    #                 'any':{
    #                     'narration':"""
    # You lean in to one of the platters and take a deep whiff...
    # The smell of the rotting food entices you as if it were a free breakfast buffet.
    #         """
    #                 }
    #         }
            },
            'tables': {
                'any': {
                    'narration':"""
The smell of rot and death fills your nostrils.
You stop smelling it before it makes you retch.
""",
                    'stat change':{'stat':'disgust', 'value':2}
                }
            },
            'tome': {
                'any': {
                    'narration':{
                        1:"""
It smells like death.
You reflexively gag and recoil away.
""",
                        2:"""
Despite everything, somehow the TOME seems... tasty.
"""
                    },
                    'stat change':{'stat':'curiosity', 'value':2}
                }
            },
            'door1': {
                'any': {
                    'narration':{
                        1:"""
The air wafting through the door smells like static electricity and ozone.
The hair stands up on the back of your neck.
""",
                        2:"""
You're not sure what that means...
"""
                    }
                }
            },
            'door2': {
                'any': {
                    'narration':"""
Smells smokey.
Damn, you could really go for some marshmallows right now.
"""
                }
            },
            'window': {
                'any': False 
            },
            'other': {
                'any': {
                    'narration':{
                        1:"""
You take a few good whiffs...
The coppery scent of BLOOD hits your nostrils, followed by the smell of rotten FOOD.
""",
                        2:"""
The train car is ripe with odors most foul.
"""
                    }
                }
            },
        },
        'look': {
            'switch': {
                'light': {
                    'narration':"""
It's a light SWITCH, toggled on.
You toggled it not long ago.
"""
                },
                'dark': False
            },
            'blood': {
                'light': {
                    'narration':{
                        1:"""
Smears and spatters of BLOOD cover the inside of the train car.
It seems to be drying, but still somewhat fresh.
""",
                        2:"""
Gleams of bright crimson reside among the flaking rusty brown.
""",
                        3:"""
... Whose blood is this, anyway?
"""
                    }
                },
                'dark': False
            },
            'food': {
                'light': {
                    'narration':"""
Plates piled high with spoiled fruit and moldy bread are spread throughout the room.
The flies are having a goddamn field day...
"""
                },
                'dark': False
            },
            'tables': {
                'light': {
                    'narration':{
                        1:"""
You see five circular TABLES. On them sits many platters of rotten FOOD.
""",
                        2:"""
Also present on the table is what seems to be an ancient TOME.
It looks quite valuable...
"""
                    }
                },
                'dark': {
                    'narration':{
                        1:"""
You see the silhoutte of TABLES laden with STUFF.
""",
                        2:"""
There is also a squarish THING sitting on one of the TABLES.
Too dark to make out what it is...
"""
                    }
                }
            },
            'tome': {
                'light': {
                    'narration':{
                        1:"""
You look over the tome, an ornate book bound in a pale leather.
A variety of symbols and patterns are embossed in precious metals on the cover.
""",
                        2:"""
The symbols are striking, but hardly anything you recognize.
It's quite a striking volume. Clearly, potent secrets reside within.
""",
                        3:"""
For some strange reason, it seems rather tasty...
"""
                    }
                },
                'dark': False
# Keep this narration for a trait check
    #             'wizard': {
    #                 'any':{
    #                     'narration':"""
    # {} looks over the tome, an ornate book bound in human skin.
    # It exudes magic from the same source as your own...
    # They kind of feel like they are bathing in their own sweat.
    #         """
    #                 }
    #             }
            },
            'door1': {
                'light': {
                    'narration':{
                        1:"""
The curtain is drawn on the other side of the door's window.
What seems to be a breeze disturbs it now and then, revealing nothing but darkness.
""",
                        2:"""
Next to the door is a sign that reads: 'To Ultra-Luxe Sleeper Car'
"""
                    }
                },
                'dark': False
            },
            'door2': {
                'light': {
                    'narration':{
                        1:"""
This door's window is covered with a large piece of plywood.
It seems someone doesn't want people going back there...
""",
                        2:"""
Next to the door is a sign that reads: 'To Kitchen Car'
"""
                    },
                    'stat change':{'stat': 'curiosity', 'value':1}
                },
                'dark': False
            },
            'window': {
                'light': {
                    'narration':{
                        1:"""
You look out the window...
But it's too bright in the train car to see anything outside!
""",
                        2:"""
Instead, you see yourself standing in your bloody surroundings.
You look disheveled and displeased.
""",
                        3:"""
You tidy yourself up as much as you can, but your clothing is riddled with holes and bloodstains.
"""
                    },
                    'trait change':{'trait':'Tidied Up', 'replaces': None, 'silent': False}
                },
                'dark': {
                    'narration':{
                        1:"""
You look out the window...
""",
                        2:"""
A wide, flat expanse of cracked soil whizzes past the window at great speed, lit only by the faint light of dusk.
The sky is clear -- both moonless and starless, and neither any structures nor signs of life can be seen outside.
You have a feeling it's going to be a long night.
"""
                    },
                    'clue change':'Locomotion',
                    'check trait':{
                        'trait':'tutorial',
                        'success':{
                            'narration':{
                                1:"""
For a sleuth such as yourself, to gather clues is to breathe, and you have taken your first breath since you have awoken here.
While it is only a pale imitation of the rejuvenating force experienced when solving mysteries, it will tide you over until that moment comes.
""",
                                2:"""
Clues may briefly slake your ravenous thirst for CONFIDENCE, sire, but only solving mysteries
and developing shrewd hunches will allow you to restore it to your usual state of contained megolomania.
""",
                                3:"""
The hunch is a key component in the life of an investigator, my liege, especially one as dependent on self esteem and appearances as yourself.
When your CONFIDENCE is waning and decisive evidence is not yet clasped in your eager hands, developing a hunch can provide temporary CONFIDENCE points,
protecting your fragile ego. However, if your hunch is proven wrong, your CONFIDENCE will be duly penalized.
"""
                            },
                            'stat change':{'stat':'confidence', 'value':1}
                        },
                        'failure':None
                    }
                }
            },
            'other': {
                'light': {
                    'narration':{
                        1:"""
You look around...
The train car is covered in smears and streaks of BLOOD.
Tacky, partially drying PUDDLES of the stuff are scattered across the floor.
Despite the obvious carnage that took place here, there doesn't seem to be any bodies present.
""",
                        2:"""
This seems to be a dining car, the walls lined with TABLES that hold a variety of items.
Platters of rotten FOOD are arrayed throughout the car, an unpleasant tableau of decay and death.
""",
                        3:"""
There is a WINDOW on each side of the carriage, made mirror-like by to the brightness inside the train car.
There are also two doors, (DOOR1 and DOOR2) to the front and rear of the train car, respectively.
""",
                        4:"""
On the wall is the light SWITCH, toggled on.
The lights flicker as the train clatters over the rough rails, but they hold.
"""
                    }
                },
                'dark': {
                    'narration':{
                        1:"""
It's too dark to see any detail, but there seem to be some TABLES around.
You can also see a large bay WINDOW in each of the two longest walls.
The faint light of dusk filters through, only a shade brighter than the darkness around you.
""",
                        2:"""
Maybe you can find some way to turn on the lights...
"""
                    },
                    'check trait': {
                        'trait':'tutorial',
                        'success':{
                            'narration': {
                                1:"""
Sire, it has come to my attention that your CONFIDENCE is dangerously low. You simply cannot continue like this for long.
I suggest you scour your environment for clues. They will help you to sustain your CONFIDENCE, keeping your connection to this realm from weakening.
""",
                                2:"""
* Commands can also be used with a target to focus your senses on a specific thing to inspect it for clues.
Valid targets will be written in CAPITALIZED text in the narration, and will be only one word long.
Try using the "look" command targeting the window now. (type 'look window' and hit 'enter' to submit the command)
"""
                            }
                        },
                        'failure': None}
                }
            },
        },
        'listen': {
            'switch': {
                'any': False
            },
            'blood': {
                'any': {
                    'narration':{
                        1:"""
You imagine the BLOOD gurgling softly.
It whispers to you...
""",
                        2:"""
"I was once in the veins of a guy named Abrahand Lickin'. Hell of a thing, ain't it?"
"""
                    }
                }
            },
            'food': {
                'any': {
                    'narration':"""
You hear the buzzing of the flies overhead.
There are a LOT of them.
"""
                }
            },
            'tables': {
                'any': {
                    'narration':"""
You hear the buzzing of the flies overhead.
There are a LOT of them.
"""
                }
            },
            'tome': {
                'any': {
                    'narration':"""
You hear otherworldly whispers emanating from the tome.
They say: "Warning! This tome is cursed!".
"""
                }
            },
            'door1': {
                'any': {
                    'narration':"""
You can't quite make it out, but you hear something rhythmic...
"""
                }
            },
            'door2': {
                'any': {
                    'narration':"""
No other sound comes from the rear car but the clattering of the rails.
        """
                }
            },
            'window': {
                'any':{
                    'narration':"""
You cup your ear against the window.
Maybe you hear a bird outside. 
I don't know, it's hard to tell.
"""
                }
            },
            'other': {
                'any': {
                    'narration':"""
You listen to the intermittent clunk of the train passing over the rough railway.
You seem to be traveling quite fast, in excess of 90 miles per hour.
"""
                }
            },
        },
        'go': {
            'door1':[],
            'door2':[]
        }

    }
}
