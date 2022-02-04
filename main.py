from argument import args,ListSoftware
from  Nmap import checkOperator
import Baner
import os
from Color import Color as color

import getpass

if getpass.getuser() != "root":
    print(color.CRED + ' program need to root permission please use sudo' +
          color.CEND)
    exit()

Baner.Baner(Baner.BanerMain)

if args.List == ListSoftware.get("Nmap"):
    Baner.Baner(Baner.BanerNmap)
    numberOperation = input(color.CBLUE + "please enter numberOperation:" +
                            color.CEND)
    checkOperator(numberOperation)                        

elif args.List == ListSoftware.get("Ping"):
    os.system("ping -c 4 " + args.Url)

else:
    print(color.CRED + 'Error please for help -h' + color.CEND)
