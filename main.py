import os
import config
config.load()
from runtime_config import *
import routines
import cacher
import utils
import ui
import hashlib

def reset_ui():
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

def ui_ci() -> dict:
    op = ui.option_menu("How would you like to input training data?",["Load from file","Type"])
    if op == 0:
        fpath = ui.fileinput("Paste the path to a file to train from it.")
        d = cacher.get_by(fpath)
        return d
    else:
        rt = ui.strinput("Paste training text here, then press enter.")
        fpath = config.training_path+os.sep+f"paste-{hashlib.md5(rt.encode()).hexdigest()}.txt"
        with open(config.training_path+os.sep+f"paste-{hashlib.md5(rt.encode()).hexdigest()}.txt","w+") as f:
            f.write(rt)
        d = cacher.get_by(fpath)
        return d

if not INTERACTIVE:


    if MODE == Modes.GENERATE:
        analy = cacher.get_by(TRAINING_FILE,FORCE_RETRAIN)
        gx = routines.generate(analy,GENERATE_CHARS,"")
        print(gx)


    if MODE == Modes.RESET:
        reset_ui()


    if MODE == Modes.DEBUG:
        print("Analysis of ",TRAINING_FILE)
        analy = cacher.get_by(TRAINING_FILE,FORCE_RETRAIN)
        for entry in analy.items():
            print(entry[0]," ->")
            for item in entry[1].items():
                print("    ",item[0]," = ",item[1])

else:
    print("Hello, welcome to the world's stupidest AI.")
    while True:
        op = ui.option_menu("Choose an option",["Generate","Analyze","Reset","Quit"])
        if op == 3:
            print("Goodbye")
            break
        elif op == 2:
            if ui.yesno("Are you sure you want to clear the cache?"):
                reset_ui()
        elif op == 1:
            
            #selfile = ui.fileinput("Paste a file to use for training")
            analy = ui_ci()
            for entry in analy.items():
                print(entry[0]," ->")
                for item in entry[1].items():
                    print("    ",item[0]," = ",item[1])

        elif op == 0:
            analy = ui_ci()
            iprompt = ui.strinput("Choose a prompt. For a random prompt, press enter now.")
            if len(iprompt) < config.CONFIG["context_characters"] and iprompt != '':
                print("Prompt too short; disregarding.")
            c2g = ui.intinput("How many characters to generate?",0)

            gx = routines.generate(analy,c2g,iprompt)
            print("AI SEZ: ",gx)
            input("Press enter to return to the menu.")
