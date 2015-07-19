import platform
if(platform.system() == "Windows"):
    slash = "\\"
else:
    slash = "/"

import sys
sys.path.insert(0,"../../../pythonModules")

import pm


