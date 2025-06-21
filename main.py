import os
import config
config.load()
from runtime_config import *
import routines
import cacher
import utils

if not INTERACTIVE:


    if MODE == Modes.GENERATE:
        analy = cacher.get_by(TRAINING_FILE,FORCE_RETRAIN)
        gx = routines.generate(analy,GENERATE_CHARS)
        print(gx)


    if MODE == Modes.RESET:
        print("Resetting cache")
        tts = 0
        _cwd = os.getcwd()
        _fls = os.listdir(config.training_path)
        os.chdir(config.training_path)
        for file in _fls:
            tts += os.path.getsize(file)
            os.remove(file)
        os.chdir(_cwd)
        print(f"Freed {utils.parse_size(tts)}")


    if MODE == Modes.DEBUG:
        print("Analysis of ",TRAINING_FILE)
        analy = cacher.get_by(TRAINING_FILE,FORCE_RETRAIN)
        for entry in analy.items():
            print(entry[0]," ->")
            for item in entry[1].items():
                print("    ",item[0]," = ",item[1])