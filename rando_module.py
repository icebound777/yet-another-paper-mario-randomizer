import random
import yaml

from LocationList import vanilla_locations

with open ('byte_values/val_items.yaml', 'r') as yamlfile:
    byte_items = (yaml.safe_load(yamlfile))

def shuffle_within_groups(shuffle_groups):
    randomized_locations = {}

    # Set up which groups to generate
    shuffle_badges = ('badges' in shuffle_groups)
    shuffle_keyItems = ('keyItems' in shuffle_groups)
    shuffle_oneOffItems = ('oneOffItems' in shuffle_groups)
    shuffle_repeatableItems = ('repeatableItems' in shuffle_groups)

    # Build groups
    grp_locations_badges = []
    grp_locations_keyItems = []
    grp_locations_oneOffItems = []
    grp_locations_repeatableItems = []

    grp_items_badges = []
    grp_items_keyItems = []
    grp_items_oneOffItems = []
    grp_items_repeatableItems = []

    for location in vanilla_locations.items():
        current_location = location[0]
        current_item = location[1][4]
        current_isRepeatable = location[1][3]

        if (shuffle_badges
                and byte_items.get(current_item).get('isBadge')):
            grp_locations_badges.append(current_location)
            grp_items_badges.append(current_item)
        
        elif (shuffle_keyItems
                and byte_items.get(current_item).get('isKeyItem')):
            grp_locations_keyItems.append(current_location)
            grp_items_keyItems.append(current_item)
        
        elif (not byte_items.get(current_item).get('isBadge')
                and not byte_items.get(current_item).get('isKeyItem')):
            if (shuffle_oneOffItems
                    and not current_isRepeatable):
                grp_locations_oneOffItems.append(current_location)
                grp_items_oneOffItems.append(current_item)
            
            elif (shuffle_repeatableItems
                    and current_isRepeatable):
                grp_locations_repeatableItems.append(current_location)
                grp_items_repeatableItems.append(current_item)

    # Shuffle groups
    for badge_location in grp_locations_badges:
        random_index = random.randint(0, len(grp_items_badges) - 1)
        randomized_locations[badge_location] = grp_items_badges.pop(random_index)
    for keyItem_location in grp_locations_keyItems:
        random_index = random.randint(0, len(grp_items_keyItems) - 1)
        randomized_locations[keyItem_location] = grp_items_keyItems.pop(random_index)
    for oneOffItem_location in grp_locations_oneOffItems:
        random_index = random.randint(0, len(grp_items_oneOffItems) - 1)
        randomized_locations[oneOffItem_location] = grp_items_oneOffItems.pop(random_index)
    for repeatableItem_location in grp_locations_repeatableItems:
        random_index = random.randint(0, len(grp_items_repeatableItems) - 1)
        randomized_locations[repeatableItem_location] = grp_items_repeatableItems.pop(random_index)

    return randomized_locations


def randomize(randomizer_settings):
    randomized_locations = {}

    if randomizer_settings.get('logic') == 'no_logic':
        # NYI
        print('No logic')
    
    if randomizer_settings.get('rando_type') == 'vanilla_shuffle':
        if randomizer_settings.get('shuffle_type') == 'within_groups':
            randomized_locations = shuffle_within_groups(randomizer_settings['shuffle_groups'])


    # rando_dict["(kmr_02) Goomba Village: Goombaria's Dolly"] = "Dolly"
    # rando_dict["(kmr_02) Goomba Village: Tree Near Fencegate"] = "Dolly"
    # rando_dict["(mac_00) Gate District: Return Dictionary To Russ T."] = "Dolly"
    # rando_dict["(mac_01) Plaza District: Tree Left Of Merlon's"] = "Dictionary"
    print(randomized_locations)
    return randomized_locations
