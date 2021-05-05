from collections import OrderedDict

# Location describes the item location itself including the map-id
# Type is either Script, Shop or Collectable, the latter describing somewhat free-standing items which can
#   be picked up by touching them
# ItemAdresses are the locations in ROM where the item-id for a location is stored. Generally, 'Collectable' items
#   have only a single ItemAdress, while 'Script' items have multiple
#   Note: Entries in ItemAdresses are ordered, which is important for setting Star Pieces via Script correctly
# FuncAdress is the location in ROM where a sub-script is called to add an item to Marios inventory.
#   These sub-scripts are addItem, addKeyItem, addBadge, addCoin, addStarpiece and have to be modified
#   depending on the item put there
# Repeatable states whether or not an item location can be checked more than once
# VanillaItem states which item is found at this location in the vanilla game

vanilla_locations = OrderedDict([
#   Location                                                     Type            ItemAdresses          FuncAdress   Repeatable VanillaItem

## kmr: Goomba Region
#   ("(kmr_00) Forest Clearing: Hidden Panel",                   ("TODO",        (?,),                 None,        False,     "Star Piece (1)")),

    ("(kmr_04) Jr. Troopa's Playground: Tree Near Exit",         ("Collectable", (0x8cdc24,),          None,        False,     "Dolly")),
#   ("(kmr_04) Jr. Troopa's Playground: Mid West Bush",          ("Script",      (?,),                 None,        False,     "Hammer")),

    ("(kmr_02) Goomba Village: Goompa Reward",                   ("Script",      (0x8baafc,0x8bab28),  (0x8bab24,), False,     "Power Jump")),
    ("(kmr_02) Goomba Village: Goompa: Koopa Koot Favor",        ("Script",      (0x8bb73c,0x8bb768),  (0x8bb764,), False,     "Tape")),
#   ("(kmr_02) Goomba Village: Give Goompapa Letter 1",          ("Script",      (?,),                 None,        False,     "Letter (13)")),
    ("(kmr_02) Goomba Village: Give Goompapa Letter 2",          ("Script",      (0x8b899c,0x8b89c8),  (0x8b89c4,), False,     "Lucky Day")),
    ("(kmr_02) Goomba Village: Goombaria's Dolly",               ("Script",      (0x8ba444,0x8ba470,
                                                                                  0x8b9058,0x8b9084),  (0x8ba46c,
                                                                                                        0x8b9080,), False,     "Star Piece (1)")),
    ("(kmr_02) Goomba Village: Veranda",                         ("Collectable", (0x8c519c,),          None,        False,     "Shooting Star")),
    ("(kmr_02) Goomba Village: Tree Near Fencegate",             ("Collectable", (0x8c7a20,),          None,        True,      "Goomnut")),
#   ("(kmr_02) Goomba Village: Chuck Quizmo",                    ("Script",      (?,),                 None,        False,     "Star Piece (1)")),

    ("(kmr_03) Bottom of the Cliff: Grey Block Hidden ? Block",  ("Collectable", (0x8c9598,),          None,        False,     "Repel Gel")),
    ("(kmr_03) Bottom of the Cliff: On Spring Ledge",            ("Collectable", (0x8c96f4,),          None,        False,     "Fire Flower")),
    ("(kmr_03) Bottom of the Cliff: Tree Near Yellow Block",     ("Collectable", (0x8ca1b8,0x8ca1e4),  None,        False,     "Mushroom")),

    ("(kmr_05) Behind the Village: End Of Upper Ledge",          ("Collectable", (0x8d090c,),          None,        False,     "Star Piece (1)")),

    ("(kmr_06) Goomba Road 2: Wooden Sign",                      ("Collectable", (0x8d3c70,),          None,        False,     "Mushroom")),
    ("(kmr_06) Goomba Road 2: Red ? Block",                      ("Collectable", (0x8d3b04,),          None,        False,     "Close Call")),

    ("(kmr_11) Goomba King's Castle: Tree Left Of Castle",       ("Collectable", (0x8e0f20,),          None,        False,     "Star Piece (1)")),
    ("(kmr_11) Goomba King's Castle: Hammerblock",               ("Collectable", (0x8dff60,0x8e0124),  None,        False,     "Super Shroom")),

    ("(kmr_10) Toad Town Entrance: Tree",                        ("Collectable", (0x8d9578,),          None,        False,     "Sleepy Sheep")),
    ("(kmr_10) Toad Town Entrance: Chest On Roof",               ("Collectable", (0x8d9518,),          None,        False,     "Hammer Throw")),

#   ("(kmr_20) Mario's House: Luigi: Koopa Koot Favor",          ("Script", (?,),          None,        False,     "Autograph (L)")),

## mac: Toad Town
    ("(mac_00) Gate District: Sushie Swim",                      ("Collectable", (0x7efffc,),          None,        False,     "Star Piece (1)")),
    ("(mac_00) Gate District: Return Stolen Dictionary",         ("Script",      (0x7f468c,0x7f46b8),  (0x7f46b4,), False,     "Star Piece (1)")),
#   ("(mac_00) Gate District: Give Miss T. Letter (18)",         ("Script", (?,),          None,        False,     "Letter (19)")),
#   ("(mac_00) Gate District: Hidden Panel",                      ("TODO", (?,),          None,        False,     "Star Piece (1)")),
#   ("(mac_00) Gate District: Shop Item 1",                      ("Shop",        (0x7f8f7c,),          None,        True,      "Fright Jar")),
#   ("(mac_00) Gate District: Shop Item 2",                      ("Shop",        (0x7f8f88,),          None,        True,      "Sleepy Sheep")),
#   ("(mac_00) Gate District: Shop Item 3",                      ("Shop",        (0x7f8f94,),          None,        True,      "POW Block")),
#   ("(mac_00) Gate District: Shop Item 4",                      ("Shop",        (0x7f8fa0,),          None,        True,      "Fire Flower")),
#   ("(mac_00) Gate District: Shop Item 5",                      ("Shop",        (0x7f8fac,),          None,        True,      "Honey Syrup")),
#   ("(mac_00) Gate District: Shop Item 6",                      ("Shop",        (0x7f8fb8,),          None,        True,      "Mushroom")),

    ("(mac_01) Plaza District: Tree Left Of Merlon's",           ("Collectable", (0x822dc8,),          None,        False,     "Star Piece (1)")),
    ("(mac_01) Plaza District: Spin Jumps Inside Merlon's",      ("Collectable", (0x81086c,0x810afc),  None,        False,     "Quick Change")),
#   ("(mac_01) Plaza District: Return Stolen Calculator",        ("TODO",        (?),  None,        False,     "I Spy")),
#   ("(mac_01) Plaza District: Return Stolen Mailbag",           ("TODO",        (?),  None,        False,     "Star Piece (1)")),
#   ("(mac_01) Plaza District: Letter To Merlon",                ("TODO",        (?),  None,        False,     "Star Piece (1)")),
#   ("(mac_01) Plaza District: Chuck Quizmo",                    ("Collectable", (?,),          None,        False,     "Star Piece (1)")),

#   ("(mac_02) Southern District: Inside Odd House",             ("TODO",        (0x828f10,0x829150),  None,        False,     "Odd Key")),
#   ("(mac_02) Southern District: Bub-ulb",                      ("Script",      (0x82fbc4,),          None,        False,     "Magical Seed 1")),
#   ("(mac_02) Southern District: Tayce T.s Reward For Pan",     ("TODO",        (0x82c5b4,0x82c778),  None,        False,     "Cake")),
#   ("(mac_02) Southern District: Fice T.s Reward For Letter",   ("TODO",        (?),  None,        False,     "Star Piece (1)")),

#   ("(mac_03) Station District: Give Dane T. Letter (20)",      ("TODO",        (?),  None,        False,     "Letter (21)")),
#   ("(mac_03) Station District: Give Dane T. Letter (22)",      ("TODO",        (?),  None,        False,     "Letter (23)")),

#   ("(mac_04) Residental District: Shop Storeroom Item 1",      ("Shop",        (?,),          None,        False,     "Snowman Doll")),
#   ("(mac_04) Residental District: Shop Storeroom Item 2",      ("Shop",        (?,),          None,        False,     "Volt Shroom")),
    ("(mac_04) Residental District: Shop Storeroom Item 3",      ("Shop",        (0x8493f8,0x849820),  None,        False,     "Toy Train")),
#   ("(mac_04) Residental District: Shop Storeroom Item 4",      ("Shop",        (?,),          None,        False,     "Dizzy Dial")),
#   ("(mac_04) Residental District: Shop Item 1",                ("Shop",        (0x84683c,),          None,        True,      "Stone Cap")),
#   ("(mac_04) Residental District: Shop Item 2",                ("Shop",        (0x846848,),          None,        True,      "Dizzy Dial")),
#   ("(mac_04) Residental District: Shop Item 3",                ("Shop",        (0x846854,),          None,        True,      "Thunder Rage")),
#   ("(mac_04) Residental District: Shop Item 4",                ("Shop",        (0x846860,),          None,        True,      "Tasty Tonic")),
#   ("(mac_04) Residental District: Shop Item 5",                ("Shop",        (0x84686c,),          None,        True,      "Volt Shroom")),
#   ("(mac_04) Residental District: Shop Item 6",                ("Shop",        (0x846878,),          None,        True,      "Super Shroom")),

#   ("(mac_05) Port District: Talk To Writer In Bar",            ("Script",      (0x85fa8c,),          None,        True,      "Lyrics")),
#   ("(mac_05) Port District: Give Melody To Writer In Bar",     ("Script",      (?,),          None,        True,      "Attack FX D")),
#   ("(mac_05) Port District: Give Fishmael Letter (15)",     ("Script",      (?,),          None,        True,      "Letter (16)")),

## osr: Peach's Castle Grounds
#   ("(osr_01) Ruined Castle Grounds: Give Toad Letter (13)",    ("Script",      (?),  None,        False,     "Letter (14)")),

## hos: Shooting Star Summit
#   ("(hos_00) Shooting Star Path: Given By Twink",              ("Script", (?,),          None,        False,     "Lucky Star")),

    ("(hos_01) Shooting Star Summit: Behind Summit",             ("Collectable", (0xa158a4,),          None,        False,     "Star Piece (1)")),

    ("(hos_06) Merluvlee's House: Merluvlee - Koopa Koot Favor", ("Collectable", (0xa3ecfc,),          None,        False,     "Autograph (M)")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 01 ( 1 SP)",     ("TODO",        (?,),                 None,        False,     "Attack FX A")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 02 ( 1 SP)",     ("TODO",        (?,),                 None,        False,     "Pay-Off")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 03 ( 3 SP)",     ("TODO",        (?,),                 None,        False,     "Chill Out")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 04 ( 5 SP)",     ("TODO",        (?,),                 None,        False,     "Pretty Lucky")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 05 ( 5 SP)",     ("TODO",        (?,),                 None,        False,     "Feeling Fine")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 06 ( 8 SP)",     ("TODO",        (?,),                 None,        False,     "Happy Heart")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 07 ( 8 SP)",     ("TODO",        (?,),                 None,        False,     "Happy Flower")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 08 (10 SP)",     ("TODO",        (?,),                 None,        False,     "Peekaboo")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 09 (10 SP)",     ("TODO",        (?,),                 None,        False,     "Zap Tap")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 10 (12 SP)",     ("TODO",        (?,),                 None,        False,     "Heart Finder")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 11 (12 SP)",     ("TODO",        (?,),                 None,        False,     "Flower Finder")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 12 (15 SP)",     ("TODO",        (?,),                 None,        False,     "HP Drain")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 13 (20 SP)",     ("TODO",        (?,),                 None,        False,     "Money Money")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 14 (25 SP)",     ("TODO",        (?,),                 None,        False,     "Flower Saver")),
#   ("(hos_06) Merluvlee's House: Merlows Badge 15 (25 SP)",     ("TODO",        (?,),                 None,        False,     "Power Plus")),

## tik: Toad Town Tunnels
    ("(tik_18) Hall to Blooper 1 (B1): Hidden ? Block",          ("Collectable", (0x89748c,),          None,        False,     "Super Shroom")),
    ("(tik_02) Blooper Boss 1 (B1): Chest",                      ("Collectable", (0x86d958,),          None,        False,     "Shrink Stomp")),
    ("(tik_03) Short Elevator Room (B1): Center ? Block",        ("Collectable", (0x871750,),          None,        False,     "Snowman Doll")),
    ("(tik_05) Spring Room (B2): Chest On Ledge",                ("Collectable", (0x876900,),          None,        False,     "Power Smash")),
    ("(tik_07) Elevator Attic Room (B2): Parakarry Ledge",       ("Collectable", (0x87dc24,),          None,        False,     "Star Piece (1)")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 01",           ("Script", (?,),          None,        False,     "Star Piece (1)")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 02",           ("Script", (?,),          None,        False,     "Life Shroom")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 03",           ("Script", (?,),          None,        False,     "Bump Attack")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 04",           ("Script", (?,),          None,        False,     "Repel Gel")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 05",           ("Script", (?,),          None,        False,     "Star Piece (1)")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 06",           ("Script", (?,),          None,        False,     "Super Shroom")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 07",           ("Script", (?,),          None,        False,     "Mushroom")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 08",           ("Script", (?,),          None,        False,     "Dried Shroom")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 09",           ("Script", (?,),          None,        False,     "Dried Shroom")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 10",           ("Script", (?,),          None,        False,     "Star Piece (1)")),
#   ("(tik_15) Rip Cheato's Home (B3): Rips Offer 11+",          ("Script", (?,),          None,        True,      "Dried Shroom")),
    ("(tik_20) Room with Spikes (B2): ? Block",                  ("Collectable", (0x89d6f0,),          None,        False,     "Shooting Star")),
    ("(tik_23) Windy Path (B3): Central Hidden Block",           ("Collectable", (0x8a5264,),          None,        False,     "Maple Syrup")),
    ("(tik_23) Windy Path (B3): Right Hidden Block",             ("Collectable", (0x8a529c,),          None,        False,     "Stop Watch")),
    ("(tik_23) Windy Path (B3): Left Hidden Block",              ("Collectable", (0x8a52d4,),          None,        False,     "Volt Shroom")),
    ("(tik_24) Hall to Ultra Boots (B3): Hidden Block",          ("Collectable", (0x8a78ec,),          None,        False,     "Life Shroom")),
#   ("(tik_25) Ultra Boots Room (B3): Big Chest",                ("Script",      (?,),          None,        False,     "Ultra Boots")),

## nok: Koopa Region
    ("(nok_11) Pleasant Path Entry: 2nd Yellow ? Block",         ("Collectable", (0x9f7150,),          None,        False,     "Fright Jar")),
    ("(nok_11) Pleasant Path Entry: Red ? Block",                ("Collectable", (0x9f70d0,),          None,        False,     "Dizzy Attack")),

    ("(nok_12) Pleasant Path Bridge: Yellow ? Block",            ("Collectable", (0x9fd2c0,),          None,        False,     "POW Block")),
    ("(nok_12) Pleasant Path Bridge: Behind Fence",              ("Collectable", (0x9fd3dc,),          None,        False,     "Sleepy Sheep")),
    ("(nok_12) Pleasant Path Bridge: Lonely Island",             ("Collectable", (0x9fd3b8,),          None,        False,     "Star Piece (1)")),

    ("(nok_13) Pleasant Crossroads: Behind Cane",                ("Collectable", (0xa023f0,),          None,        False,     "Honey Syrup")),
#   ("(nok_13) Pleasant Crossroads: Brown Block Secret",         ("TODO",        (0xa02164,0xa0238c),  None,        False,     "Attack FX B")),

#   ("(nok_01) Koopa Village 1: In Lower Right Bush",            ("TODO",        (0x9d6a48,),          None,        False,     "Dried Shroom")),
#   ("(nok_01) Koopa Village 1: In Third Right Bush",            ("TODO",        (0x9d6a80,),          None,        True,      "Koopa Leaf")),
#   ("(nok_01) Koopa Village 1: Give Koover Letter (14)",        ("TODO",        (?,),          None,        True,      "Letter (15)")),
#   ("(nok_01) Koopa Village 1: Give Koover Letter (16)",        ("TODO",        (?,),          None,        True,      "Letter (17)")),
#   ("(nok_01) Koopa Village 1: Rightmost Bush Koopa Koot Favor",("Script",      (?,),          None,        True,      "Empty Wallet")),
#   ("(nok_01) Koopa Village 1: Shop Item 1",                    ("Shop",        (0x9d4f4c,),          None,        True,      "Dizzy Dial")),
#   ("(nok_01) Koopa Village 1: Shop Item 2",                    ("Shop",        (0x9d4f58,),          None,        True,      "POW Block")),
#   ("(nok_01) Koopa Village 1: Shop Item 3",                    ("Shop",        (0x9d4f64,),          None,        True,      "Fire Flower")),
#   ("(nok_01) Koopa Village 1: Shop Item 4",                    ("Shop",        (0x9d4f70,),          None,        True,      "Honey Syrup")),
#   ("(nok_01) Koopa Village 1: Shop Item 5",                    ("Shop",        (0x9d4f7c,),          None,        True,      "Volt Shroom")),
#   ("(nok_01) Koopa Village 1: Shop Item 6",                    ("Shop",        (0x9d4f88,),          None,        True,      "Mushroom")),
#   ("(nok_01) Koopa Village 1: Chuck Quizmo",                   ("Script",      (?,),                 None,        False,     "Star Piece (1)")),

    ("(nok_02) Koopa Village 2: Push Block Puzzle",              ("Collectable", (0x9dce20,),          None,        False,     "Star Piece (1)")),
#   ("(nok_02) Koopa Village 2: Mrs Kolorado: Koopa Koot Favor", ("Script",      (0x9e5644,),          None,        False,     "Koopa Legends")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 2 (Sleepy)",    ("Script",      (0x9e9d3c,),          None,        False,     "Silver Credit")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 4 (Tea)",       ("Script",      (?,),                 None,        False,     "Star Piece (3)")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 8 (Autograph)", ("Script",      (?,),                 None,        False,     "Star Piece (3)")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 10 (Life)",     ("Script",      (0x9e9da4,),          None,        False,     "Gold Credit")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 12 (Bob-ombs)", ("Script",      (?,),                 None,        False,     "Star Piece (3)")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 16 (Lime)",     ("Script",      (?,),                 None,        False,     "Star Piece (3)")),
#   ("(nok_02) Koopa Village 2: Koopa Koot Favor 20 (Red Jar)",  ("Script",      (?,),                 None,        False,     "Star Piece (3)")),
#   ("(nok_02) Koopa Village 2: Chuck Quizmo",                   ("Script",      (?,),                 None,        False,     "Star Piece (1)")),

    ("(nok_03) Behind Koopa Village: Ontop Of Block",            ("Collectable", (0x9ecb9c,),          None,        False,     "HP Plus 2")),
    
#   ("(nok_04) Fuzzy Forest: Fuzzies",                           ("Script",      (0x9f0f64,0x9f32e4),  None,        False,     "Kooper's Shell")),

    ("(nok_14) Path to Fortress 1: Ontop of Block",              ("Collectable", (0xa056bc,),          None,        False,     "Thunder Bolt")),
    ("(nok_14) Path to Fortress 1: Hidden ? Block",              ("Collectable", (0xa05728,),          None,        False,     "Fire Flower")),

#   ("(nok_15) Path to Fortress 2: Tree",                        ("TODO",        (0xa0bb38,),          None,        False,     "Star Piece (1)")),

## trd: Koopa Bros. Fortress
    ("(trd_00) Fortress Exterior: Far Right Cracked Wall",       ("Collectable", (0x99b108,),          None,        False,     "Refund")),
#   ("(trd_00) Fortress Exterior: Chest On Ledge",               ("TODO", (0x99b154,),          None,        False,     "FP Plus 2")),

#   ("(trd_01) Left Tower: Defeat Koopa",                        ("?", (?,),          None,        False,     "Fortress Key")),
    ("(trd_01) Left Tower: F2 Far Left Pedestal",                ("Collectable", (0x99fcfc,),          None,        False,     "Smash Charge")),

# all the keys ??

#   ("(trd_03) Central Hall: Inside left Cell",                  ("Collectable", (?,),          None,        False,     "Fortress Key")),
    ("(trd_03) Central Hall: Inside middle Cell",                ("Collectable", (0x9a60bc,),          None,        False,     "Power Bounce")),
#   ("(trd_03) Central Hall: Inside right Cell",                 ("Collectable", (?,),          None,        False,     "Fortress Key")),

    ("(trd_08) Dungeon Fire Room: On Pedestal",                  ("Collectable", (0x9bc16c,),          None,        False,     "Fortress Key")),

    ("(trd_09) Battlement: Block Behind Boulder",                ("Collectable", (0x9bde54,),          None,        False,     "Maple Syrup")),

## iwa: Mt Rugged
    ("(iwa_10) Train Station: Inside Center Back Bush",          ("Collectable", (0x9268c8,),          None,        True,      "Egg")),

    ("(iwa_00) Mt Rugged 1: ? Block",                            ("Collectable", (0x90d358,),          None,        False,     "Sleepy Sheep")),
    ("(iwa_00) Mt Rugged 1: Hitting Whacka",                     ("Collectable", (0x90ebd4,),          None,        True,      "Whacka's Bump")),

    ("(iwa_01) Mt Rugged 2: Kooper Ledge",                       ("Collectable", (0x913004,),          None,        False,     "Letter (01)")),
    ("(iwa_01) Mt Rugged 2: Parakarry Ledge",                    ("Collectable", (0x912fe0,),          None,        False,     "Quake Hammer")),
    
    ("(iwa_02) Mt Rugged 3: On Wooden Scaffolding",              ("Collectable", (0x9171f4,),          None,        False,     "Star Piece (1)")),
#   ("(iwa_02) Mt Rugged 3: Parakarry Ledge",                    ("Script",      (0x9186c4,),          None,        False,     "Magical Seed 2")),

    ("(iwa_03) Mt Rugged 4: Floating Yellow ? Block",            ("Collectable", (0x91a494,),          None,        False,     "Mushroom")),
#   ("(iwa_03) Mt Rugged 4: Hidden Cave Chest",                  ("Collectable", (0x91a3ac,),          None,        False,     "Damage Dodge 2")),
    ("(iwa_03) Mt Rugged 4: Far Left Platform",                  ("Collectable", (0x91a514,),          None,        False,     "Star Piece (1)")),
    ("(iwa_03) Mt Rugged 4: Top Right Grounded ? Block",         ("Collectable", (0x91a4cc,),          None,        False,     "Honey Syrup")),
    ("(iwa_03) Mt Rugged 4: Cliff Slide Jump Onto Ledge",        ("Collectable", (0x91a4f0,),          None,        False,     "Letter (25)")),
    
    ("(iwa_04) Suspension Bridge: Bottom Of CLiff",              ("Collectable", (0x91cf70,),          None,        False,     "Letter (10)")),

## dro: Dry Dry Outpost
#   ("(dro_01) Outpost 1: Give Lyrics To Composer",              ("Script",      (0x964334,),          None,        True,      "Melody")),
#   ("(dro_01) Outpost 1: Give Mouser Letter (19)",              ("Script",      (?,),          None,        True,      "Letter (12)")),
#   ("(dro_01) Outpost 1: Shop Item 1",                          ("Collectable", (0x9666fc,),          None,        True,      "Thunder Bolt")),
#   ("(dro_01) Outpost 1: Shop Item 2",                          ("Collectable", (0x966708,),          None,        True,      "Dusty Hammer")),
#   ("(dro_01) Outpost 1: Shop Item 3",                          ("Collectable", (0x966714,),          None,        True,      "Honey Syrup")),
#   ("(dro_01) Outpost 1: Shop Item 4",                          ("Collectable", (0x966720,),          None,        True,      "Dried Shroom")),
#   ("(dro_01) Outpost 1: Shop Item 5",                          ("Collectable", (0x96672c,),          None,        True,      "Dried Pasta")),
#   ("(dro_01) Outpost 1: Shop Item 6",                          ("Collectable", (0x966738,),          None,        True,      "Mushroom")),

    ("(dro_02) Outpost 2: Ontop Of Roof",                        ("Collectable", (0x96cd9c,),          None,        False,     "Letter (08)")),
#   ("(dro_02) Outpost 2: Moustafas Gift",                       ("Script",      (0x976048,),          None,        False,     "Pulse Stone")),
#   ("(dro_02) Outpost 2: Give Mr. E. Letter (17)",              ("Script",      (?,),          None,        False,     "Letter (18)")),
#   ("(dro_02) Outpost 2: Chuck Quizmo",                         ("Collectable", (?,),          None,        False,     "Star Piece (1)")),

## sbk: Dry Dry Desert
    ("(sbk_20) N1W3 Special Block: ? Block 1 Hit",               ("Collectable", (0x938abc,0x938cf8),  None,        False,     "Mushroom")),
    ("(sbk_20) N1W3 Special Block: ? Block 10 Hits",             ("Collectable", (0x938b8c,0x938d48),  None,        False,     "Super Shroom")),
    ("(sbk_20) N1W3 Special Block: ? Block 100 Hits",            ("Collectable", (0x938c5c,0x938d98),  None,        False,     "Ultra Shroom")),
    ("(sbk_22) N1W1: Center ? Block",                            ("Collectable", (0x93a710,),          None,        False,     "Fire Flower")),
    ("(sbk_24) N1E1 Palm Trio: Palm Trio Hidden Block",          ("Collectable", (0x93b740,),          None,        False,     "Runaway Pay")),
#   ("(sbk_30) W3 Kolorado's Camp: Hand In Artifact",            ("Script", (,),          None,        False,     "Star Piece (1)")),
#   ("(sbk_45) E1 Nomadimouse: Letter for Nomadimous",           ("Script", (?,),          None,        False,     "Star Piece (1)")),
    ("(sbk_45) S1E2 Small Bluffs: Ontop Of Floating Block",      ("Collectable", (0x94e934,),          None,        False,     "Stop Watch")),
    ("(sbk_45) S1E2 Small Bluffs: Tweester Rock",                ("Collectable", (0x94e958,),          None,        False,     "Spin Attack")),
    ("(sbk_55) S2E2 West of Oasis: Behind Bush",                 ("Collectable", (0x953f70,),          None,        False,     "Tasty Tonic")),
    ("(sbk_56) S2E3 Oasis: Left Tree",                           ("Collectable", (0x956438,),          None,        True,      "Lemon")),
    ("(sbk_56) S2E3 Oasis: Right Tree",                          ("Collectable", (0x95648c,),          None,        True,      "Lime")),
    ("(sbk_61) S3W2 Hidden AttackFX: Boulder Hidden Block",      ("Collectable", (0x957300,),          None,        False,     "Attack FX C")),

## isk: Dry Dry Ruins
    ("(isk_02) Sarcophagus Hall 1: Inside Sarcophagus",          ("Collectable", (0x9791a4,),          None,        False,     "Spike Shield")),
    ("(isk_03) Sand Drainage Room 1: On Pedestal",               ("Collectable", (0x978b80,),          None,        False,     "Ruins Key")),
    ("(isk_05) Pyramid Stone Room: Behind The Grey Block",       ("Collectable", (0x97fd0c,),          None,        False,     "Pyramid Stone")),
    ("(isk_06) Sand Drainage Room 2: On Pedestal",               ("Collectable", (0x980d70,),          None,        False,     "Ruins Key")),
    ("(isk_06) Sand Drainage Room 2: Bellow The Sand",           ("Collectable", (0x980d4c,),          None,        False,     "Star Piece (1)")),
#   ("(isk_07) Sarcophagus Hall 2: Defeat The Ambush",           ("Collectable", (?,),          None,        False,     "Ruins Key")),
    ("(isk_07) Sarcophagus Hall 2: Behind The Grey Block",       ("Collectable", (0x982c74,),          None,        False,     "Artifact")),
#   ("(isk_09) Super Hammer Room: Hidden Room Chest",            ("Collectable", (0x986f48,),          None,        False,     "Slow Go")),
#   ("(isk_09) Super Hammer Room: Big Chest",                    ("Script",      (?,),          None,        False,     "Super Hammer")),
    ("(isk_12) Sand Drainage Room 3: Behind The Grey Block",     ("Collectable", (0x98dc80,),          None,        False,     "Ruins Key")),
    ("(isk_13) Lunar Stone Room: Behind The Grey Block",         ("Collectable", (0x991abc,),          None,        False,     "Lunar Stone")),
    ("(isk_14) Diamond Stone Room: Behind The Grey Block",       ("Collectable", (0x994714,),          None,        False,     "Diamond Stone")),

## mim: Forever Forest
#   ("(mim_04) Tree Face (Bub-ulb): Talk To Bub-ulb",            ("Script", (0xba00bc,),          None,        False,     "Magical Seed 3")),
    ("(mim_09) Flowers Appear (FP Plus): ? Block in Center",     ("Collectable", (0xbb4150,),          None,        False,     "FP Plus")),
    ("(mim_11) Outside Boo's Mansion: ? Block On The Right",     ("Collectable", (0xbba2b0,),          None,        False,     "Volt Shroom")),
    ("(mim_11) Outside Boo's Mansion: Bushes Farthest Right",    ("Collectable", (0xbbb210,),          None,        True,      "Strange Leaf")),
#   ("(mim_12) Exit to Gusty Gulch: Hidden Panel",               ("Collectable", (?,),          None,        False,      "Star Piece (1)")),

## obk: Boo's Mansion
#   ("(obk_01) Foyer: Give Franky Letter (12)",                  ("Script", (?,),          None,        False,      "Letter (20)")),
#   ("(obk_07) Record Player Room: Guarded Chest",               ("Collectable", (0xbd0cf8,),          None,        False,      "Weight")),
#   ("(obk_08) Record Room: Play With The Boos",                 ("Collectable", (?,),          None,        False,      "Record")),
#   ("(obk_02) Basement Stairs: Hidden Panel",                   ("Collectable", (?,),          None,        False,      "Star Piece (1)")),
#   ("(obk_04) Super Boots Room: Big Chest Boo Game",            ("Script", (?,),          None,        False,      "Super Boots")),
#   ("(obk_04) Super Boots Room: Hidden Panel",                  ("Collectable", (?,),          None,        False,      "Star Piece (1)")),
    ("(obk_04) Super Boots Room: Inside Storage Crate",          ("Collectable", (0xbc8f68,),          None,        False,      "Maple Syrup")),
#   ("(obk_03) Basement: Inside Storage Crate",                  ("Collectable",        (?),  None,        False,      "Super Shroom")),
#   ("(obk_03) Basement: Shop Item 1",                           ("Shop",        (?),  None,        True,      "Super Shroom")),
#   ("(obk_03) Basement: Shop Item 2",                           ("Shop",        (0xbc57fc,),  None,        True,      "Life Shroom")),
#   ("(obk_03) Basement: Shop Item 3",                           ("Shop",        (0xbc57f0,),  None,        True,      "Maple Syrup")),
#   ("(obk_03) Basement: Shop Item 4",                           ("Shop",        (0xbc57e4,),  None,        True,      "Snowman Doll")),
#   ("(obk_03) Basement: Shop Item 5",                           ("Shop",        (0xbc57d8,),  None,        True,      "Stop Watch")),
#   ("(obk_03) Basement: Shop Item 6",                           ("Shop",        (0xbc57cc,),  None,        True,      "Mystery?")),
    ("(obk_06) Library: Ontop Of Bookshelf",                     ("Collectable", (0xbceaec,),  None,        False,      "Boo's Portrait")),
    ("(obk_06) Library: Inside Storage Crate",                   ("Collectable", (0xbcebb4,),  None,        False,      "Star Piece (1)")),

## arn: Gusty Gulch
    ("(arn_02) Wasteland Ascent 1: Kooper Ledge",                ("Collectable", (0xbde48c,),  None,        False,      "Dizzy Dial")),
    ("(arn_02) Wasteland Ascent 1: Foreground ? Block",          ("Collectable", (0xbde558,),  None,        False,      "Repel Gel")),
    ("(arn_02) Wasteland Ascent 1: On The Ground",               ("Collectable", (0xbde4b0,),  None,        False,      "Letter (07)")),
    ("(arn_04) Wasteland Ascent 2: ? Block",                     ("Collectable", (0xbe7810,),  None,        False,      "Super Shroom")),
    ("(arn_04) Wasteland Ascent 2: Behind Rock",                 ("Collectable", (0xbe78a0,),  None,        False,      "Star Piece (1)")),

## dgb: Tubba's Castle
    ("(dgb_07) Study (1F): Ontop Of Huge Table",                 ("Collectable", (0xc3f35c,),  None,        False,      "Star Piece (1)")),
#   ("(dgb_06) Basement: In Chest",                              ("Collectable", (0xc3d7f8,),  None,        False,      "Castle Key (T)")),
    ("(dgb_11) Covered Tables Room (1F): Ontop Huge Table",      ("Collectable", (0xc4de70,),  None,        False,      "D-Down Jump")),
#   ("(dgb_12) Spike Trap Room (2F): In Chest",                  ("Collectable", (0xc4e8b8,),  None,        False,      "Castle Key (T)")),
    ("(dgb_13) Hidden Bedroom (2F): Bookshelf Hiding Spot",      ("Collectable", (0xc4ebdc,),  None,        False,      "Mega Rush")),
    ("(dgb_03) Table/Clock Room (1/2F): Ontop Huge Table",       ("Collectable", (0xc34e1c,),  None,        False,      "Star Piece (1)")),
    ("(dgb_14) Stairs to Third Floor: ? Block",                  ("Collectable", (0xc4f4d0,),  None,        False,      "Maple Syrup")),
    ("(dgb_16) Sleeping Clubbas Room (3F): On Pedestal",         ("Collectable", (0xc53ccc,),  None,        False,      "Castle Key (T)")),
#   ("(dgb_18) Master Bedroom (3F): In Chest",                   ("Script", (0xc59788,),  None,        False,      "Mystical Key")),

## omo: Shy Guy's Toybox
#   ("(omo_01) BLU Large Playroom: Leftmost Shyguy",             ("Collectable", (0xd9d27c,),  None,        False,      "Calculator")),
#   ("(omo_13) BLU Anti-Guy Hall: Anti-Guy Chest",               ("Collectable", (0xde5258,),  None,        False,      "Power Plus 2")),
# omo_01 2x Cake Mix, 1x Mushroom, 1x Fire Flower ??
#   ("(omo_04) BLU Block City: Ontop Of Building",               ("Collectable", (0xdb02a4,0xdb02c8??),  None,        False,      "Star Piece (1)")),
#   ("(omo_04) BLU Block City: Behind Green Building Block",     ("Collectable", (0xdb02a4,0xdb02c8??),  None,        False,      "Star Piece (1)")),
    ("(omo_04) BLU Block City: Upper ? Block",                   ("Collectable", (0xdb0160,),  None,        False,      "Thunder Bolt")),
#   ("(omo_04) BLU Block City: Guarded Chest",                   ("Collectable", (0xdafb88,),  None,        False,      "Storeroom Key")),
#   ("(omo_04) BLU Block City: Chest Guard",                     ("Collectable", (?,),  None,        False,      "Mushroom")),
#   ("(omo_06) PNK Station: In Chest",                           ("Collectable", (0xdbd128,),  None,        False,      "Mailbag")),
#   ("(omo_06) PNK Station: Hidden Panel",                       ("Collectable", (?,),  None,        False,      "Star Piece (1)")),
#   ("(omo_07) PNK Playhouse: Far Left Chest",                   ("Collectable", (0xdc3264,),  None,        False,      "Defend Plus")),
#   ("(omo_07) PNK Playhouse: Central Chest",                    ("Collectable", (0xdc32b0,),  None,        False,      "Ice Power")),
#   ("(omo_07) PNK Playhouse: Guarded Chest",                    ("Collectable", (0xdc3208,),  None,        False,      "Frying Pan")),
#   ("(omo_07) PNK Playhouse: Chest Guard",                      ("Collectable", (?,),  None,        False,      "Thunder Rage")),
#   ("(omo_05) PNK Gourmet Guy Crossing: Give Gourmet Guy Cake", ("Collectable", (0xdb69e8,0xdb74ac),  None,        False,      "Cookbook")),
    ("(omo_05) PNK Gourmet Guy Crossing: Hidden ? Block",        ("Collectable", (0xdb74f4,),  None,        False,      "Dizzy Dial")),
#   ("(omo_09) GRN Treadmills/Slot Machine: Defeat Shyguy",      ("Collectable", (0xdd4114,),  None,        False,      "Mystery Note")),
    ("(omo_09) GRN Treadmills/Slot Machine: Inside Building",    ("Collectable", (0xdd3f6c,),  None,        False,      "Star Piece (1)")),
#   ("(omo_09) GRN Treadmills/Slot Machine: Guarded Chest",      ("Collectable", (0xdd3e38,),  None,        False,      "Dictionary")),
#   ("(omo_09) GRN Treadmills/Slot Machine: Chest Guard",        ("Collectable", (?,),  None,        False,      "Super Soda")),
    ("(omo_10) RED Station: Hidden ? Block",                     ("Collectable", (0xddc740,),  None,        False,      "Super Shroom")),
    ("(omo_11) RED Moving Platforms: Right Hidden ? Block",      ("Collectable", (0xdded70,),  None,        False,      "Volt Shroom")),
    ("(omo_11) RED Moving Platforms: Central Hidden ? Block",    ("Collectable", (0xddee18,),  None,        False,      "Deep Focus 2")),
    ("(omo_11) RED Moving Platforms: Left Hidden ? Block",       ("Collectable", (0xddeda8,),  None,        False,      "Snowman Doll")),
    ("(omo_02) RED Boss Barricade: Ontop Of Floating Block",     ("Collectable", (0xda0550,),  None,        False,      "Shooting Star")),
    ("(omo_02) RED Boss Barricade: Yellow ? Block",              ("Collectable", (0xda04d0,),  None,        False,      "Sleepy Sheep")),

## jan Jade Jungle
    ("(jan_00) Whale Cove: Behind Bush",                         ("Collectable", (0xb25e04,),  None,        False,      "Stop Watch")),
    ("(jan_00) Whale Cove: Palm Tree",                           ("Collectable", (0xb27f2c,),  None,        True,       "Coconut")),

    ("(jan_01) Beach: On The Rocks",                             ("Collectable", (0xb2b43c,),  None,        False,      "Letter (11)")),
    ("(jan_01) Beach: Left Hidden Block",                        ("Collectable", (0xb2b498,),  None,        False,      "Repel Gel")),
    ("(jan_01) Beach: Right Hidden Block",                       ("Collectable", (0xb2b4f4,),  None,        False,      "Mystery?")),
#   ("(jan_01) Beach: Tree 1",                       ("Collectable", (?,),  None,        ?,      "Coconut")),
#   ("(jan_01) Beach: Tree 2",                       ("Collectable", (?,),  None,        ?,      "Coconut")),
#   ("(jan_01) Beach: Tree 3",                       ("Collectable", (?,),  None,        ?,      "Coconut")),
#   ("(jan_01) Beach: Tree 4",                       ("Collectable", (?,),  None,        ?,      "Coconut")),
#   ("(jan_01) Beach: Tree 5",                       ("Collectable", (?,),  None,        ?,      "Star Piece (1)")),

#   ("(jan_02) Village Cove: Hidden Panel",                      ("?", (?,),  None,        False,      "Star Piece (1)")),
#   ("(jan_02) Village Cove: Left Tree",                         ("?", (?,),  None,        True,       "Coconut")),
#   ("(jan_02) Village Cove: Right Tree",                        ("?", (?,),  None,        True,       "Coconut")),
#   ("(jan_02) Village Cove: From Village Leader",               ("Script", (0xb31fa4,),  None,        False,       "Jade Raven")),

#   ("(jan_03) Village Buildings: Right Tree",                   ("?", (?,),  None,        True,       "Coconut")),
#   ("(jan_03) Village Buildings: Give Red Yoshi Letter (21)",   ("?", (?,),  None,        False,       "Letter (22)")),
#   ("(jan_03) Village Buildings: Give Kolorado Volcano Vase",   ("Script",      (0xb40e04,),  None,        False,      "Magical Seed 4")),
#   ("(jan_03) Village Buildings: Shop Item 1",                  ("Shop",        (0xb3958c,),  None,        True,       "Snowman Doll")),
#   ("(jan_03) Village Buildings: Shop Item 2",                  ("Shop",        (0xb39598,),  None,        True,       "Thunder Rage")),
#   ("(jan_03) Village Buildings: Shop Item 3",                  ("Shop",        (0xb395a4,),  None,        True,       "Fire Flower")),
#   ("(jan_03) Village Buildings: Shop Item 4",                  ("Shop",        (0xb395b0,),  None,        True,       "Tasty Tonic")),
#   ("(jan_03) Village Buildings: Shop Item 5",                  ("Shop",        (0xb395bc,),  None,        True,       "Honey Syrup")),
#   ("(jan_03) Village Buildings: Shop Item 6",                  ("Shop",        (0xb395c8,),  None,        True,       "Super Shroom")),

    ("(jan_04) Sushi Tree: Back Right Island Ground",            ("Collectable", (0xb46180,),  None,        False,       "Star Piece (1)")),
    ("(jan_04) Sushi Tree: Back Right Island Tree",              ("Collectable", (0xb489c8,),  None,        False,       "Letter (04)")),
#   ("(jan_04) Sushi Tree: In Chest After Ch. 5",                ("Collectable", (0xb460c8,),  None,        False,       "Volcano Vase")),

    ("(jan_05) SE Jungle (Quake Hammer): Island ? Block",        ("Collectable", (0xb52400,),  None,        False,       "Power Quake")),

    ("(jan_09) NW Jungle (Large Ledge): Right Tree",             ("Collectable", (0xb6be68,),  None,        False,       "Fright Jar")),

    ("(jan_10) Western Dead End: Under Water",                   ("Collectable", (0xb707cc,),  None,        False,       "Star Piece (1)")),

#   ("(jan_14) Deep Jungle 3: Second Left Tree",                 ("Collectable", (0xb7c1d0,),  None,        ?,       "Fire Flower")),
#   ("(jan_14) Deep Jungle 3: Rightmost Tree",                   ("Collectable", (0xb7c290,),  None,        ?,       "Mushroom")),

    ("(jan_18) Great Tree Vine Ascent: End Of The Vine",         ("Collectable", (0xb83e1c,),  None,        False,       "Happy Heart 2")),

#   ("(jan_22) Path to the Volcano: Gift From Raphael",          ("Script", (0xb88964,),  None,        False,       "Ultra Stone")),

## kzn: Mt. Lavalava
    ("(kzn_03) Central Cavern: Ontop Of Block",                  ("Collectable", (0xc67408,),  None,        False,       "POW Block")),
    ("(kzn_03) Central Cavern: Ontop Of Central Pillar",         ("Collectable", (0xc6739c,),  None,        False,       "Fire Shield")),

#   ("(kzn_07) Ultra Hammer Room: Big Chest",                    ("Script", (?,),  None,        False,       "Ultra Hammer")),

#   ("(kzn_08) Dizzy Stomp Room: In Chest",                      ("Collectable", (0xc76188,),  None,        False,       "Dizzy Stomp")),

    ("(kzn_19) Boss Room: Upper Level Left ? Block",             ("Collectable", (0xc95e90,),  None,        False,       "Super Shroom")),
    ("(kzn_19) Boss Room: Upper Level Right ? Block",            ("Collectable", (0xc95ec8,),  None,        False,       "Maple Syrup")),

## flo: Flower Fields
#   ("(flo_09) (East) Triple Tree Path: Second Left Ivy",        ("Collectable", (?,),  None,        True,        "Stinky Herb")),
#   ("(flo_09) (East) Triple Tree Path: Hitting The Trees",      ("Collectable", (0xcb8290,),  None,        False,       "Happy Flower 2")),

#   ("(flo_03) (East) Petunia's Field: Tree Drop 1",             ("Collectable", (0xcac098,),  None,        True,        "Red Berry")),
#   ("(flo_03) (East) Petunia's Field: Tree Drop 2",             ("Collectable", (0xcac0b4,),  None,        True,        "Red Berry")),
#   ("(flo_03) (East) Petunia's Field: Save Petunia",            ("Script",      (0xca8ed8,),  None,        False,       "Magical Bean")),

#   ("(flo_22) (East) Old Well: Blue Berry Into Well",           ("?",      (0xced36c,0xced7a4),  None,        False,       "Flower Saver 2")),

#   ("(flo_25) (SW) Path to Crystal Tree: Central Ivy",          ("Collectable", (?,),  None,        True,       "Stinky Herb")),
    ("(flo_25) (SW) Path to Crystal Tree: Tree Drop 1",          ("Collectable", (0xcf7230,),  None,        True,        "Yellow Berry")),
    ("(flo_25) (SW) Path to Crystal Tree: Tree Drop 2",          ("Collectable", (0xcf724c,),  None,        True,        "Yellow Berry")),

#   ("(flo_07) (SW) Posie and Crystal Tree: Talk To Posie",      ("Script",      (0xcae398,),  None,        False,       "Fertile Soil")),
#   ("(flo_07) (SW) Posie and Crystal Tree: Talk To Posie Again",("Script",      (?,),  None,        False,       "Crystal Berry")),

#   ("(flo_16) (NE) Elevators: Ivy",                             ("Collectable", (?,),  None,        True,       "Stinky Herb")),
#   ("(flo_08) (SE) Briar Platforming: Ivy",                     ("Collectable", (?,),  None,        True,       "Stinky Herb")),
    ("(flo_08) (SE) Briar Platforming: Hidden In The Flowers",   ("Collectable", (0xcb1398,),  None,        False,       "Star Piece (1)")),
    ("(flo_08) (SE) Briar Platforming: Tree Drop 1",             ("Collectable", (0xcb45f8,),  None,        True,        "Blue Berry")),
    ("(flo_08) (SE) Briar Platforming: Tree Drop 2",             ("Collectable", (0xcb4614,),  None,        True,        "Blue Berry")),

    ("(flo_24) (SE) Water Level Room: Visible ? Block",          ("Collectable", (0xcf2b10,),  None,        False,       "Dizzy Dial")),
    ("(flo_24) (SE) Water Level Room: Hidden ? Block",           ("Collectable", (0xcf2b48,),  None,        False,       "Maple Syrup")),
    ("(flo_24) (SE) Water Level Room: Tree Drop 1",              ("Collectable", (0xcf200c,),  None,        True,        "Bubble Berry")),
    ("(flo_24) (SE) Water Level Room: Tree Drop 2",              ("Collectable", (0xcf2028,),  None,        True,        "Bubble Berry")),

#   ("(flo_10) (SE) Lily's Fountain: Return Water Stone",        ("Script",      (0xcbbc44,),  None,        False,       "Miracle Water")),
#   ("(flo_10) (SE) Lily's Fountain: Tree",                      ("Collectable", (0xcbdc10,),  None,        ?,       "Jammin Jelly")),

    ("(flo_23) (West) Path to Maze: Hidden ? Block Parcour",     ("Collectable", (0xcf0844,),  None,        False,       "Shooting Star")),
#   ("(flo_12) (West) Rosie's Trellis: Hidden ? Block Parcour",  ("Script",      (?,),  None,        False,       "Water Stone")),

    ("(flo_14) (NW) Bubble Flower: Ontop Of Ledge",              ("Collectable", (0xcd024c,),  None,        False,       "Star Piece (1)")),
#   ("(flo_14) (NW) Bubble Flower: Ivy",                         ("Collectable", (?,),  None,        True,       "Stinky Herb")),
    ("(flo_13) (NW) Lakilester: Below Boulder",                  ("Collectable", (0xcc7194,),  None,        False,       "Mega Smash")),

    ("(flo_19) (NW) Cloudy Climb: Ontop Of Cloud",               ("Collectable", (0xce41bc,),  None,        False,       "S. Jump Chg.")),

## sam: Mt Shiver
#   ("(sam_02) Shiver City Center: Shop Item 1",                 ("Collectable", (0xd10dfc,),  None,        True,        "Dizzy Dial")),
#   ("(sam_02) Shiver City Center: Shop Item 2",                 ("Collectable", (0xd10e08,),  None,        True,        "Shooting Star")),
#   ("(sam_02) Shiver City Center: Shop Item 3",                 ("Collectable", (0xd10e14,),  None,        True,        "Snowman Doll")),
#   ("(sam_02) Shiver City Center: Shop Item 4",                 ("Collectable", (0xd10e20,),  None,        True,        "Maple Syrup")),
#   ("(sam_02) Shiver City Center: Shop Item 5",                 ("Collectable", (0xd10e2c,),  None,        True,        "Life Shroom")),
#   ("(sam_02) Shiver City Center: Shop Item 6",                 ("Collectable", (0xd10e38,),  None,        True,        "Super Shroom")),

#   ("(sam_11) Shiver City Pond Area: In The Pond",              ("Collectable", (?,),  None,        False,        "Warehouse Key")),


## kkj: Peach's Castle
    ("(kkj_16) Library (2F): Between The Bookshelves",           ("Collectable", (0xaf1bac,),          None,        False,     "Power Rush")),

## Misc
#   ("(misc) Give Kolorado Letter (25)",                         ("Script", (?,),          None,        False,     "Star Piece (1)")),
])