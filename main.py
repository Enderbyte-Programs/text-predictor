import random
import config
config.load()

TRAINING_FILE = "training-american.txt"

with open(TRAINING_FILE,encoding="utf-8") as f:
    raw = f.read()
    for fc in config.CONFIG["banned_characters"]:
        raw = raw.replace(fc," ")
    raw = raw.replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ").replace("  "," ")

total_chars = len(raw)

tdict: dict[str,dict[str,int]] = {}
uniquechars = []

#Iterate through characters
ci = 0
for character in raw:

    if ci+config.CONFIG["context_characters"]+1 == total_chars:
        break

    #character += raw[ci+1]
    #character += raw[ci+2]
    #character += raw[ci+3]
    #character += raw[ci+4]
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

#print(tdict)

chars2gen = int(input("How many characters? >>"))

final = random.choice(list(tdict.keys()))
for i in range(chars2gen):
    #lastchar = final[-5] + final[-4] + final[-3] + final[-2] + final[-1]
    lastchar = ""
    for i in range(-config.CONFIG["context_characters"],0):
        #Counts from -x to 0
        lastchar += final[i]
    probarray = []
    for pset in tdict[lastchar].items():
        probarray.extend([pset[0] for _ in range(pset[1])])

    final += random.choice(probarray)

print(final)

# a += 2              a = a + 2