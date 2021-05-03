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

item_locations = OrderedDict([
#   Location                                                     Type            ItemAdresses          FuncAdress   Repeatable VanillaItem

## kmr: Goomba Region
#   ("(kmr_00) Forest Clearing: Hidden Panel",                   ("TODO",  (),                   (),          False,     "Star Piece (1)")),

    ("(kmr_04) Jr. Troopa's Playground: Tree Near Exit",         ("Collectable", (0x8cdc24,),          None,        False,     "Dolly")),

#   ("(kmr_02) Goomba Village: Goompa Reward",                   ("Script",      (),                   (),          False,     "Power Jump")),
#   ("(kmr_02) Goomba Village: Goompa: Koopa Koot Favor",        ("Script",      (),                   (),          False,     "Tape")),
    ("(kmr_02) Goomba Village: Goompapa Letter",                 ("Script",      (0x8b899c, 0x8b89c8), (0x8b89c4),  False,     "Lucky Day")),
    ("(kmr_02) Goomba Village: Goombaria's Dolly",               ("Script",      (0x8ba444, 0x8ba470), (0x8ba46c),  False,     "Star Piece (1)")),
#   ("(kmr_02) Goomba Village: Chuck Quizmo",                    ("Script",      (),                   (),          False,     "Star Piece (1)")),
    ("(kmr_02) Goomba Village: Veranda",                         ("Collectable", (0x8c519c),           None,        False,     "Shooting Star")),
    ("(kmr_02) Goomba Village: Tree Near Fencegate",             ("Collectable", (0x8c7a20,),          None,        True,      "Goomnut")),

#   ("(kmr_03) Bottom of the Cliff: Grey Block Hidden ? Block",  ("Collectable", (0x8c9598),           None,        False,     "Repel Gel")),
    ("(kmr_03) Bottom of the Cliff: On Spring Ledge",            ("Collectable", (0x8c96f4,),          None,        False,     "Fire Flower")),
    ("(kmr_03) Bottom of the Cliff: Tree Near Yellow Block",     ("Collectable", (0x8ca1b8, 0x8ca1e4), None,        False,     "Mushroom")),

    ("(kmr_05) Behind the Village: End Of Upper Ledge",          ("Collectable", (0x8d090c,),          None,        False,     "Star Piece (1)")),

    ("(kmr_06) Goomba Road 2: Wooden Sign",                      ("Collectable", (0x8d3c70,),          None,        False,     "Mushroom")),
    ("(kmr_06) Goomba Road 2: Red ? Block",                      ("Collectable", (0x8d3b04,),          None,        False,     "Close Call")),

    ("(kmr_11) Goomba King's Castle: Tree Left Of Castle",       ("Collectable", (0x8e0f20,),          None,        False,     "Star Piece (1)")),
    ("(kmr_11) Goomba King's Castle: Hammerblock",               ("Collectable", (0x8dff60,0x8e0124),  None,        False,     "Super Shroom")),

    ("(kmr_10) Toad Town Entrance: Tree",                        ("Collectable", (0x8d9578,),          None,        False,     "Sleepy Sheep")),
    ("(kmr_10) Toad Town Entrance: Chest On Roof",               ("Collectable", (0x8d9518,),          None,        False,     "Hammer Throw")),

## mac: Toad Town
#   ("(mac_00) Gate District: ?",                      ("TODO", (0x7efffc,),          None,        False,     "Star Piece (1)")),
#   ("(mac_00) Gate District: ?",                      ("TODO", (?,),          None,        False,     "Star Piece (1)")),
#   ("(mac_00) Gate District: Shop Item 1",                      ("Shop",        (0x7f8f7c,),          None,        True,      "Fright Jar")),
#   ("(mac_00) Gate District: Shop Item 2",                      ("Shop",        (0x7f8f88,),          None,        True,      "Sleepy Sheep")),
#   ("(mac_00) Gate District: Shop Item 3",                      ("Shop",        (0x7f8f94,),          None,        True,      "POW Block")),
#   ("(mac_00) Gate District: Shop Item 4",                      ("Shop",        (0x7f8fa0,),          None,        True,      "Fire Flower")),
#   ("(mac_00) Gate District: Shop Item 5",                      ("Shop",        (0x7f8fac,),          None,        True,      "Honey Syrup")),
#   ("(mac_00) Gate District: Shop Item 6",                      ("Shop",        (0x7f8fb8,),          None,        True,      "Mushroom")),

    ("(mac_01) Plaza District: Tree Left Of Merlon's",           ("Collectable", (0x822dc8,),          None,        False,     "Star Piece (1)")),
#   ("(mac_01) Plaza District: Chuck Quizmo",                    ("Collectable", (?,),          None,        False,     "Star Piece (1)")),
#   ("(mac_01) Plaza District: Spin Jumps Inside Merlon's",      ("TODO",        (0x81086c,0x810afc),  None,        False,     "Quick Change")),

#   ("(mac_02) Southern District: Inside Odd House",             ("TODO",        (0x828f10,0x829150),  None,        False,     "Odd Key")),
#   ("(mac_02) Southern District: Bub-ulb",                      ("Script",      (0x82fbc4,),          None,        False,     "Magical Seed 1")),
#   ("(mac_02) Southern District: Tayce T.s Reward For Pan",     ("TODO",        (0x82c5b4,0x82c778),  None,        False,     "Cake")),

#   ("(mac_04) Residental District: Shop Item 1",                ("Shop",        (0x84683c,),          None,        True,      "Stone Cap")),
#   ("(mac_04) Residental District: Shop Item 2",                ("Shop",        (0x846848,),          None,        True,      "Dizzy Dial")),
#   ("(mac_04) Residental District: Shop Item 3",                ("Shop",        (0x846854,),          None,        True,      "Thunder Rage")),
#   ("(mac_04) Residental District: Shop Item 4",                ("Shop",        (0x846860,),          None,        True,      "Tasty Tonic")),
#   ("(mac_04) Residental District: Shop Item 5",                ("Shop",        (0x84686c,),          None,        True,      "Volt Mushroom")),
#   ("(mac_04) Residental District: Shop Item 6",                ("Shop",        (0x846878,),          None,        True,      "Super Shroom")),

#   ("(mac_05) Port District: Talk To Writer In Bar",            ("Script",      (0x85fa8c,),          None,        True,      "Lyrics")),
#   ("(mac_05) Port District: Give Melody To Writer In Bar",     ("Script",      (?,),          None,        True,      "Attack FX D")),

## hos: Shooting Star Summit
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
#   ("(nok_01) Koopa Village 1: Shop Item 1",                    ("Shop",        (0x9d4f4c,),          None,        True,      "Dizzy Dial")),
#   ("(nok_01) Koopa Village 1: Shop Item 2",                    ("Shop",        (0x9d4f58,),          None,        True,      "POW Block")),
#   ("(nok_01) Koopa Village 1: Shop Item 3",                    ("Shop",        (0x9d4f64,),          None,        True,      "Fire Flower")),
#   ("(nok_01) Koopa Village 1: Shop Item 4",                    ("Shop",        (0x9d4f70,),          None,        True,      "Honey Syrup")),
#   ("(nok_01) Koopa Village 1: Shop Item 5",                    ("Shop",        (0x9d4f7c,),          None,        True,      "Volt Mushroom")),
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
#   ("(dro_01) Outpost 1: Shop Item 1",                          ("Collectable", (0x9666fc,),          None,        True,      "Thunder Bolt")),
#   ("(dro_01) Outpost 1: Shop Item 2",                          ("Collectable", (0x966708,),          None,        True,      "Dusty Hammer")),
#   ("(dro_01) Outpost 1: Shop Item 3",                          ("Collectable", (0x966714,),          None,        True,      "Honey Syrup")),
#   ("(dro_01) Outpost 1: Shop Item 4",                          ("Collectable", (0x966720,),          None,        True,      "Dried Shroom")),
#   ("(dro_01) Outpost 1: Shop Item 5",                          ("Collectable", (0x96672c,),          None,        True,      "Dried Pasta")),
#   ("(dro_01) Outpost 1: Shop Item 6",                          ("Collectable", (0x966738,),          None,        True,      "Mushroom")),

#   ("(dro_02) Outpost 2: Chuck Quizmo",                         ("Collectable", (?,),          None,        False,     "Star Piece (1)")),
    ("(dro_02) Outpost 2: Ontop Of Roof",                        ("Collectable", (0x96cd9c,),          None,        False,     "Letter (08)")),
#   ("(dro_02) Outpost 2: Moustafas Gift",                       ("Script",      (0x976048,),          None,        False,     "Pulse Stone")),

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
#   ("(obk_07) Record Player Room: Guarded Chest",               ("Collectable", (0xbd0cf8,),          None,        False,      "Weight")),
#   ("(obk_08) Record Room: Play With The Boos",                 ("Collectable", (?,),          None,        False,      "Record")),
#   ("(obk_02) Basement Stairs: Hidden Panel",                   ("Collectable", (?,),          None,        False,      "Star Piece (1)")),
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

## kkj: Peach's Castle
    ("(kkj_16) Library (2F): Between The Bookshelves",           ("Collectable", (0xaf1bac,),          None,        False,     "Power Rush")),
])