main_menu = r"""


                  Welcome to...

      ______    _____    ______    ______
     / /  \_\  / / \ \  | |__) \  | |__) \
    ( (  ____ ( (   ) ) |  _  _/  |  ____/
     \ \__/ /  \ \_/ /  | | \ \   | |
      \____/    \___/   |_|  \_\  |_|

      
       1) New game
       2) Load game
       3) Quit

> """


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
help_text = """
------------------------------------------------
Call on your character's five senses to help you understand the environment!

sinmply type one of these commands:
    "touch", "taste", "sniff", "look", or "listen"
If you call on one of your senses, the game will ask if you'd like to use it on anything in particular.
CAPITALIZED text shows an object or character can be interacted with. Type them in lowercase if you'd like to use them.
if you don't want to interact with a specific thing, just press RETURN.

However, keep in mind that it may affect your character.
You may not always like what you find...

To move between areas, simply type the  of the exit you wish to use.

There are also other hidden commands...

Good luck!
------------------------------------------------

"""
identity = """
    You are playing as {}, a {} {}.
"""

intro = """
    {} is standing in a darkened train car.
    The carriage bumps and rattles.
    What do you do?
"""

backgrounds = """
    1) Malcontent
    2) Utilitarian
    3) Gourmond
    4) Reactionary
"""

background_info = """
INSERT DETAIL ON BACKGROUNDS HERE
"""

loaded_character = """
    {} is a {} {}, currently located in the {}.
"""

item_acquired = """
    {} pockets {}
"""


error = "\nInvalid entry! please try again.\n"

game_over = ["""
    {} cannot continue like this.
    Try again? (Y/n)
""", """
    Thanks for playing!
"""]


state_change = {
    'normal':"""

""",
    'wizard':"""

""",
    'cursed':"""

"""
}

valid_targets = {
    'dining_car': ['switch', 'light switch', 'blood', 'food', 'tables', 'tome', 'door1', 'door2', 'window', 'other']
    }


