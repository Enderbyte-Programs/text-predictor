import hashlib
import config
import routines
import os
import json
import sys

def get_by(filepath:str,force_retrain:bool=False) -> dict[str,dict[str,int]]:
    tdir = config.training_path
    #Hash contents
    with open(filepath,encoding="utf-8") as f:
        data = f.read()
        for fc in config.CONFIG["banned_characters"]:
            data = data.replace(fc," ")
            data = data.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")
        hsh = hashlib.md5(data.encode()).hexdigest()
    cc = config.CONFIG["context_characters"]

    fullpath = tdir + os.sep + f"{hsh}-{cc}.json"

    if os.path.isfile(fullpath) and not force_retrain:
        with open(fullpath) as f:
            return json.load(f)
    else:
        analysis = routines.analyze(data)
        with open(fullpath,"w+") as f:
            f.write(json.dumps(analysis))
        return analysis
    