# test
# example of calling mai server

import monument
import sys
from os.path import expanduser

home = expanduser("~").replace("\\","/")

# ----------------------------------------------------------------------------
# if linux, set installation folder
# otherwise leave blank
if sys.platform.startswith("linux"):
 install = home + "/Monument"
else:
 install = ""

# ----------------------------------------------------------------------------
# start monument
monument.init(install)

# ----------------------------------------------------------------------------
# run models
maifile = home + "/maitest/insure.mai"
csvfile = home + "/maitest/insure2.csv"
algo = "Ent-Boost(AIG)"
res = monument.serve(maifile,csvfile,algo)
print(algo + ":")
print(res)

print("-----------------")

algo = "LightGBM(MET)"
res = monument.serve(maifile,csvfile,algo)
print(algo + ":")
print(res)
