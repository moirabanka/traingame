I want to scale back my goals, and possibly focus in on the sleuth class as the main character archetype of the game. Finding evidence, drawing conclusions, investigating, and having breakdowns when your theories are proven wrong. Take influence from ace attorney.
all gameplay is going to center around the planned mechanics for the sleuth background. Character and narrative diversity will arise from the character's emotions and traits acquired either during character creation or through gameplay.

New concept for character creation.


Overall narrative:
Some sort of disaster befalls a train transporting people across the wastes. A number of people die, including almost all of the waitstaff. Only one waiter remains, and they refuse to work under the conditions. However, a number of powerful people are present on the train, and demand to be served. At their orders, the most freshly dead waiter was made into a wayfarer who would break the worker's one-man strike. When the supernaturalist employed by one of the powerful people attempted to summon a pliant spirit into the dead waiter's body, a mistake was made. Instead of a convenient scab, the spirit of the legendary private detective Burlock Golmes was summoned. Now it is the player's task to establish what exactly happened on this train, who caused it, where exactly you are, and what is going on.


Example of mechanics:
the rich undead character in the sleeper car will check your character for the 'wealthy' trait that can be picked at the beginning of the game. If you don't have it, he will ask your character to fetch his meal for him from the chef in the kitchen car, as he ordered it quite some time ago. if you have not found a way to straighten up your outfit before now, he will chastise you for your unprofessionalism and you will gain a goal to tidy up. When this conversation concludes, you will also gain the goal to find a way into the kitchen car.

if you approach the rich undead as a wizard, he will be quite scared of you. If you press him for information, he will cave. However, eventually he will betray you...

if you approach the rich undead while cursed, he will laugh at you.


Other Notes:
What info do you need for mysteries in the mind palace?
    mystery name, mystery status (what step are you on?), mystery description (stored in its own library), player-associated clues, correct clues, red herrings, completion condition(?)
What info do you need when adding a new mystery to the player's active mysteries?
    is the mystery already in progress, at a later/earlier step, or completed? 
What info do you need when changing an active mystery to the next step?

mystery commands:
display mysteries in progress
display solved mysteries
select a mystery, also displays theories and clues for selected mystery as well as a brief summary
commit to a theory for a specified mystery (only used after a mystery has been selected)


The player's save file should ONLY show the name of each mystery chain and the step number. Gathered clues should be stored in a list with no extra information. All information regarding mysteries or clues can be fetched from game_data

mystery data is stored in its own dictionary, the mystery_library. This dictionary's keys hold sub-dictionaries representing the different mystery chains present in the game. within each mystery chain are the steps to its completion, which may branch based on the player's beliefs and choices. Each step has its own sub-sub-dictionary, which contains info like the name of the step, the log of events relevant to each mystery, the correct clues

Clues will be automatically associated with theories. It is the player's job to gather enough clues to get a decent understanding of how the evidence supports each theory. Each clue found will increase the player's anticipation when associated with a theory. Once they have gathered sufficient evidence, the player will be able to commit to a theory, gaining a decent amount of confidence. However if a clue is found that disproves a theory the player has committed to, they will lose confidence and convert their anticipation into surprise. This malus can be mitigated by having fully identified other theories. If the player tries to commit to a theory without enough evidence to validate their belief, they will instead develop a "hunch". When a player has a hunch, they will gain confidence for each clue already known as well as each new clue found that supports the hunched theory. However, if the hunch is definitively disproven, the confidence loss and surprise gain will be increased. This will create a risk-reward dynamic that encourages the player to hunch theories and win big as a stylish detective. However, the system also encourages the player to explore thoroughly as a dutiful gumshoe in order to keep themselves from suffering too great of losses.