normal = {
    "dining car": {
        "touch": {
            "switch":"""
    You find a LIGHT SWITCH!
    You flick it on, bathing the train car in light.
    There's blood everywhere, and I mean *everywhere*.
            """,
            "blood":"""
    It's a viscous, dark fluid. Tacky in places, and partially dried.
            """,
            "food":"""
    You sift through the plates of rotten FOOD...
    Eventually, you have to face the truth. there's nothing edible here.
    You accidentally poke your finger through the soft exterior of a decaying fruit.
    Gross...
            """,
            "tables":"""
    You feel a number of objects here.
    Some sort of squarish THING, and what seems to be heaping plates of FOOD
            """,
            "tome":{
                "influence":"""
    You grab the TOME.
    It seems to compel you to open it...
    Can you resist its influence?
                """,
                "success":"""
    You speak the TOME's word of power!
    The TOME has no more power over you. It goes limp in your hands.
    Your skin begins to emit a soft glow...
                """,
                "failure":"""
    You are unable to resist the TOME's influence!
    The TOME chills your hands, freezing them in place!
    You can't tell if the book contains pictures or words, but the ink writhes ceaselessly...
            """},
            "door1":"""
    You feel all around the door.
    It feels like a normal door on a train.
            """,
            "door2":"""
    You feel all around the door.
    It feels like a normal door on a train.
            """,
            "window":"""
    You touch the glass of the window.
    It's cool, like the night outside.
    You feel the vibrations of the train car as it rattles along the rails.
            """,
            "other":"""
    Unsure of what you're looking for, you grope around the carriage.
    On the walls and floor, you find a number of PUDDLES and WET SURFACES, 
    what seems to be a LIGHT SWITCH, and a number of TABLES laden with ITEMS.
    You feel the cool glass of a WINDOW inset into each wall.
    There are doors (DOOR 1 and DOOR 2) at the front and rear of the carriage.
            """
        },
        "taste": {
            "switch":"""
    You lean in and lick the LIGHT SWITCH.
    After a few seconds of fumbling, you manage to turn on the lights!
            """,
            "blood":"""
    It tastes metallic...
    Yep, that's definitely BLOOD.
            """,
            "food":"""
    You attempt to peel a rotting banana before you eat it,
    but the stem sloughs off in your grasp.
    You take a small bite, peel and all.
    You feel gross...
            """,
            "tables":"""
    Ouch! You get a huge splinter in your tongue!
    However, the sliver is so big you kinda look like one of those cool guys with toothpicks.
    You decide to keep it.
            """,
            "tome":"""
    You lick the tome...
    Ouch! You got a papercut on your tongue!
    The blood seeps into the tome's pages, quickly disappearing before your eyes...
    A word of power whispers itself into your mind...
    "XOGLFOTZ"
            """,
            "door1":"""
    Yep, it tastes like door.
            """,
            "door2":"""
    Yep, it tastes like door.
            """,
            "window":"""
    You put your mouth on the window, breathing out to cause your cheeks to inflate.
    If any four-year-olds were on the other side of the glass, they'd be cracking up.
    Kinda unsanitary, though...
            """,
            "other":"""
    You lick the wall.
    It tastes like BLOOD.
            """
        },
        "sniff": {
            "switch":"""
    That doesn't smell like anything.
            """,
            "blood":"""
    A metallic, rich aroma...
    Yep, that smells like BLOOD.
            """,
            "food":"""
    You lean in to one of the platters and take a deep whiff...
    You detect notes of rotting fruits and meats.
            """,
            "tables":"""
    The smell of rot and death fills your nostrils.
    You stop smelling it before it makes you retch.
            """,
            "tome":"""
    It smells like death.
    You reflexively gag and recoil away.
            """,
            "door1":"""
    The air wafting through the door smells like static electricity and ozone.
    The hair stands up on the back of your neck.
    You're not sure what that means...
            """,
            "door2":"""
    That doesn't smell like anything.
            """,
            "window":"""
    That doesn't smell like anything.
            """,
            "other":"""
    You take a few good whiffs...
    The coppery scent of BLOOD hits your nostrils, followed by the smell of rotten FOOD.
            """
        },
        "look": {
            "switch": """
    It's a LIGHT SWITCH, toggled on.
    You toggled it not long ago.
            """,
            "blood":"""
    Smears and spatters of blood cover the inside of the train car.
    It seems to be drying, but still somewhat fresh.
    Gleams of bright crimson reside among the flaking rusty brown
            """,
            "food":"""
    Plates piled high with spoiled fruit and moldy bread are spread throughout the room.
    The flies are having a goddamn field day...
            """,
            "tables":{
                'light':"""
    You see five circular tables. On them sits many platters of rotten FOOD.
    Also present on the table is what seems to be an ancient TOME.
    It looks quite valuable...
                """,
                'dark':"""
    You see the silhoutte of TABLES laden with ITEMS.
    Too dark to make out what the ITEMS are...
                """
            },
            "tome":"""
    You look over the tome, an ornate book bound in a pale leather.
    A variety of symbols and patterns are embossed in precious metals on the cover.
    The symbols are striking, but hardly anything you recognize.
    It's quite a striking volume. Clearly, potent secrets reside within.
    For some strange reason, it seems rather tasty...
            """,
            "door1":"""
    The curtain is drawn on the other side of the door's window.
    What seems to be a breeze disturbs it now and then, revealing nothing but darkness.
""",
            "door2":"""
    This door's window is covered with a large piece of plywood.
    It seems someone doesn't want people going back there...
""",
            "window":{
                'light':"""
    You look out the window...
    But it's too bright in the train car to see anything outside!
    Instead, you see yourself standing in your bloody surroundings.
    You look disheveled and displeased.
                """,
                'dark':"""
    You look out the window...
    The silhouettes of trees whiz past the dark sky.
    The moon hangs overhead, Its meager sliver casting a slight silvery glow.
    Beyond the rattling of the rails beneath the carriage, all is quiet.
    You feel like it's going to be a long night.
                """
            },
            "other": {
                'light':"""
    You look around...
    The train car is covered in smears and streaks of BLOOD.
    Tacky, partially drying PUDDLES of the stuff are scattered across the floor.
    Despite the obvious carnage that took place here, there doesn't seem to be any bodies.
    This seems to be a dining car, the walls lined with TABLES that hold a variety of ITEMS.
    Platters of rotten FOOD are arrayed throughout the car, an unpleasant tableau of decay and death.
    On the wall is the light SWITCH, toggled on.
    There is a WINDOW on each side of the carriage, made mirror-like by to the brightness inside the train car.
    There are two DOORs (DOOR1 and DOOR2) to the front and rear of the train car, respectively.
    The lights flicker as the train clatters over the rough rails, but they hold.
                """,
                'dark':"""
    It's too dark to see any detail, but there seem to be some TABLES around...
                """
            }
        },
        "listen": {
            "food":"""
    You hear the buzzing of the flies overhead.
    There are a LOT of them.
            """,
            "tables":"""
    You hear the buzzing of the flies overhead.
    There are a LOT of them.
            """,
            "tome":"""
    You hear otherworldly whispers enticing you.
    This books seems quite powerful.
    Perhaps that power can be yours...
            """,
            "door1":"""
    You can't quite make it out, but you hear something rhythmic...
            """,
            "door2":"""
    No other sound comes from the rear car but the clattering of the rails.
            """,
            "other":"""
    You listen to the intermittent clunk of the train passing over the rough railway.
    You seem to be traveling quite fast.
            """
        },
        "go": {
            "door1":"""

            """,
            "door2":"""

            """
        }
    }
}

