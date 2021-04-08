import os

from statics.version import __version__
from bytelocations.bytes import bl_starting_location

print(f'YaPMR v.{__version__}')

infile = 'Paper Mario (U) [!].z64'
outfile = 'PMRandomized.z64'

assert(os.path.isfile(infile))
os.system('copy "%s" "%s"' % (infile, outfile))
f=open(outfile,'rb+')

f.seek(0x20)
assert(f.read(11) == b'PAPER MARIO')

#don't start the game from mario's house
f.seek(bl_starting_location)
f.write((0x24020000).to_bytes(4,'big'))

f.close()
assert(os.path.isfile('rn64crc2\\rn64crc.exe'))
os.system('rn64crc2\\rn64crc.exe "%s" -u' % outfile)