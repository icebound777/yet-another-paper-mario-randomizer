import os
import re
from math import pow

import yaml
import json

from LocationList import vanilla_locations

with open('byte_values/loc_text.yaml', 'r') as yamlfile:
    bl_text_firstplay = (yaml.safe_load(yamlfile)).get('text_firstplay')

with open('byte_values/val_text_characters.yaml', 'r') as yamlfile:
    byte_text_characters = yaml.safe_load(yamlfile)

with open ('byte_values/val_items.yaml', 'r') as yamlfile:
    byte_items = (yaml.safe_load(yamlfile))

with open ('byte_values/val_additem_functions.yaml', 'r') as yamlfile:
    additem_functions = (yaml.safe_load(yamlfile))

with open('byte_values/loc_maps.yaml', 'r') as yamlfile:
    bl_starting_location = (yaml.safe_load(yamlfile)).get('initial_map')

with open('byte_values/val_maps.yaml', 'r') as yamlfile:
    byte_maps = (yaml.safe_load(yamlfile))

def conv_chars_to_bytes(charstring):
    hexval = 0
    for i in reversed(range(0, len(charstring))):
        hexval += byte_text_characters.get(charstring[i]) * pow(256, (len(charstring) - 1 - i))
    return(int(hexval).to_bytes(len(charstring),'big'))

def patch_rom(infile, outfile, general_settings, randomized_locations):

    # Write to new ROM
    os.system('copy "%s" "%s"' % (infile, outfile))
    f=open(outfile,'rb+')

    ## Always apply following modifications regardless of settings
    # Overwrite "First Play" text on new savefile with "Randomized"
    f.seek(bl_text_firstplay)
    f.write(conv_chars_to_bytes('Rand'))
    f.write(conv_chars_to_bytes('omiz'))
    f.write(conv_chars_to_bytes('ed'))

    ##

    # Disable developer logos
    if 'skip_devlogos' in general_settings:
        f.seek(0xF298)
        f.write((0x00000000).to_bytes(4, 'big'))
        f.write((0x24040700).to_bytes(4, 'big'))
        f.write((0xA44400AC).to_bytes(4, 'big')) 
    
    # Disable intro video
    if 'skip_intro' in general_settings:
        f.seek(0x11c84)
        f.write((0x34051000).to_bytes(4, 'big'))
    
    # Disable demo reel
    if 'disable_demo' in general_settings:
        f.seek(0x12644)
        f.write((0x1000).to_bytes(2, 'big'))

    # Change initial map (StarRod style) ?? doesnt really work
    # f.seek(0x2811720)
    # f.write((0x24010001).to_bytes(4, 'big'))
    # f.seek(0x2811728)
    # f.write((0x24010001).to_bytes(4, 'big'))


    # Load vanilla locations
    item_locations = vanilla_locations

    for modified_check in randomized_locations.keys():
        new_location_tuple = (item_locations[modified_check][0],
                              item_locations[modified_check][1],
                              item_locations[modified_check][2],
                              item_locations[modified_check][3],
                              randomized_locations.get(modified_check))
        item_locations[modified_check] = new_location_tuple

    # Iterate over all item check locations
    for location in item_locations.items():
        # Write different addObject function if necessary (mostly used in Scripts)
        cur_locationtype = location[1][0]
        cur_itemname = location[1][4]
        if cur_locationtype == 'Script':
            if byte_items.get(cur_itemname).get('isKeyItem'):
                cur_additem_function_val = additem_functions.get('addKeyItem')
            elif byte_items.get(cur_itemname).get('isBadge'):
                cur_additem_function_val = additem_functions.get('addBadge')
            elif cur_itemname.startswith('Star Piece'):
                cur_additem_function_val = additem_functions.get('addStarPieces')
            else:
                cur_additem_function_val = additem_functions.get('addItem')
            for func_adress in location[1][2]:
                f.seek(func_adress)
                f.write(cur_additem_function_val.to_bytes(4,'big'))

        # Iterate over all item byte locations of that item check
        for item_adress in location[1][1]:
            # Write byte value of item to item byte location
            if (cur_itemname.startswith('Star Piece') and
                cur_locationtype == 'Script' and
                (item_adress == location[1][1][-1] or # hacky solution for Goombaria's Dolly
                 item_adress == location[1][1][1])):
                # Find # of Star Pieces to set
                reg_pattern_sp_count = re.compile(r'(?<=\()(\d+)(?=\))')
                reg_match_sp_count = reg_pattern_sp_count.search(cur_itemname)
                item_value = int(reg_match_sp_count.group())
            else:
                item_value = byte_items.get(cur_itemname).get('bytes')
            f.seek(item_adress)
            f.write(item_value.to_bytes(4,'big'))


                

    # testing
    # f.seek(0x8c7a20)
    # f.write((0x00000100).to_bytes(4, 'big'))