wizard = {
    "car0": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    },
    "dining car": {
        "touch": {
            "switch":"""
    {} has no need for such contrivances of simpler beings.
    The luminousity of their skin should suffice.
            """,
            "blood":"""
    Somweone has left their life's blood behind.
    Too far degraded for any use. A pity...
            """,
            "food":"""
    {} refuses to touch the rotten food.
    Let the dead decompose in peace...
            """,
            "tables":"""
    The tables are constructed with plastic paneling printed to look like wood.
    It's incredibly tacky. {} is somewhaty insulted by your suggestion to touch it.
    Out of the overwhelming kindness of their heart, they forgive you.
            """,
            "tome":"""
    {} picks up the tome. It hangs limply in their grasp, defeated.
    They and the tome now share the source of their powers.
    For one to hurt the other is to hurt themselves.
            """,
            "door1":"""
    Behind this door lies something the likes of which {} has never perceived, not even with their mind's eye.
    They are compelled by the allure of the unknown... They must see it, now!
            """,
            "door2":"""
    {} already knows what a door feels like.
    It feels like a normal door on a normal train.
            """,
            "window":"""
    {} touches the window. It feels like cool glass
    It reminds them of what they think a crystal ball might feel like.
            """,
            "other":"""
    {} refuses to grope around like a fool.
            """
        },
        "taste": {
            "blood":"""
    {} doesn't need to taste the blood to know it tastes like blood.
    They taste it anyway...
    The bloodstains range from 30 minutes to 2 hours in age, from at least 5 people.
            """,
            "food":"""
    Unnecessary. {} has already calculated the original flavor of the fresh food in their head.
    Hmm... Maybe some more Sodium Chloride next time...
            """,
            "tome":"""
    Been there, done that.
            """,
            "other":"""
    {} refuses.
            """
        },
        "sniff": {
            "blood":"""
    A metallic, rich aroma...
    Weak blood, drained of the little life essence it once carried.
            """,
            "tome":"""
    It smells like powerful magic...
    The same magic {} feels coursing through their body.
            """,
            "door1":"""
    The air wafting through the door smells like static electricity and ozone.
    The hair stands up on the back of {}'s neck.
    A potent spirit dwells in the next car...
            """,
            "other":"""
    {} takes a few good whiffs...
    The train car is ripe with odours most foul.
            """
        },
        "look": {
            
            "switch": {
                "light": """
    A pitiful contraption for lesser beings unable to project light from their very skin.
    It's beneath {} to make use of it.
    They turn it off, because it's too bright in here.
                """,
                "dark":"""
    A pitiful contraption for lesser beings unable to project light from their very skin.
    It's beneath {} to make use of it.
    It's as dark as it gets in here.
                """
            },
            "blood":"""
    Somweone has left their life's blood behind.
    Too far degraded for any use. A pity...
            """,
            "food":"""
    Disgusting. {} will not pollute their mind with such unclean images.
            """,
            "tables":"""
    {} sees five circular tables laden with rotten FOOD.
    Also present on the tables is the TOME.
    It sits, exhausted of malice.
            """,
            "tome":"""
    {} looks over the tome, an ornate book bound in human skin.
    It exudes magic from the same source as your own...
    They kind of feel like they are bathing in their own sweat.
            """,
            "door1":"""
    The curtain is drawn on the other side of the door's window.
    What seems to be a breeze disturbs it now and then, revealing nothing but darkness.
    The allure of the unknown calls...
            """,
            "door2":"""
    This door's window seems to be covered with a large piece of plywood. How uncouth.
    Flickering light from the other side of the door shines through small gaps in the wood.
            """,
            "window":"""
    {} looks out the window...
    But it's too bright in the train car to see anything outside.
    Instead, {} sees themself, a magnifiscent figure wreathed in the glowing blue light that suffuses the room.
    {} gives a wizardly wink at you through the mirrored window.
            """,
            "other":"""
    {} looks around...
    The train car is covered in about three gallons of rapidly expiring life's BLOOD.
    Tacky, partially drying PUDDLES of the stuff are scattered across the floor.
    Despite the obvious carnage that took place here, there doesn't seem to be any bodies.
    This seems to be a dining car, the walls lined with TABLES holding a variety of ITEMS.
    Platters of rotten FOOD are arrayed throughout the car, an unpleasant tableau of decay and death.
    On the wall is the light SWITCH, rendered unnecessary.
    There is a WINDOW on each side of the carriage, made mirror-like by the brightness inside the train car.
    There are two DOORS (DOOR 1 and DOOR 2) to the front and rear of the train car, respectively.
                """
        },
        "listen": {
            "blood":"""
    {} imagines the BLOOD gurgling softly.
    It whispers...
    "I was once in the veins of a guy named Abrahand Lickin'. Hell of a thing, ain't it?"
            """,
            "tome":"""
    {} hears otherworldly whispers emanating from the tome.
    They say: "Warning! This tome is cursed!".
            """,
            "door1":"""
    {} hears something rhythmic...
    It sounds like the chanting of an incantation.
            """,
            "window":"""
    {} cups their ear against the window.
    Maybe they hear a bird outside. 
    I don't know, it's hard to tell.
            """,
            "other":"""
    {} listens to the intermittent clunk of the train passing over the rough railway.
    The train seems to be traveling quite fast, about 90 miles per hour.
            """
        },
        "go": {
            "door1":"""

            """,
            "door2":"""

            """
        }
    },
    "car2": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    },
    "void": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    },
    "car3": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    }
}

