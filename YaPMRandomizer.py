import os
import hashlib

from rando_module import randomize

from statics.version import __version__
from statics.rom_hash import __rom_hash__

def check_rom(infile):
    try:
        assert(os.path.isfile(infile))
    except AssertionError:
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
    except AssertionError:
        print('Error: Incorrect ROM. Please select a valid Paper Mario (U) ROM file!')
        exit(1)

def main():
    print(f'YaPMR - Yet another Paper Mario Randomizer v.{__version__}')

    infile = 'Paper Mario (U) [!].z64'
    # infile = 'Paper Mario (U) [!]_Debug.z64'
    outfile = 'PMRandomized.z64'

    # Open Rom and check if it is actually a PM rom
    check_rom(infile)

    # Randomize
    randomize(infile, outfile)

    # Patch ROM

    # Create patch file if necessary

    # Create spoiler log if necessary

    # Fix bootcode
    try:
        assert(os.path.isfile('rn64crc2\\rn64crc.exe'))
        os.system('rn64crc2\\rn64crc.exe "%s" -u' % outfile)
    except AssertionError:
        print('')
        exit(1)


if __name__ == '__main__':
    main()