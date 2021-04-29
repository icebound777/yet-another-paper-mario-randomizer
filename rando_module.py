import os
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

def conv_chars_to_bytes(charstring):
    hexval = 0
    for i in reversed(range(0, len(charstring))):
        hexval += byte_text_characters.get(charstring[i]) * pow(256, (len(charstring) - 1 - i))
    return(int(hexval).to_bytes(len(charstring),'big'))

def randomize(infile, outfile):

    #spoiler_log = json.dumps(item_locations, indent = 4)
    #print(spoiler_log)

    # Write to new ROM
    os.system('copy "%s" "%s"' % (infile, outfile))
    f=open(outfile,'rb+')

    # Overwrite "First Play" text on new savefile with "Randomized"
    f.seek(bl_text_firstplay)
    f.write(conv_chars_to_bytes('Rand'))
    f.write(conv_chars_to_bytes('omiz'))
    f.write(conv_chars_to_bytes('e'))

    # Don't start the game from Mario's house
    f.seek(bl_starting_location)
    f.write(byte_maps.get('kmr').get('kmr_00').get('bytes').to_bytes(4,'big'))
#    f.write((0x23000000).to_bytes(4,'big'))
#    f.seek(0x168083)
#    f.write((0x00A3).to_bytes(2, 'big'))

    # Iterate over all item check locations
    for location in item_locations.items():
        # Iterate over all item byte locations of that item check
        for byte_location in location[1][1]:
            # Write byte value of item to item byte location
            byte_value = byte_items.get(location[1][4]).get('bytes')
            f.seek(byte_location)
            f.write(byte_value.to_bytes(4,'big'))

    # testing
    # f.seek(0x8c7a20)
    # f.write((0x00000100).to_bytes(4, 'big'))

# to try:
# 0x8b7676 #no #
# 0x8b77a2 #no #no
# 0x8b8a5e #no #no
# 0x8b905a #no #yes
# 0x8ba446 #yes #no
# 

# write itemvalue into dgb_14
# f.seek(0xC4F4D0)
# f.write((0x0000015E).to_bytes(4,'big'))

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

# f.seek(0x6B450)
# testvar = hex(int.from_bytes(f.read(4), 'big'))
# print(f'{testvar}')
# testvar = hex(int.from_bytes(f.read(4), 'big'))
# print(f'{testvar}')

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

    # Save randomized file
    f.close()