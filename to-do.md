Immediate Goals
- [x] condition-agnostic consequences
- [x] target aliases
    e.g: 'taste puddle' needs to return the same consequences as 'taste blood'
- [x] command aliases
    e.g: 'lick blood' needs to return the same consequences as 'taste blood'
- [x] target-agnostic consequences
    in cases where performing an action on a target does not have any unique consequences (e.g: sniffing the lightswitch), this should return the same consequences as if the 'other' target was used
- [x] create a new consequence type that checks if the player wants to perform an additional action with a Y/n prompt
    e.g: player enters 'touch door' when cursed. the game asks the player if they want to smash the door, and lets them type yes or no
    maybe accomplish these with a flag put on any narration. straightforward narration can be stored as a string in a dictionary key, but this kind of special narration is stored as a list that also contains an extra flag that triggers this prompt along with other strings for follow-up narration
    if i'm doing this, i might as well also make a flag that lets the player choose from a list of options. it would be cool if the options could be contextual and based on the player's current emotions or stance. This could be the basis of the dialogue system.
- [x] change how player commands are processed
    one-word commands should be valid, and invalid targets need to default to 'other'
- [x] implement system commands that can be used while in game, such as 'save' or 'load'
- [x] find a way to display special narration based on conditions, backgrounds, emotions, or stances
    I'm thinking thay this special narration should always be associated with a check. However, I also want to have an alternate mechanic for replacing the original status-based narration, though this should be done only rarely.
- [ ] add a game cycle function that loops through the player turn, threat turns, and performs necessary checks and upkeep
- [x] loop the player turn so that the player can retry faulty commands
- [x] change the resolve function so it is more readable
- [ ] add a time counter that can be used to trigger threat turns
- [ ] migrate narration to new consequence dictionary
- [ ] add additional consequences for the migrated narration
- [ ] system command that shows all commands the player can use right now
    including contextual commands and those drawn from the character's background and status
- [ ] system command that shows the character's current emotional state and stance
- [ ] tracked character history
    should take note of all interactions that can have an effect on the character that shouldn't be repeatable.
    also requires a system that checks when a command has been used before and changes the consequences as a result
- [ ] flesh out the backgrounds
    Malcontent (madcap?)
        Wants to break things. better at aggression. cruel streak.
    Utilitarian
        Wants to use and repurpose items.
    Gourmond
        Appreciative of life's beauties. indulgent. loves food. has a good time.
    Reactionary
        Ruled by fear. hateful can transmute fear to anger and disgust at will. good reaction time. resistant to cognitive dissonance
        So far, this is by far the most interesting class


Game presentation
- [x] main menu
    should be able to choose whether to start a new game, load a save, or quit. Ideally, should also have a way to delete characters and a developer menu with commands that can help debug the game

Zones
- [ ] Car 0 (caboose): locked car with secrets
- [ ] Car 1: kitchen car (on fire?)
- [ ] Car 2: murder mystery dining car (starting zone)
- [ ] Car 3: luxury first class sleeper car (undead rich people)
    the door to this car is locked. the ley must be found elsewhere. Cursed characters can open the door without the key by smashing through the door.
- [ ] Car 4: cargo car
    there is a door here in the side of the carriage, seemingly leading to the open air but instead opening on another area
- [ ] Cars 5 & 6: economy micro-budget passenger car
- [ ] Car 7: staff quarters
- [ ] Car 8: engine
- [ ] Wasteland
    largely empty, coordinate tracked area with hidden secrets and basic survival mechanics (dig up a lizard for food). Can be accessed when leaving the train. it is impossible to re-enter the train. This is your character's life now.


Character state
- [x] saved character file and loadable worldstate
- [ ] hunger counter
    this ticks up as your character acts, ticking up faster for physically/mentally exerting actions. Your character's statuses determine the kind of food they find palatable (e.g: cursed characters want meat/rotten food, wizards want fancy or esoteric foods). The palatability of the food you consume will determine its effects on your character's emotions. Your character won't need to eat too often (kept realistic to time passing), but the food you eat will provide bonuses and maluses
- [x] character creation step
    The player chooses a number of personality traits for their character that create synergies between emotions and stances. (e.g: the "malcontent" personality trait gives bonuses to happiness while in the aggro stance, the "utilitarian" trait gives bonuses to happiness when consuming simple foods or performing efficacious actions, and the "melacholic" trait allows you to increase your sadness level at any time using the special "contemplate" move)
    The player also selects a background that determines their character's initial emotional state along with some semi-hidden values that effect how your character reacts to certain events.
- [x] emotional state tracking
    As the player directs their character to interact with their world, the character will be emotionally affected by the things they experience
- [ ] emotional stances
    The game tallies up your character's emotion values and uses them to determine your current "stance"
    current stance list:
        ebullient
        aggressive
        defensive
        repulsed
        

- [ ] mutually exlusive statuses
- [ ] inter-compatible statuses
- [x] tracked inventory system

Mechanics
- [x] character actions change emotional state
- [ ] current emotional state effects narration
- [ ] emotional spiralling
- [ ] character rebellion
- [ ] confidence/desperation mechanic
- [ ] character followers
- [ ] wasteland survival (AI integration??)
- [ ] dialogue battle system
    The only form of combat in the game. Your character's emotional state affects their current "stance" (aggro, apologetic, obsequious, etc).
    Your character's stance affects which dialogue moves are available. For example, if you are in the aggro stance, you can use the "threaten" move
- [ ] mortal (survival) mode vs immortal mode
- [ ] adrenaline
- [ ] cognitive dissonance stat that increases when opposing emotions are gained
- [ ] crisis events
- [ ] repurposing of inventory items into tools using the 'repurpose' command
    should this be a special ability for the 'utilitarian' background?
    this should change the item into an alternate form based on the player's surroundings.
    e.g: in the wasteland, a stick in the inventory can be repurposed into a digging tool

Display
- [ ] slow printing stylish output
- [ ] text colors for different NPCs and character states
