# YaPMR - Yet another Paper Mario Randomizer

**Heavy WIP, doesn't randomize at the moment!**

My personal excursion into the worlds of Python and ROM hacking.

* Why create a randomizer for Paper Mario if there are already a bunch?

    Main reason: I wanted to play around with writing a randomizer myself from scratch.

* Wait, there are already other randomizer projects for Paper Mario?
    * https://github.com/JoshW-7/PaperMarioRandomizer/
    * https://github.com/MrCheeze/paper-mario-randomizer
    * https://github.com/Pronyo-Chan/paper-mario-randomizer  
    (Also check out the Paper Mario Modding discord!)

**Huge thanks to Clover and his StarRod tool for helping me a lot in understanding PM's ROM!**  
**Also thanks to MrCheeze and his PM rando project for giving me a starting point on ROM hacking with Python!**

## Current ToDo:

* Create a list of item checks, including items (single time and repeatable), keyItems, badges, star pieces, open shops (basic shops & badge shop), menu shops (Merlow's) and special items (boots/hammer upgrades, lucky star)

## Features:

* Implemented features:
    * Check ROM for validity
    * Disable dev logos, intro video, demo reel
* Features I want to implement (in this order):
    * Item randomization within the respective item pools (items, keyItems, badges)
    * Create patch files so a seed can be recreated from the base ROM
    * Option to output human-readable spoiler log file
    * Item randomization across item pools (including freestanding star pieces)
    * Make Goompa always give a useful badge which Mario's current badge points allow to equip
    * Basic keyItem placement logic to avoid softlocks
    * Item randomization including shops
    * 'Quick story' option to skip most of the gameplay-interrupting story parts
        * Includes skipping Peach interludes, minimizing the amount of speech bubbles during required story parts, setting different story bytes to avoid story parts and cutscenes without altering the story progression
    * Item randomization across item pools (including shops and all star pieces except for Chuck Quizmo's and Koopa Koot's)
    * 'Quick Bowser's Castle' option to make BC completely solved when Mario first enters it
* Features that would be cool and I want to include, but could proof very difficult to implement (in no particular order):
    * Lock battle RNG depending on seed (either once globaly or on a per-battle basis)
    * Either ensure through keyItem placement logic that you can never acquire more than 32 keyItems at once, or increase the size of the keyItem inventory
    * Randomize boots and hammer upgrades locations
    * Make boots and hammer upgrades progressive
    * Randomize partners amongst acquire partner locations
    * Turn partner acquiration into items and shuffle those into the item pool
    * 'Open story' mode: Re-write the story byte system to a per-chapter byte system so the chapters can be done out of order
        * Make star spirits either work out of order or make them progressive
        * Activate all blue warp pipes from the start
* Features that would be cool, but I'm not sure if I want to invest the time (in no particular order):
    * Create a proper User Interface for the randomizer
    * Chuck Quizmo
        * Force CQ to always spawn
        * Shuffle CQ star pieces into the item pool and allow CQ questions to give items other than star pieces
        * Not sure about this modification since one would just reload the map until all questions are answered, which could be quite the chore
    * Option to reenable cut items and badges
    * Option to modify starting items such as level, held items,keyItems,Badges, hammer and boots upgrades, star power, number of star pieces, partners
    * Option to modify badge's badge point cost
        * This is mainly for the idea of starting the game with a held Speedy Spin badge that costs zero badge points
    * Fix a few base game bugs (like Goombario's Multibonk cap, Sushi's Tidal Wave)
    * Option to shuffle bosses (within reason)
    * Option to randomize music
    * Option to randomize loading zones
    * Option to randomize battle formations (within reason)
    * Option to randomize enemy HP, attack and defense (within reason)
    * Create a sort of hint system for important items