import os
from math import pow

import yaml

from statics.version import __version__

def conv_chars_to_bytes(charstring):
    hexval = 0
    for i in reversed(range(0, len(charstring))):
        hexval += byte_text_characters.get(charstring[i]) * pow(256, (len(charstring) - 1 - i))
    return(int(hexval).to_bytes(len(charstring),'big'))

with open('byte_values/val_text_characters.yaml', 'r') as yamlfile:
    byte_text_characters = yaml.safe_load(yamlfile)
with open('byte_values/loc_maps.yaml', 'r') as yamlfile:
    bl_starting_location = (yaml.safe_load(yamlfile)).get('initial_map')
with open('byte_values/loc_text.yaml', 'r') as yamlfile:
    bl_text_firstplay = (yaml.safe_load(yamlfile)).get('text_firstplay')

print(f'YaPMR v.{__version__}')

infile = 'Paper Mario (U) [!].z64'
outfile = 'PMRandomized.z64'

# Open Rom and check if it is actually a PM rom
assert(os.path.isfile(infile))
os.system('copy "%s" "%s"' % (infile, outfile))
f=open(outfile,'rb+')

f.seek(0x20)
assert(f.read(11) == b'PAPER MARIO')

# Overwrite "First Play" text on new savefile with "Randomized"
f.seek(bl_text_firstplay)
f.write(conv_chars_to_bytes('Rand'))
f.write(conv_chars_to_bytes('omiz'))
f.write(conv_chars_to_bytes('ed'))

# Don't start the game from Mario's house
f.seek(bl_starting_location)
#f.write(byte_locations.get('isk_03').get('bytes'))
f.write((0x2402018A).to_bytes(4,'big'))

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

# Save randomized file and fix bootcode
f.close()
assert(os.path.isfile('rn64crc2\\rn64crc.exe'))
os.system('rn64crc2\\rn64crc.exe "%s" -u' % outfile)
