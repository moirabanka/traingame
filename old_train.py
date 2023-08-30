help_text = """

Call on your character's five senses to help you understand the environment!

sinmply type one of these commands:
    "touch", "taste", "sniff", "look", or "listen"
If you call on one of your senses, the game will ask if you'd like to use it on anything in particular.
CAPITALIZED text shows the names of interactable things. Type them in lowercase if you'd like to use them.
if you don't want to interact with a specific thing, just press RETURN.

However, keep in mind that it may affect your character.
You may not always like what you find...

To move between areas, simply type the name of the exit you wish to use.

There are also other hidden commands...

Good luck!


"""


print(help_text)
name = input("Enter your character's name:\n> ")

print(f"{name} is standing in a darkened train car.\nThe carriage bumps and rattles.")
print("What do you do?")

"""
List of interactables:

car1
lightswitch, blood, food, tables, tome, door1, door2, window

car1_wizard, car1_cursed: (all values for car1, plus...) ghost/spirit

car2: shrine, 

car2_wizard, car2_cursed: 
"""

"""
rethinking inputs...?
valid_targets = [switch, lightswitch]
touch_what = input("> ")
if touch_what in valid_targets:
    print("turned on lights!")

"""
def reset_car(carnumber):
    prompt = "Okay... what do you do now?\n"
    if carnumber == "1_default":
        print("\n\nYou're still in the car where you woke up. The lights are off.")
        print(prompt)
        car1()
    elif carnumber == "1_cursed":
        print("\n\nYou're still in the car you woke up in. Your hands are still stuck holding the book.")
        print("You feel like something is watching you.")
        print(prompt)
        #car1_cursed()
    elif carnumber == "1_lights_on":
        print("\n\nYou're still in the car where you woke up. The lights are on.")
        print(prompt)
        car1_lights_on()
    elif carnumber == "1_wizard":
        print(f"\n\n{name}'s physical form still dwells in the train car where their former self once awoke.")
        print("How long ago that seems...")
        print(f"{name}'s surroundings are lit by their luminescence.")
        car1_wizard()

