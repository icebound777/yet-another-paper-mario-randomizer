import os

from statics.version import __version__
from bytelocations.bytes import bl_starting_location, byte_locations

print(f'YaPMR v.{__version__}')

infile = 'Paper Mario (U) [!].z64'
outfile = 'PMRandomized.z64'

# Open Rom and check if it is actually a PM rom
assert(os.path.isfile(infile))
os.system('copy "%s" "%s"' % (infile, outfile))
f=open(outfile,'rb+')

f.seek(0x20)
assert(f.read(11) == b'PAPER MARIO')

# Don't start the game from Mario's house
#print(f'{f.tell()}')
f.seek(bl_starting_location)
#print(f'{f.tell()}')
#f.write(byte_locations.get('kmr_03'))
f.write((0x2402004F).to_bytes(4,'big'))
#print(f'{f.tell()}')

# Save randomized file and fix bootcode
f.close()
assert(os.path.isfile('rn64crc2\\rn64crc.exe'))
os.system('rn64crc2\\rn64crc.exe "%s" -u' % outfile)