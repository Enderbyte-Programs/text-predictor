import utils
import os

def option_menu(prompt:str,options:list[str]) -> int:
    maxlen = max([len(s) for s in options])
    maxlen = max([maxlen,len(prompt)])
    blockedlist = list(utils.chunks(options,9))#Numbers 1 -> 9
    pageno = 0

    while True:
        print("="*maxlen)
        print(prompt)
        print("-"*maxlen)
        ii = 0
        for option in blockedlist[pageno]:
            ii += 1
            print(ii," - ",option)
        if pageno > 0 and len(blockedlist) > 1:
            print("p - Previous Page")
        if pageno < len(blockedlist)-1:
            print("n - Next Page")
        print("-"*maxlen)
        chop = input(">> ")

        if chop == "n" and pageno < len(blockedlist) - 1:
            pageno += 1
            print("-"*maxlen)
            continue

        if chop == "p" and pageno > 0:
            pageno -= 1
            print("-"*maxlen)
            continue

        try:
            chop = int(chop)
        except:
            print("Invalid Option")
            print("-"*maxlen)
            continue

        if chop > len(blockedlist[pageno]):
            print("Invalid Option")
            print("-"*maxlen)
        else:
            print("-"*maxlen)
            return chop-1 + pageno*9
        
def strinput(prompt:str) -> str:
    return input(prompt+" >>")

def yesno(prompt:str) -> bool:
    while True:
        s = strinput(prompt+" (y/n)")
        if s.lower().startswith("y"):
            return True
        elif s.lower().startswith("n"):
            return False
        else:
            print("Invalid option.")

def fileinput(prompt:str) -> str:
    while True:
        s = strinput(prompt)
        if not os.path.isfile(s):
            print("Please paste a full valid path.")
        else:
            return s

def intinput(prompt:str,minimum=None) -> int:
    while True:
        s = strinput(prompt)
        try:
            s = int(s)
        except:
            print("Invalid Input!")
            continue
        if minimum is not None:
            if s < minimum:
                print("Too low!")
                continue

        return s