def car1():
    action = input("> ")
    if action == "touch":
        print("Want to touch anything in particular?")
        touch_what = input("> ")
        #maybe use "variable in [list]"
        if touch_what == ("switch" or "lightswitch"):
            print("You find a light SWITCH!")
            print("You flick it on, bathing the train car in light.")
            print("There's blood everywhere, and I mean *everywhere*.")
            reset_car("1_lights_on")
        elif touch_what == ("blood" or "surfaces" or "puddles"):
            print("It's a viscous, dark fluid. Tacky in places, and partially dried.")
            reset_car("1_default")
        elif touch_what == ("tables" or "items"):
            print("You feel a number of objects here. Some sort of squarish THING, and what seems to be heaping plates of rotten FOOD")
            reset_car("1_default")
        elif touch_what == "food":
            print("You sift through the plates of rotten FOOD...")
            print("Eventually, you have to face the truth. there's nothing edible here.")
            print("You accidentally poke your finger through the soft exterior of a decaying fruit.")
            print("Gross...")
            reset_car("1_default")
        elif touch_what == ("thing" or "tome"):
            print("You grab the tome and the lights flicker out. It seems to compel you to open it...")
            resist = input("Can you resist its influence?\n> ")
            if resist == "xoglfotz":
                print("You speak the tome's word of power!")
                print("The tome has no more power over you. It goes limp in your hands.")
                print("Your skin begins to emit a soft glow...")
                print(f"{name} feels more magic.")
                car1_wizard()
            else:
                print("You are unable to resist the tome's influence!")
                print("The tome chills your hands, freezing them in place!")
                print("You can't tell if the book contains pictures or words, but the images writhe ceaselessly...")
                #car1_cursed()
                reset_car("1_default")
        elif touch_what == ("door1" or "door2"):
            print("You feel all around the door. It feels like a normal door on a train.")
            reset_car("1_default")
        else:
            print("Unsure of what you're looking for, you grope around the carriage.")
            print("On the walls and floor, you find a number of PUDDLES and wet SURFACES, what seems to be a light SWITCH, and a number of TABLES laden with ITEMS.")
            print("You feel the cool glass of a WINDOW inset into each wall.")
            print("There are doors (DOOR1 and DOOR2) on the front and rear of the carriage, leading to other train cars.")
            reset_car("1_default")


    elif action == "taste":
        print("Want to taste anything in particular?")
        taste_what = input("> ")
        if taste_what == ("surfaces" or "blood" or "puddles"):
            print("It tastes metallic...")
            print("Yep, that's definitely BLOOD.")
            reset_car("1_default")
        elif taste_what == ("tome" or "thing"):
            print("You lick the tome...")
            print("Ouch! You got a papercut on your tongue!")
            print("The blood seeps into the tome's pages, quickly disappearing before your eyes...")
            print("A word of power whispers itself into your mind...\n\"XOGLFOTZ\"")
            reset_car("1_default")
        elif taste_what == "food":
            print("You attempt to peel a rotting banana before you eat it, but the stem simply sloughs off in your grasp.")
            print("You take a small bite, peel and all.")
            print("You feel gross.")
            reset_car("1_default")
        elif taste_what == ("switch" or "lightswitch"):
            print("You lean in and lick the light SWITCH. After a few seconds of fumbling, you manage to turn on the lights!")
            print("How many people have touched that thing...?")
            car1_lights_on()
        elif taste_what == "tables":
            print("Ouch! You get a huge splinter in your tongue!")
            print("On the other hand, the sliver is so big you kinda look like one of those cool guys with toothpicks.")
            print("You decide to keep it.")
            reset_car("1_default")
        elif taste_what == ("door1" or "door2"):
            print("Yep, it tastes like door.")
            reset_car("1_default")
        else:
            print("You lick the wall. It tastes like BLOOD.")
            reset_car("1_default")
    

    elif action == "sniff":
        print("Want to sniff anything in particular?")
        sniff_what = input("> ")
        if sniff_what == ("blood" or "surfaces" or "puddles"):
            print("A metallic, rich aroma...")
            print("Yep, that smells like blood.")
            reset_car("1_default")
        elif sniff_what == ("tome" or "thing"):
            print("It smells like death.")
            print("You reflexively gag and recoil away.")
            reset_car("1_default")
        elif sniff_what == "door1":
            print("The air wafting through the door smells like static electricity and ozone.")
            print("The hair stands up on the back of your neck.")
            print("You're not sure what that means...")
            reset_car("1_default")
        else:
            print("You take a few good whiffs...")
            print("The coppery scent of BLOOD hits your nostrils almost immediately, followed by the scent of rotten FOOD.")
            reset_car("1_default")


    elif action == "look":
        print("Want to look at anything in particular?")
        look_what = input("> ")
        if look_what == "tables":
            print("You see the silhoutte of TABLES laden with ITEMS.")
            print("Too dark to make out what the ITEMS are...")
            reset_car("1_default")
        elif look_what == "window":
            print("""You look out the window...
The silhouettes of trees whiz past the dark sky.
The moon hangs overhead, Its meager sliver casting a slight silvery glow.
Beyond the rattling of the rails beneath the carriage, all is quiet.
You feel like it's going to be a long night.
                  """)
            reset_car("1_default")
        else:
            print("It's too dark to see any detail, but there seem to be some TABLES around...")
            reset_car("1_default")
                

    elif action == "listen":
        print("Listen to anything in particular?")
        listen_what = input("> ")
        if listen_what == ("tome" or "thing"):
            print("You hear otherworldly whispering.")
            print("This books seems quite powerful.")
            print("Perhaps that power can be yours...")
            reset_car("1_default")
        elif listen_what == "door1":
            print("You can't quite make it out, but you hear something rhythmic...")
            print("Maybe music?")
            reset_car("1_default")
        else:
            print("You listen to the intermittent clunk of the train passing over the rough railway.")
            print("You seem to be traveling quite fast.")
            reset_car("1_default")
    

    elif action == "door1":
        print("You enter the first door, moving towards the head of the train.")
        #car2()
        reset_car("1_default")

    elif action == "door2":
        print("The door is stuck! You try to dislodge it to no avail.")
        print("you hear the clacking of the developer's keys, trying to write more of this game before you get the door open.")
        reset_car("1_default")

    else:
        print("Unrecognized command! Sorry...")
        print("Would you like to see the help text?")
        want_help = input("Type \"y\" if you would like me to print the help text, otherwise, simply press RETURN.")
        if want_help == "y":
            print(help_text)
        reset_car("1_default")

