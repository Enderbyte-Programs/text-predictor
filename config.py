import json
import os
import platform

_default_config = {
    "context_characters" : 5,
    "banned_characters" : ["\r","\n"]
}

CONFIG:dict
data_path:str
config_path:str
training_path:str

def load():
    global CONFIG
    global data_path, config_path, training_path
    if platform.system() == "Windows":
        data_path = os.path.expandvars(f"%APPDATA%{os.sep}dumbai")
    else:
        data_path = os.path.expanduser("~/.local/share/dumbai")

    config_path = data_path + os.sep + "config.json"
    training_path = data_path + os.sep + "data"

    if not os.path.isdir(training_path):
        os.makedirs(training_path)

    CONFIG = {}

    if not os.path.isfile(config_path):
        CONFIG = _default_config
    else:
        with open(config_path) as f:
            CONFIG = json.load(f)
    writeappdata()

def writeappdata():
    with open(config_path,"w+") as f:
        f.write(json.dumps(CONFIG))