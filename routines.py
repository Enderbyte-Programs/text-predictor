import random
import utils
import config

def analyze(raw:str) -> dict[str,dict[str,int]]:
    total_chars = len(raw)
    p_total_chars = utils.parse_size(total_chars)

    finaldict = {}
    for m in range(config.CONFIG["context_characters"],0,-1):
        tdict: dict[str,dict[str,int]] = {}
        uniquechars = []

        #Iterate through characters
        ci = 0
        for character in raw:

            if ci+m+1 == total_chars:
                break
            for i in range(1,m):
                character += raw[ci+i]

            if not character in uniquechars:
                uniquechars.append(character)
            
            afterchar = raw[ci + m]
            if not character in tdict:
                tdict[character] = {}
            if afterchar in tdict[character]:
                tdict[character][afterchar] += 1
            else:
                tdict[character][afterchar] = 1

            ci += 1
        finaldict[str(m)] = tdict
    print("Analysed ",p_total_chars,f" ({len(list(finaldict.keys()))} rounds)")
    return finaldict

def generate(analysis:dict,noc:int,prompt:str) -> str:
    if prompt == "":
        final = random.choice(list(analysis[str(config.CONFIG["context_characters"])].keys()))
    else:
        final = prompt

    active_context_characters = config.CONFIG["context_characters"]

    for i in range(noc):
        while True:
            try:
                lastchar = ""
                for i in range(-active_context_characters,0):
                    #Counts from -x to 0
                    lastchar += final[i]
                    
                probarray = []
                for pset in analysis[str(active_context_characters)][lastchar].items():
                    probarray.extend([pset[0] for _ in range(pset[1])])

                final += random.choice(probarray)
                active_context_characters = config.CONFIG["context_characters"]
                break
            except:
                active_context_characters -= 1
                if active_context_characters == 0:
                    return final + " || Unfortunately, not enough content could be generated. Please provide more training data."
    return final