import random
import config

def analyze(raw:str) -> dict[str,dict[str,int]]:
    total_chars = len(raw)

    tdict: dict[str,dict[str,int]] = {}
    uniquechars = []

    #Iterate through characters
    ci = 0
    for character in raw:

        if ci+config.CONFIG["context_characters"]+1 == total_chars:
            break
        for i in range(1,config.CONFIG["context_characters"]):
            character += raw[ci+i]

        if not character in uniquechars:
            uniquechars.append(character)
        
        afterchar = raw[ci + config.CONFIG["context_characters"]]
        if not character in tdict:
            tdict[character] = {}
        if afterchar in tdict[character]:
            tdict[character][afterchar] += 1
        else:
            tdict[character][afterchar] = 1

        ci += 1
    return tdict

def generate(analysis:dict,noc:int) -> str:
    final = random.choice(list(analysis.keys()))
    for i in range(noc):
        #lastchar = final[-5] + final[-4] + final[-3] + final[-2] + final[-1]
        lastchar = ""
        for i in range(-config.CONFIG["context_characters"],0):
            #Counts from -x to 0
            lastchar += final[i]
        probarray = []
        for pset in analysis[lastchar].items():
            probarray.extend([pset[0] for _ in range(pset[1])])

        final += random.choice(probarray)
    return final