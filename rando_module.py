import os
import re
from math import pow

import yaml
import json


from LocationList import item_locations

with open('byte_values/loc_text.yaml', 'r') as yamlfile:
    bl_text_firstplay = (yaml.safe_load(yamlfile)).get('text_firstplay')
with open('byte_values/val_text_characters.yaml', 'r') as yamlfile:
    byte_text_characters = yaml.safe_load(yamlfile)
with open('byte_values/loc_maps.yaml', 'r') as yamlfile:
    bl_starting_location = (yaml.safe_load(yamlfile)).get('initial_map')
with open('byte_values/val_maps.yaml', 'r') as yamlfile:
    byte_maps = (yaml.safe_load(yamlfile))
with open ('byte_values/val_items.yaml', 'r') as yamlfile:
    byte_items = (yaml.safe_load(yamlfile))
with open ('byte_values/val_additem_functions.yaml', 'r') as yamlfile:
    additem_functions = (yaml.safe_load(yamlfile))

def conv_chars_to_bytes(charstring):
    hexval = 0
    for i in reversed(range(0, len(charstring))):
        hexval += byte_text_characters.get(charstring[i]) * pow(256, (len(charstring) - 1 - i))
    return(int(hexval).to_bytes(len(charstring),'big'))

def randomize(infile, outfile):
    # Write to new ROM
    os.system('copy "%s" "%s"' % (infile, outfile))
    f=open(outfile,'rb+')

    # Skip developer logos
    f.seek(0xF298)
    f.write((0x00000000).to_bytes(4, 'big'))
    f.write((0x24040700).to_bytes(4, 'big'))
    f.write((0xA44400AC).to_bytes(4, 'big'))

    # Skip intro video
    f.seek(0x11c84)
    f.write((0x34051000).to_bytes(4, 'big'))

    # Disable demo reel
    f.seek(0x12644)
    f.write((0x1000).to_bytes(2, 'big'))

    # Overwrite "First Play" text on new savefile with "Randomized"
    f.seek(bl_text_firstplay)
    f.write(conv_chars_to_bytes('Rand'))
    f.write(conv_chars_to_bytes('omiz'))
    f.write(conv_chars_to_bytes('ed'))

    # Iterate over all item check locations
    for location in item_locations.items():
        # Write different addObject function if necessary (mostly used in Scripts)
        cur_locationtype = location[1][0]
        cur_itemname = location[1][4]
        if cur_locationtype == 'Script':
            print('Script!')
            if byte_items.get(cur_itemname).get('isKeyItem'):
                cur_additem_function_val = additem_functions.get('addKeyItem')
            elif byte_items.get(cur_itemname).get('isBadge'):
                cur_additem_function_val = additem_functions.get('addBadge')
            elif cur_itemname.startswith('Star Piece'):
                cur_additem_function_val = additem_functions.get('addStarPieces')
            else:
                cur_additem_function_val = additem_functions.get('addItem')
            func_adress = location[1][2]
            f.seek(func_adress)
            f.write(cur_additem_function_val.to_bytes(4,'big'))

        # Iterate over all item byte locations of that item check
        for item_adress in location[1][1]:
            # Write byte value of item to item byte location
            if cur_itemname.startswith('Star Piece') and cur_locationtype == 'Script' and item_adress == location[1][1][-1]:
                # Find # of Star Pieces to set
                reg_pattern_sp_count = re.compile(r'(?<=\()(\d+)(?=\))')
                reg_match_sp_count = reg_pattern_sp_count.search(cur_itemname)
                item_value = int(reg_match_sp_count.group())
                # print(f'  Calculated Starpieces: {item_value}')
            else:
                item_value = byte_items.get(cur_itemname).get('bytes')
                # print('  Set Itemvalue')
            f.seek(item_adress)
            f.write(item_value.to_bytes(4,'big'))

    # Save randomized file
    f.close()