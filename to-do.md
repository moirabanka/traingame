what needs to be done:
- [ ] revise tutorial messages, finish walkthrough of the mystery system
- [ ] add the option for narration to be tagged with a speaker (either a character, trait, or skill)
- [ ] nail down emotion mechanics

New goals:
    overarching:
- [ ] create a tutorial
- [x] redo text printing
- [ ] create autosense feature
    this would allow for certain one-word commands to occur automatically, like looking around when you enter a new room. with autosense disabled, saving throws are needed to keep from perceiving some things (e.g: trying not to pay attention to a horrible smell)
    autolook
    autosmell
    autolisten
    autotaste, autotouch (normally disabled, only enabled by some traits)
- [ ] assign a priority value for all narration
    this would allow coincident narration consequences to be sorted in order of their priority when displaying narration from multiple sources. the highest priority could ovverride the default narration
- [ ] add 'frenzy' stat for unpredictable actions
- [ ] remove narration from game_data and put it into its own file where it can be arranged more beautifully
    I was writing tutorial narration and things got disorganized. narration should be grouped by trait, sense, target, and location in some arrangement
    immediate:
- [ ] create a system for labeling the speaker of given lines of narration
    this is necessary for implementing dialogue with NPCs and the player's own skills
- [ ] allow certain lines of narration/dialogue to interrupt primary narration or replace specific parts
    this will help create a dynamic system of narration and dialogue
    maybe enmesh this with the dialogue priority idea
- [x] implement line wrapping for narration in a narrate(narration) function
- [x] add slow printing to narration
- [x] add confidence/composure stat to character file
- [x] change how longer narration is displayed
- [ ] rewrite stat check/change functions to be able to change or check anything (stats, traits, inventory, etc)
- [ ] autosense/autolook feature
- [ ] redo game intro with the new_game consequence library
- [ ] add clue change and mystery change consequences to the narration library
    longer narration should be broken into chunks displayed one at a time. The player should be able to press 'enter' or 'space' to go to the next chunk
- [ ] add 'myself' as a universal target
- [ ] add help entries for mind palace commands
- [x] test mystery system code
- [ ] make every check or stat change check the player's history
- [x] revise narration_library to fit with new printing style
- [ ] fully populate narration_library with...
    - [ ] clues
    - [ ] mysteries
    - [ ] stat changes
    - [ ] checks with special narration
- [x] remove background system
- [x] remove status from main file and game_data
- [ ] create check_trait() function
- [ ] implement initial trait choice




Initial planning goals:
    Game presentation
- [x] main menu
    should be able to choose whether to start a new game, load a save, or quit. Ideally, should also have a way to delete characters and a developer menu with commands that can help debug the game
- [ ] beautify the main menu
    allow navigation with arrow keys to choose an option 

    Zones
- [ ] Car 0 (caboose): locked car with secrets
- [ ] Car 1: kitchen car (on fire?)
- [ ] Car 2: murder mystery dining car (starting zone)
- [ ] Car 3: luxury first class sleeper car (undead rich people)
    the door to this car is locked. the key must be found elsewhere. Cursed characters can open the door without the key by smashing through the door.
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
- [ ] cognitive dissonance stat
- [x] mutually exlusive statuses
- [x] inter-compatible statuses
- [x] tracked inventory system

    Mechanics
- [x] character actions change emotional state
- [ ] character traits
    Minor modifiers for your character. Traits should be acquirable through gameplay (e.g: licking the table will give you the 'toothpick' trait), possibly with some that can be chosen at character creation. A character's current traits should be stored as a list in their save file, and may be referenced in special circumstances or used when describing your character
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
