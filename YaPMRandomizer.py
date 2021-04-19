import os

from statics.version import __version__
from bytelocations.bytes import bl_starting_location, byte_locations, bl_text_firstplay, byte_text_randomizer_1, byte_text_randomizer_2, byte_text_randomizer_3

print(f'YaPMR v.{__version__}')

infile = 'Paper Mario (U) [!].z64'
outfile = 'PMRandomized.z64'

# Open Rom and check if it is actually a PM rom
assert(os.path.isfile(infile))
os.system('copy "%s" "%s"' % (infile, outfile))
f=open(outfile,'rb+')

f.seek(0x20)
assert(f.read(11) == b'PAPER MARIO')

# Overwrite "First Play" text on new file with "Randomized"
f.seek(bl_text_firstplay)
f.write(byte_text_randomizer_1)
f.write(byte_text_randomizer_2)
f.write(byte_text_randomizer_3)

# Don't start the game from Mario's house
f.seek(bl_starting_location)
#f.write(byte_locations.get('isk_03').get('bytes'))
f.write((0x240200CA).to_bytes(4,'big'))

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