#pip install socket
#pip install os-sys
from socket import *

import os

targetserver = input("Enter ip for scan : ")

targetIP = gethostbyname(targetserver)

print ("Ready to scan : ", targetIP)
