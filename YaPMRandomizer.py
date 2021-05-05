import os
import hashlib

from rando_module import randomize
from patch_module import patch_rom

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
    randomizer_settings = {}
    # Default Settings
    randomizer_settings['logic'] = 'no_logic'
    randomizer_settings['rando_type'] = 'vanilla_shuffle'
    randomizer_settings['shuffle_type'] = 'within_groups'
    randomizer_settings['shuffle_groups'] = ('repeatableItems','oneOffItems','keyItems','badges')

    randomized_locations = randomize(randomizer_settings)

    # Patch ROM
    general_settings = ['skip_devlogos', 'skip_intro', 'disable_demo']
    patch_rom(infile, outfile, general_settings, randomized_locations)

    # Create patch file if necessary

    # Output md5
    with open(outfile, 'rb') as f:
            f.seek(0)
            hasher = hashlib.md5()
            buf = f.read()
            hasher.update(buf)
            print('van: 1a491454b6afe2e8a7ce50967774225b')
            print('md5: ' + hasher.hexdigest())


if __name__ == '__main__':
    main()