# monument

import jbase
import json
import sys
from getmac import get_mac_address
from os.path import expanduser
from socket import gethostname


def close():
  jbase.close()


def getuname():
 return "darwin" if sys.platform.startswith("darwin") \
  else "win32" if sys.platform.startswith("win32") else "linux"


def init(appdir=""):
 home = expanduser("~").replace("\\","/")
 uname = getuname()
 if uname == "darwin":
  appdir = "/Applications/Monument.app/Contents/Resources/app"
  userdir = home + "/Library/MonumentAI/user"
 elif uname == "win32":
  appdir = home + "/AppData/Local/Programs/ai.monument.app/resources/app"
  userdir = home + "/AppData/Local/MonumentAI/user"
 else:
  appdir = appdir + "/resources/app"
  userdir = home + "/.config/MonumentAI/user"

 with open(userdir + "/config/reg.json") as regfile:
   reg = json.load(regfile)
 key = reg["key"]
 name = reg["name"]
 pad = reg["pad"]
 host = gethostname()
 mac = get_mac_address()
 arg ={"hostname":host,"key":key,"mac":mac,"name":name,"pad":pad,
  "regs":0,"tok":"xae1hiz7ut","update":0}
 d=json.dumps(arg).replace('": ','":')
 jbase.init(appdir,uname)
 jbase.do("ARGV_z_=:'" + d + "';'" + key + "'")
 jbase.do("BINPATH_z_=:'" + appdir + "/j'")
 jbase.do("Userpath_z_=:'" + userdir + "'")
 jbase.do("(3 : '0!:0 y')<BINPATH,'/profile.ijs'")
 jbase.do("appinit 1")


def serve(maifile,csvfile,algo):
 cmd=json.dumps(("maisvr",("model",maifile,csvfile,algo)))
 return json.loads(jbase.call(cmd))
