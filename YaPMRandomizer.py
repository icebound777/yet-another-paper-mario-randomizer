import os
import hashlib
from math import pow

from rando_module import randomize

from statics.version import __version__
from statics.rom_hash import __rom_hash__

print(f'YaPMR - Yet another Paper Mario Randomizer v.{__version__}')

infile = 'Paper Mario (U) [!].z64'
# infile = 'Paper Mario (U) [!]_Debug.z64'
outfile = 'PMRandomized.z64'

# Open Rom and check if it is actually a PM rom
try:
    assert(os.path.isfile(infile))
except AssertionError as error:
    print('Error: Input-File not found!')
    exit(1)
    
try:
    with open(infile, 'rb') as f:
        f.seek(0x20)
        assert(f.read(11) == b'PAPER MARIO')
        f.seek(0)
        hasher = hashlib.md5()
        buf = f.read()
        hasher.update(buf)
        assert(hasher.hexdigest() == __rom_hash__)
except AssertionError as error:
    print('Error: Incorrect ROM. Please select a valid Paper Mario (U) ROM file!')
    exit(1)

# Randomize
randomize(infile, outfile)

# Output patchfile

# Patch ROM

# fix bootcode
assert(os.path.isfile('rn64crc2\\rn64crc.exe'))
os.system('rn64crc2\\rn64crc.exe "%s" -u' % outfile)
