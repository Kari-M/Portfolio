import shutil
import os
from time import time

##source = 'C:\Users\Kari\Desktop\original_docs'
##destination = 'C:\Users\Kari\Desktop\edited_docs'
##files = os.listdir(source)
##path = source + '\\'

def mins_since_mod(path):
    ##print path
    return (time() - os.path.getmtime(path)) / 60

###for f in files:
##    path = source + '\\' + f
##    if mins_since_mod(path) < (24*60):
##        shutil.move(path, destination)


                  









