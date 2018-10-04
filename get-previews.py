from argparse import ArgumentParser
from fnmatch import filter as fnfilter
from glob import glob
from os.path import dirname, exists, join
from zipfile import ZipFile

parser = ArgumentParser(description='Extract thumbnail images from F3D files')
parser.add_argument('--force', action='store_true', help='overwrite existing thumbnails')
args = parser.parse_args()

f3dfiles = glob('**/*.f3d')

for f3dfile in f3dfiles:
    productname = dirname(f3dfile)
    targetimagepath = join(productname, '{}.png'.format(productname))
    if exists(targetimagepath) and not args.force:
        print('Preview image for {} already exists; skipping (pass --force to override)'.format(productname))
        continue

    zipfile = ZipFile(f3dfile)
    pngs = fnfilter(zipfile.namelist(), '**/Previews/*.png')
    if len(pngs) <= 0:
        print('Could not find a preview image for {}; skipping'.format(productname))
        continue
    biggestPNG = sorted(pngs, key=(lambda png: zipfile.getinfo(png).file_size))[0]

    with open(targetimagepath, 'wb') as f:
        f.write(zipfile.read(biggestPNG))

    print('Extracted preview image for {}'.format(productname))