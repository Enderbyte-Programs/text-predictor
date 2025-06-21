import sys
import os
import enum

class Modes(enum.Enum):
    GENERATE = 0
    DEBUG = 1
    RESET = 2

def _try_get_ind(l:list,n:int) -> str:
    try:
        return l[n]
    except:
        return ""

def has_optional_argument(fullname:str) -> bool:
    return fullname in sys.argv

INTERACTIVE = True#If no arguments, assume that the user wants interactive mode
TRAINING_FILE = ""
GENERATE_CHARS = 0
MODE = Modes.GENERATE

ALLOW_OVERWRITE = has_optional_argument("--overwrite")
FORCE_RETRAIN = has_optional_argument("--force")

HELP_TEXT = """
** IMPORTANT - By running this program with command line arguments, you want non-interactive mode. If you would like to use interactive mode, please run this program without any arguments.

Usage: <action> [mandatory arguments] [optional arguments]

Actions:
    help: Print this help text and exit
    generate: Using a previous name, generate a certain number of characters*
    debug: Print the training information for a certain file to the console*
    reset: Delete all training files

Mandatory Arguments for each action

Generating
Usage: generate <file path> <# of characters>

Debugging / Analyzing file
Usage: debug <file path>

*Note: All data is printed to the console, so please use shell redirection to write it to a file.

Optional Arguments
--overwrite : it is OK to overwrite a files if needed.
--force     : even if the training file exists, delete it and redo training.

"""

args = sys.argv[1:]
verb = _try_get_ind(args,0)
#Verb can be help | generate | train | reset
action1 = _try_get_ind(args,1)
action2 = _try_get_ind(args,2)

if verb != "":
    INTERACTIVE = False

if verb == "help" or verb == "--help":
    print(HELP_TEXT)
    sys.exit()

elif verb == "generate":
    MODE = Modes.GENERATE
    if not os.path.isfile(action1):
        print("Error - Please specify a valid training input file")
        sys.exit(-1)
    else:
        TRAINING_FILE = action1
    try:
        GENERATE_CHARS = int(action2)
    except:
        print("Error - please specify a whole number of characters to generate")
        sys.exit(-1)
    
elif verb == "debug":
    MODE = Modes.DEBUG
    if not os.path.isfile(action1):
        print("Error - Please specify a valid training input file")
        sys.exit(-1)
    TRAINING_FILE = action1

elif verb == "reset":
    MODE = Modes.RESET

elif verb == "":
    pass

else:
    print("Error - not a valid action. ")
    sys.exit(-1)