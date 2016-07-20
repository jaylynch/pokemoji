import os
import urllib

OUT_BASE = os.path.join(os.getcwd(), "img", "pokedex")
OUT_FULL = os.path.join(OUT_BASE, "full")
OUT_SMALL = os.path.join(OUT_BASE, "small")

for i in xrange(1,721):
  filename = "{0:03d}.png".format(i)
  full_url = "http://assets.pokemon.com/assets/cms2/img/pokedex/full/%s" % (filename)
  small_url = "http://assets.pokemon.com/assets/cms2/img/pokedex/detail/%s" % (filename)

  full_file = os.path.join(OUT_FULL, filename)
  small_file = os.path.join(OUT_SMALL, filename)

  urllib.urlretrieve(full_url, full_file)
  urllib.urlretrieve(small_url, small_file)

  print "Done with %s" % (filename)

