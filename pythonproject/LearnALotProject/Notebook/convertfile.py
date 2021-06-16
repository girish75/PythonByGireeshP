import os
import sys

from PIL import Image

for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                print("outfile = ", outfile.title())
                im.save(outfile)
        except OSError:
            print("cannot convert", infile)
