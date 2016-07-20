import os
import urllib
from wand.image import Image

OUT_BASE = os.path.join(os.getcwd(), "img", "pokedex")
OUT_FULL = os.path.join(OUT_BASE, "full")
OUT_SMALL = os.path.join(OUT_BASE, "small")

OUT_256 = os.path.join(OUT_BASE, "256")
OUT_128 = os.path.join(OUT_BASE, "128")
OUT_64 = os.path.join(OUT_BASE, "64")
OUT_32 = os.path.join(OUT_BASE, "32")

for i in xrange(1,721):
  filename = "{0:03d}.png".format(i)
  full_file = os.path.join(OUT_FULL, filename)

  out_256 = os.path.join(OUT_256, filename)
  out_128 = os.path.join(OUT_128, filename)
  out_64 = os.path.join(OUT_64, filename)
  out_32 = os.path.join(OUT_32, filename)

  with Image(filename=full_file) as img:
    img.resize(256,256)
    img.save(filename=out_256)
    img.resize(128,128)
    img.save(filename=out_128)
    img.resize(64,64)
    img.save(filename=out_64)
    img.resize(32,32)
    img.save(filename=out_32)

  print "Done with %s" % (filename)

