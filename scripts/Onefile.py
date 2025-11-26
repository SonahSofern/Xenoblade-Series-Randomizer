import sys, os

if getattr(sys, 'frozen', False):  # If the app is running as a bundled executable
    isOneFile = True
else:
    isOneFile = False
    
    
def Directory(dir):
    '''Handles directories when a packed version of the randomizer
    Returns the properly formatted directory'''
    if not isOneFile:
        return dir
    else:
        return os.path.join(sys._MEIPASS, dir)