cursed = {
    "car0": {
        "touch": {

        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    },
    "dining car": {
        "touch": {
            'other':"""
    You try to touch the {}, but your hands are still frozen to the tome!
    They're starting to go numb...
            """
        },
        "taste": {
            "switch":"""
    Arms still frozen in place by the cursed TOME, you crane your neck towards the LIGHT SWITCH.
    After a few seconds of fumbling, you manage to turn on the lights!
            """,
            "blood":"""
    It tastes metallic, tangy, and almost sweet.
    Yep, that's definitely BLOOD.
    You wish it was fresher...
    You're quite hungry.
            """,
            "food":"""
    Leaning over the table with your upper body, you use your mouth to seize a scrap of spoiled meat.
    After a few short minutes of crunching and slurping, it's gone.
    You're still hungry...
            """,
            "tables":"""
    The bare imitation-wood vinyl turns your stomach.
    However, you manage to find a spot of BLOOD while licking the table.
    It's not enough, though...
            """,
            "tome":"""
    You try to lick the tome...
    However, your arms are paralyzed too far forward.
    You cannot reach its pages with your tongue.
            """,
            "door1":"""
    This door tastes like promise.
    Like power.
            """,
            "door2":"""
    This door tastes like freedom...
    And death.
            """,
            "window":"""
    You lick the window.
    It's a cold night, and something strange is on the air.
    You keep licking until you find a spot of blood.
    Not bad.
            """,
            "other":"""
    You lick the wall.
    It tastes like BLOOD.
    You're quite hungry.
            """
        },
        "sniff": {
            "blood":"""
    A metallic, rich aroma...
    Yep, that smells like BLOOD.
    It's drying, though. Not fresh.
            """,
        # these are copied from normal. need to be edited for cursed still
            "food":"""
    You lean in to one of the platters and take a deep whiff...
    The smell of the rotting food entices you as if it were a free breakfast buffet.
            """,
            "tables":"""
    The smell of rot and death fills your nostrils.
    Your stomach growls...
    Why did you ever used to think this was bad?
            """,
            "tome":"""
    It smells just like you.
            """,
            "door1":"""
    The air wafting through the door smells like static electricity and ozone.
    The hair stands up on the back of your neck.
    It feels powerful...
            """,
            "door2":"""
    That doesn't smell like anything.
            """,
            "window":"""
    That doesn't smell like anything.
            """,
            "other":"""
    You take a few good whiffs...
    The coppery scent of BLOOD hits your nostrils, overwhelming all else.
    If only it was fresher...
            """
        },
        "look": {
            "dark": {
                "tables":"""

                """,
                "window":"""

                """,
                "other":"""

                """
            },
            "light": {
                "switch":"""

                """,
                "blood":"""

                """,
                "food":"""

                """,
                "tables":"""

                """,
                "tome":"""

                """,
                "door1":"""

                """,
                "door2":"""

                """,
                "window":"""

                """,
                "other":"""

                """
            }
        },
        "listen": {
            "switch":"""

            """,
            "blood":"""

            """,
            "food":"""

            """,
            "tables":"""

            """,
            "tome":"""

            """,
            "door1":"""

            """,
            "door2":"""

            """,
            "window":"""

            """,
            "other":"""

            """
        }
    },
    "car2": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    },
    "void": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    },
    "car3": {
        "touch": {
            
        },
        "taste": {

        },
        "sniff": {
        
        },
        "look": {
        
        },
        "listen": {
        
        }
    }

}

# this is where the narration for different gome over/ending conditions is stored
endings = {
"fell off":"""

""",
"voided out":"""

"""

}