def car1_lights_on():
    action = input("> ")
    if action == "touch":
        print("Want to touch anything in particular?")
        touch_what = input("> ")
        if touch_what == ("switch" or "lightswitch"):
            print("You flick it off, plunging the train car back into darkness.")
            reset_car("1_default")
        elif touch_what == ("surfaces" or "blood" or "puddles"):
            print("It's a viscous, dark fluid. Tacky in places, and partially dried.")
            reset_car("1_lights_on")
        elif touch_what == ("tables" or "items"):
            print("You feel a number of objects here. Some sort of squarish THING, and what seems to be heaping plates of rotten FOOD")
            reset_car("1_lights_on")
        elif touch_what == "food":
            print("You sift through the plates of rotten FOOD...")
            print("Eventually, you have to face the truth. There's nothing edible here.")
            reset_car("1_lights_on")
        elif touch_what == ("tome" or "thing"):
            print("You grab the tome and the lights flicker out. It seems to compel you to open it...")
            resist = input("Can you resist its influence?\n> ")
            if resist == "xoglfotz":
                print("You speak the tome's word of power!")
                print("The tome has no more power over you. It goes limp in your hands.")
                print("Your skin begins to emit a soft glow.")
                print(f"{name} feels more magic...")
                car1_wizard()
            else:
                print("You are unable to resist the tome's influence!")
                print("The tome chills your hands, freezing them in place!")
                print("You can't tell if the book contains pictures or words, but the images writhe ceaselessly...")
                #car1_cursed()
                reset_car("1_lights_on")
        elif touch_what == ("door1" or "door2"):
            print("You feel all around the door. It feels like a normal door on a train.")
            reset_car("1_lights_on")
        else:
            print("Unsure of what you're looking for, you grope around the carriage.")
            print("On the walls and floor, you find a number of PUDDLES and wet SURFACES, what seems to be a light SWITCH, and a number of TABLES laden with ITEMS.")
            print("You feel the cool glass of a WINDOW inset into each wall.")
            print("There are doors (DOOR1 and DOOR2) on the front and rear of the carriage, leading to other train cars.")
            reset_car("1_lights_on")


    elif action == "taste":
        print("Want to taste anything in particular?")
        taste_what = input("> ")
        if taste_what == ("blood" or "surfaces" or "puddles"):
            print("It tastes metallic...")
            print("Yep, that's definitely BLOOD.")
            reset_car("1_lights_on")
        elif taste_what == ("thing" or "tome"):
            print("You lick the tome...")
            print("Ouch! You got a papercut on your tongue!")
            print("The blood seeps into the tome's pages, quickly disappearing before your eyes...")
            print("A word of power whispers itself into your mind...\n\"XOGLFOTZ\"")
            reset_car("1_lights_on")
        elif taste_what == "food":
            print("You attempt to peel a rotting banana before you eat it, but the stem simply sloughs off in your grasp.")
            print("You take a small bite, peel and all.")
            print("You feel gross.")
            reset_car("1_lights_on")
        elif taste_what == ("lightswitch" or "switch"):
            print("You lean in and lick the light SWITCH. After a few seconds of fumbling, you manage to turn off the lights!")
            print("How many people have touched that thing...?")
            reset_car("1_default")
        elif taste_what == "tables":
            print("Ouch! You get a huge splinter in your tongue!")
            print("On the other hand, the sliver is so big you kinda look like one of those cool guys with toothpicks.")
            print("You decide to keep it.")
            reset_car("1_lights_on")
        elif taste_what == ("door1" or "door2"):
            print("Yep, it tastes like door.")
            reset_car("1_lights_on")
        else:
            print("You lick the wall. It tastes like BLOOD.")
            reset_car("1_lights_on")
    

    elif action == "sniff":
        print("Want to sniff anything in particular?")
        sniff_what = input("> ")
        if sniff_what == ("blood" or "surfaces" or "puddles"):
            print("A metallic, rich aroma...")
            print("Yep, that smells like blood.")
            reset_car("1_lights_on")
        elif sniff_what == ("tome" or "thing"):
            print("It smells like death.")
            print("You reflexively gag and recoil away.")
            reset_car("1_lights_on")
        elif sniff_what == "door1":
            print("The air wafting through the door smells like static electricity and ozone.")
            print("The hair stands up on the back of your neck.")
            print("You're not sure what that means...")
            reset_car("1_lights_on")
        else:
            print("You take a few good whiffs...")
            print("The coppery scent of BLOOD hits your nostrils almost immediately, followed by the scent of rotten FOOD.")
            reset_car("1_lights_on")


    elif action == "look":
        print("Want to look at anything in particular?")
        look_what = input("> ")
        if look_what == ("tables" or "items"):
            print("You see five circular tables. On them sits many platters of rotten FOOD.")
            print("Also present on the tables is what seems to be an ancient TOME.")
            print("It looks quite valuable...")
            reset_car("1_lights_on")
        if look_what == ("tome" or "thing"):
            print("You look over the tome, an ornate book bound in a pale leather with a wide variety of symbols and patterns embossed in precious metals.")
            print("The symbols are striking, but hardly anything you recognize. Perhaps some sort of calligraphy?")
            print("It's quite a striking volume, however. Clearly, potent secrets reside within.")
            print("And, for some strange reason, it seems rather tasty...")
            reset_car("1_lights_on")
        if look_what == ("blood" or "surfaces" or "puddles"):
            print("Smears and spatters of blood cover the inside of the train car.")
            print("It seems to be drying, but still somewhat fresh.\nGleams of bright crimson reside among the flaking rusty brown.")
            reset_car("1_lights_on")
        if look_what == "food":
            print("Plates piled high with spoiled fruit and moldy bread are spread throughout the room.")
            print("The flies are having a goddamn field day...")
            reset_car("1_lights_on")
        if look_what == "door1":
            print("The curtain is drawn on the other side of the door's window.")
            print("What seems to be a breeze disturbs it now and then, revealing nothing but darkness.")
            reset_car("1_lights_on")
        if look_what == "door2":
            print("This door's window seems to be covered with a large piece of plywood.")
            reset_car("1_lights_on")
        elif look_what == "window":
            print("""You look out the window...
But it's too bright in the train car to see anything outside.
Instead, you see yourself standing in your bloody surroundings.
You look disheveled and displeased.
                  """)
            reset_car("1_lights_on")
        else:
            print("""You look around...
The train car is covered in smears and streaks of BLOOD.
Tacky, partially drying PUDDLES of the stuff are scattered across the floor.
Despite the obvious carnage that took place here, there doesn't seem to be any bodies.
This seems to be a dining car, the walls lined with TABLES that hold a variety of ITEMS.
Platters of rotten FOOD are arrayed throughout the car, an unpleasant tableau of decay and death.
On the wall is the light SWITCH, toggled on.
There is a WINDOW on each side of the carriage, made mirror-like by to the brightness inside the train car.
There are two DOORs (DOOR1 and DOOR2) to the front and rear of the train car, respectively.
The lights flicker as the train clatters over the rough rails, but they hold.
                  """)
            reset_car("1_lights_on")
                

    elif action == "listen":
        print("Listen to anything in particular?")
        listen_what = input("> ")
        if listen_what == ("tome" or "thing"):
            print("You hear otherworldly whispers enticing you.")
            print("This books seems quite powerful.")
            print("Perhaps that power can be yours...")
            reset_car("1_lights_on")
        elif listen_what == "door1":
            print("You can't quite make it out, but you hear something rhythmic...")
            print("Maybe music?")
            reset_car("1_lights_on")
        else:
            print("You listen to the intermittent clunk of the train passing over the rough railway.")
            print("You seem to be traveling quite fast.")
            reset_car("1_lights_on")
    
    
    elif action == "door1":
        print("You enter the first door, moving towards the head of the train.")
        #car2()
        reset_car("1_lights_on")

    elif action == "door2":
        print("The door is stuck! You try to dislodge it to no avail.")
        print("you hear the clacking of the developer's keys, trying to write more of this game before you get the door open.")
        reset_car("1_lights_on")

    else:
        print("Unrecognized command! Sorry...")
        print("Would you like to see the help text?")
        want_help = input("Type \"y\" if you would like me to print the help text, otherwise, simply press RETURN.")
        if want_help == "y":
            print(help_text)
        reset_car("1_lights_on")

