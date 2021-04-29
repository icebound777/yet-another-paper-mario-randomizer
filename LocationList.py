from collections import OrderedDict

# Location describes the item location itself including the map-id
# Type is either Script, Shop or Collectable, the latter describing somewhat free-standing items which can
#   be picked up by touching them
# ItemAdresses are the locations in ROM where the item-id for a location is stored. Generally, 'Collectable' items
#   have only a single ItemAdress, while 'Script' items have multiple
# ScriptAdress is the location in ROM where a sub-script is called to add an item to Marios inventory.
#   These sub-scripts are addItem, addKeyItem, addBadge, addCoin, addStarpiece and have to be modified
#   depending on the item put there
# Repeatable states wether or not an item location can be checked multiple times
# VanillaItem states which item is found at this location in the vanilla game

item_locations = OrderedDict([
#   Location                                                    Type            ItemAdresses          ScriptAdress Repeatable VanillaItem

## kmr: Goomba Region
#   ("(kmr_00) Forest Clearing: Hidden Panel",                  ("Flipground",  (),                   (),          False,     "Star Piece (1)")),

    ("(kmr_04) Jr. Troopa's Playground: Tree Near Exit",        ("Collectable", (0x8cdc24,),          None,        False,     "Dolly")),

#   ("(kmr_02) Goomba Village: Goompa - Reward",                ("Script",      (),                   (),          False,     "Power Jump")),
#   ("(kmr_02) Goomba Village: Goompa - Koopa Koot Favor",      ("Script",      (),                   (),          False,     "Tape")),
#   ("(kmr_02) Goomba Village: Goompapa Letter",                ("Script",      (0x8b899c, 0x8b89c8), (0x8b89c4),  False,     "Lucky Day")),
#   ("(kmr_02) Goomba Village: Goombaria's Dolly",              ("Script",      (0x8ba446, 0x8ba470), (0x8ba46c),  False,     "Star Piece (1)")),
#   ("(kmr_02) Goomba Village: Chuck Quizmo",                   ("Script",      (),                   (),          False,     "Star Piece (1)")),
#   ("(kmr_02) Goomba Village: Veranda",                        ("Collectable", (0x8c519c),           None,        False,     "Shooting Star")),
    ("(kmr_02) Goomba Village: Tree Near Fencegate",            ("Collectable", (0x8c7a20,),          None,        True,      "Goomnut")),

#   ("(kmr_03) Bottom of the Cliff: Grey Block Hidden ? Block", ("Collectable", (0x8c9598),           None,        False,     "Repel Gel")),
    ("(kmr_03) Bottom of the Cliff: On Spring Ledge",           ("Collectable", (0x8c96f4,),          None,        False,     "Fire Flower")),
    ("(kmr_03) Bottom of the Cliff: Tree Near Yellow Block",    ("Collectable", (0x8ca1b8, 0x8ca1e4), None,        False,     "Mushroom")),

    ("(kmr_05) Behind the Village: End Of Upper Ledge",         ("Collectable", (0x8d090c,),          None,        False,     "Star Piece (1)")),

    ("(kmr_06) Goomba Road 2: Wooden Sign",                     ("Collectable", (0x8d3c70,),          None,        False,     "Mushroom")),
    ("(kmr_06) Goomba Road 2: Red ? Block",                     ("Collectable", (0x8d3b04,),          None,        False,     "Close Call")),

    ("(kmr_11) Goomba King's Castle: Tree Left Of Castle",      ("Collectable", (0x8e0f20,),          None,        False,     "Star Piece (1)")),
    ("(kmr_11) Goomba King's Castle: Hammerblock",              ("Collectable", (0x8dff60,0x8e0124),  None,        False,     "Super Shroom")),

    ("(kmr_10) Toad Town Entrance: Tree",                       ("Collectable", (0x8d9578,),          None,        False,     "Sleepy Sheep")),
    ("(kmr_10) Toad Town Entrance: Chest On Roof",              ("Collectable", (0x8d9518,),          None,        False,     "Hammer Throw")),

## mac: Toad Town
#    ("(mac_00) Gate District: ?",                      ("Collectable", (0x7efffc,),          None,        False,     "Star Piece (1)")),
#    ("(mac_00) Gate District: ?",                      ("Collectable", (?,),          None,        False,     "Star Piece (1)")),
#   ("(mac_00) Gate District: Shop Item 1",                     ("Shop",        (0x7f8fb8,),          None,        True,      "Mushroom")),
#   ("(mac_00) Gate District: Shop Item 2",                     ("Shop",        (0x7f8fac,),          None,        True,      "Honey Syrup")),
#   ("(mac_00) Gate District: Shop Item 3",                     ("Shop",        (0x7f8fa0,),          None,        True,      "Fire Flower")),
#   ("(mac_00) Gate District: Shop Item 4",                     ("Shop",        (0x7f8f94,),          None,        True,      "POW Block")),
#   ("(mac_00) Gate District: Shop Item 5",                     ("Shop",        (0x7f8f88,),          None,        True,      "Sleepy Sheep")),
#   ("(mac_00) Gate District: Shop Item 6",                     ("Shop",        (0x7f8f7c,),          None,        True,      "Fright Jar")),

    ("(mac_01) Plaza District: Tree Left Of Merlons",           ("Collectable", (0x822dc8,),          None,        False,     "Star Piece (1)")),
    ("(mac_01) Plaza District: Spin Jumps Inside Merlons",      ("TODO",        (0x81086c,0x810afc),  None,        False,     "Quick Change")),

    ("(mac_02) Southern District: Inside Odd House",            ("TODO",        (0x828f10,0x829150),  None,        False,     "Odd Key")),
    ("(mac_02) Southern District: Bub-ulb",                     ("TODO",        (0x82fbc4,),          None,        False,     "Magical Seed 1")),
    ("(mac_02) Southern District: Tayce T.s Reward For Pan",    ("TODO",        (0x82c5b4,0x82c778),  None,        False,     "Cake")),
])