# write itemvalue into dgb_14
# f.seek(0xC4F4D0)
# f.write((0x0000015E).to_bytes(4,'big'))

# start of black magic
    # Don't start the game from Mario's house
    # f.seek(bl_starting_location)
    # f.write(byte_maps.get('kmr').get('kmr_10').get('bytes').to_bytes(4,'big'))
#    f.write((0x23000000).to_bytes(4,'big'))
#    f.seek(0x168083)
#    f.write((0x00A3).to_bytes(2, 'big'))

    #code patch: start with goombario out
    # f.seek(0x808A8)
    # f.write((0xA0820012).to_bytes(4,'big'))
    # f.write((0xA082000A).to_bytes(4,'big')) # enable action command
    # f.write((0x2402FFFF).to_bytes(4,'big'))
    # f.seek(0x808E4)
    # f.write((0xA0800000).to_bytes(4,'big'))
    # #have every party member
    # f.write((0xA0A20014).to_bytes(4,'big'))
    # #enable menus
    # f.seek(0x168074)
    # f.write((0x2406FF81).to_bytes(4,'big'))
# end of black magic

# for i in range(302,303):
#     f.seek(0x6B450 + i*0x20)
#     nameptr = int.from_bytes(f.read(4), 'big') - 0x80024C00
#     f.seek(nameptr)
#     name = f.read(8).decode().strip('\0')
#     print(f'{i}: {name}')

# with open('E:/Downloads/_Git/MrCheeze_paper-mario-randomizer/roomdata.json', 'r') as jsonfile:
#     roomdata = json.load(jsonfile)

# # invert byte_items
# items_byte = {}
# for i in byte_items.keys():
#     items_byte[byte_items.get(i).get('bytes')] = i

# for i in range(421):
#     f.seek(0x6B450 + i*0x20)
#     nameptr = int.from_bytes(f.read(4), 'big') - 0x80024C00
#     f.seek(4, os.SEEK_CUR)
#     roomptr = int.from_bytes(f.read(4), 'big')
#     f.seek(nameptr)
#     name = f.read(8).decode().strip('\0')
#     print(f'{name}')
#     count_item = 0
#     for itemptr in roomdata[name]['items']:
#         item_location = roomptr + itemptr - 0x80240000
#         f.seek(item_location)
#         item = int.from_bytes(f.read(4), 'big')
#         if 0 < item < 0x200:
#             print(f'    {hex(item_location)}: {items_byte.get(item)}')
#         else:
#             print(f'    {hex(item_location)}: {item}')
#         count_item += 1



    # Save patched file
    f.close()

    # Fix bootcode
    try:
        assert(os.path.isfile('rn64crc2\\rn64crc.exe'))
        os.system('rn64crc2\\rn64crc.exe "%s" -u' % outfile)
    except AssertionError:
        print('')
        exit(1)
    
    # Output spoiler log if necessary
    trimmed_locations = {}
    for location in item_locations.items():
        trimmed_locations[location[0]] = location[1][4]
    spoiler_log = json.dumps(trimmed_locations, indent=4)
    try:
        jsonSpoiler = open("spoiler_log.json", "w")
        jsonSpoiler.write(spoiler_log)
        jsonSpoiler.close()
    except OSError:
        print('Error: Spoiler log could not be written!')