def car1_wizard():
    action = input("> ")
    if action == "touch":
        print("Want to touch anything in particular?")
        touch_what = input("> ")
        if touch_what == ("switch" or "lightswitch"):
            print(f"{name} has no need for such contrivances of simpler beings.")
            print(f"The luminosity of {name}'s skin should suffice.")
            reset_car("1_wizard")
        elif touch_what == ("surfaces" or "blood" or "puddles"):
            print("Somweone has left their life's blood behind.")
            print("Too far degraded for any use. A pity...")
            reset_car("1_wizard")
        elif touch_what == ("tables" or "items"):
            print("The tables are constructed with plastic paneling printed to look like wood.")
            print(f"It's incredibly tacky. {name} is somewhaty insulted by your suggestion to touch it.")
            print(f"Out of the overwhelming kindness of their heart, {name} forgives you.")
            reset_car("1_wizard")
        elif touch_what == "food":
            print(f"{name} refuses to touch the rotten food.")
            print("Let the dead demcompose in peace...")
            reset_car("1_wizard")
        elif touch_what == ("tome" or "thing"):
            print(f"{name} picks up the tome. It hangs limply in their grasp, defeated.")
            print(f"{name} and the tome now share the source of their powers. For one to hurt the other is to hurt themselves.")
            reset_car("1_wizard")
        elif touch_what == ("door1"):
            print(f"Behind this door lies something the likes of which {name} has never perceived, not even with their mind's eye...")
            print(f"{name} is compelled by the allure of the unknown. They must see it, now!")
            #car2_wizard()
            reset_car("1_wizard")
        elif touch_what == ("door2"):
            print("Behind this door lies an absolute void. An unmade space.")
            print("Fascinating...")
            reset_car("1_wizard")
        else:
            print(f"{name} refuses to grope around like a fool.")
            reset_car("1_wizard")


    elif action == "taste":
        print("Want to taste anything in particular?")
        taste_what = input("> ")
        if taste_what == ("blood" or "surfaces" or "puddles"):
            print(f"{name} doesn't need to taste that to know it tastes like blood.")
            print(f"{name} tastes it anyway...")
            print("The bloodstains range from 30 minutes to 2 hours in age, from at least 5 people.")
            reset_car("1_wizard")
        elif taste_what == ("tome" or "thing"):
            print("Been there, done that.")
            reset_car("1_wizard")
        elif taste_what == "food":
            print(f"Unnecessary. {name} has already calculated the original flavor of the fresh food in their head.")
            print("Hmm... Maybe some more Sodium Chloride next time...")
            reset_car("1_wizard")
        else:
            print(f"{name} refuses.")
            reset_car("1_wizard")
    

    elif action == "sniff":
        print("Want to sniff anything in particular?")
        sniff_what = input("> ")
        if sniff_what == ("blood" or "surfaces" or "puddles"):
            print("A metallic, rich aroma...")
            print("Weak blood, drained of the little life essence it once carried.")
            reset_car("1_wizard")
        elif sniff_what == ("tome" or "thing"):
            print("It smells like powerful magic...")
            print(f"The same magic {name} feels coursing through their body.")
            reset_car("1_wizard")
        elif sniff_what == "door1":
            print("The air wafting through the door smells like static electricity and ozone.")
            print(f"The hair stands up on the back of {name}'s neck.")
            print("A potent spirit dwells in the next car...")
            curious_check = input(f"is {name} able to resist their curiosity? (y/n)\n> ")
            if curious_check == "y":
                print(f"{name} thinks better of rushing in.")
                reset_car("1_wizard")
            else:
                print(f"{name} cannot resist! They rush through the door.")
                #car2_wizard()
                reset_car("1_wizard")

        else:
            print(f"{name} takes a few good whiffs...")
            print(f"The coppery scent of shed life's BLOOD hits {name}'s nostrils immediately, followed by the stech of decay, which {name} abjures.")
            print(f"{name} can also smell magic in the air...")
            reset_car("1_wizard")


    elif action == "look":
        print("Want to look at anything in particular?")
        look_what = input("> ")
        if look_what == ("tables" or "items"):
            print(f"{name} sees five circular tables laden with rotten FOOD.")
            print("Also present on the tables is the TOME.")
            print("It sits exhausted of malice.")
            reset_car("1_wizard")
        if look_what == ("tome" or "thing"):
            print(f"{name} looks over the tome, an ornate book bound in human skin.")
            print("It exudes magic from the same source as your own...")
            print(f"{name} kind of feels like they are bathing in their own sweat.")
            print(f"{name} finds this uninteresting.")
            reset_car("1_wizard")
        if look_what == ("blood" or "surfaces" or "puddles"):
            print("Somweone has left their life's blood behind.")
            print("Too far degraded for any use. A pity...")
            reset_car("1_wizard")
        if look_what == ("food" or "filth"):
            print(f"Disgusting. {name} will not pollute their mind with such unclean images.")
            reset_car("1_wizard")
        if look_what == "door1":
            print("The curtain is drawn on the other side of the door's window.")
            print("What seems to be a breeze disturbs it now and then, revealing nothing but darkness.")
            print("The allure of the unknown calls...")
            reset_car("1_wizard")
        if look_what == "door2":
            print("This door's window seems to be covered with a large piece of plywood. How uncouth.")
            reset_car("1_wizard")
        elif look_what == "window":
            print(f"""{name} looks out the window...
But it's too bright in the train car to see anything outside.
Instead, {name} sees themself, a magnifiscent figure wreathed in the glowing blue light that suffuses the room.
{name} gives a wizardly wink at you through the mirrored window.
                  """)
            reset_car("1_wizard")
        else:
            print(f"""{name} looks around...
The train car is covered in about three gallons of rapidly expiring life's BLOOD.
Tacky, partially drying PUDDLES of the stuff are scattered across the floor.
Despite the obvious carnage that took place here, there doesn't seem to be any bodies.
This seems to be a dining car, the walls lined with TABLES holding a variety of ITEMS.
Platters of rotten FOOD are arrayed throughout the car, an unpleasant tableau of decay and death.
On the wall is the light SWITCH, rendered unnecessary.
There is a WINDOW on each side of the carriage, made mirror-like by the brightness inside the train car.
There are two DOORS (DOOR 1 and DOOR 2) to the front and rear of the train car, respectively.
Everything in the carriage is lit by the ghostly glow emitted by {name}'s skin.
                  """)
            reset_car("1_wizard")
                

    elif action == "listen":
        print("Listen to anything in particular?")
        listen_what = input("> ")
        if listen_what == ("tome" or "thing"):
            print(f"{name} hears otherworldly whispers emanating from the tome.")
            print("They say: \"Warning! This tome is cursed!\".")
            reset_car("1_wizard")
        elif listen_what == "door1":
            print(f"{name} hears something rhythmic...")
            print("It sounds like the chanting of an incantation.")
            reset_car("1_wizard")
        else:
            print(f"{name} listens to the intermittent clunk of the train passing over the rough railway.")
            print("The train seems to be traveling quite fast, about 90 miles per hour.")
            reset_car("1_wizard")
    
    
    elif action == "door1":
        print("You enter the first door, moving towards the head of the train.")
        #car2()
        reset_car("1_wizard")

    elif action == "door2":
        print("The door is stuck! You try to dislodge it to no avail.")
        print("you hear the clacking of the developer's keys, trying to write more of this game before you get the door open.")
        reset_car("1_wizard")

    else:
        print("Unrecognized command! Sorry...")
        print("Would you like to see the help text?")
        want_help = input("Type \"y\" if you would like me to print the help text, otherwise, simply press RETURN.")
        if want_help == "y":
            print(help_text)
        reset_car("1_wizard")


#def car1_cursed():

#def car2():

#def car2_wizard():

#def car2_cursed():


car1()