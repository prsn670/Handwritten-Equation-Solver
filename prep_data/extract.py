import patoolib as plib
from constants.constants import EXTRACT_LOCATION


def extract_data(filepath):
    print(f'extracting to {EXTRACT_LOCATION}')
    plib.extract_archive(filepath, outdir=EXTRACT_LOCATION)
