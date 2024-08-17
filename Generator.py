import pandas as pd
import random
import time

CHARACTER_DICT={}
KINK_DICT={}
OCT_TOTAL=31

#kinktober df generator - bg3

def listCreator(textFile):
    """Creates a list from a pre-defined string value"""
    dicky={}
    for line in textFile:
        number,value=line.split(':')
        key=int(number)
        value=value.strip(" ,\n")
        dicky[key]=value
    return dicky

def readFiles(in1,in2):
    """Reads files and makes lists out of them"""
    global CHARACTER_DICT
    global KINK_DICT
    with open (in1,'r') as f1:
        lines=f1.readlines()
        CHARACTER_DICT = listCreator(lines)
    with open (in2,'r') as f2:
        lines2=f2.readlines()
        KINK_DICT = listCreator(lines2)
    
def characterRandomizer():
    """Takes characters from Dictionary and randomizes them in a list"""
    character_top=[]
    character_bottom=[]
    for i in range(OCT_TOTAL):
        choicea=random.choice(CHARACTER_DICT)
        choiceb=random.choice(CHARACTER_DICT)
        #remove duplicate A,B characters:
        checking=True
        while checking:
            if choicea==choiceb:
                choiceb=random.choice(CHARACTER_DICT)
            else:
                checking=False
        character_top.append(choicea)
        character_bottom.append(choiceb)

    time.sleep(1.5)
    print('''...characters selected...
    ''')
    return character_top, character_bottom
def kinkRandomizer(character_top, character_bottom):
    """Randomizes the kinks into a list"""
    kink_list = []
    date = []
    day = 1
    for i in range(OCT_TOTAL):
        if i+1 =='OCT_TOTAL':
            break
        choice3=random.choice(KINK_DICT)
        kink_list.append(choice3)
        date.append(day)
        day+=1

    time.sleep(1.5)
    print('''...kinks randomized...
    ''')
    #populate dataframe 
    dict={
        'Oct.':date,
        'A':character_top,
        'B':character_bottom,
        'Kink':kink_list,
    }
    return dict
def dataFrameCreator(dict, fileName):
    df=pd.DataFrame(dict)

    #output files
    df.to_csv(f'{fileName}.csv',index=False)
    df.to_html(f'{fileName}.html',index=False)

        
def main():
    print("""
    >>> k-tober Random.Gen <<<
    >>> MuchaMocha <<<
    runtime: 5 s
    version: 1.0

    -*-*-*-*-*-*-""")
    time.sleep(1)
    #name output with user spec
    fileName=input("""
    Enter output file title.
    Press enter.
    'name'= """)

    time.sleep(0.5)
    print('''
    -*-*-*-*-*-*-

    preparing to pester the Pale Elf... 
    ''')
    readFiles('characters.txt', 'kinks.txt')
    character_top, character_bottom = characterRandomizer()
    dict = kinkRandomizer(character_top, character_bottom)
    dataFrameCreator(dict, fileName)

    time.sleep(1.5)
    print(f'''...successfully generated 
    "{fileName}" files.

    -*-*-*-*-*-*-
    ⣤⢤⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣿⠀⠀  go forth and live
    ⢹⣧⢸⠀          a life of sin.⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⢹⣧⢸⠀⠀⠀⠸⡆⠉⠵⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⣾⡄⠸⠀⠀⠀⠀⠈⠢⣀⣼⣞⣴⣰⡖⣒⡒⠦⠀⣀⣀⣀⡤⠊⠇⠀⠀⠀
    ⢿⡧⠀⠀⠀⠀⠀⠀⠰⢷⣿⣼⣿⣿⣿⣿⢲⣯⣿⣿⡮⠋⠀⠀⣺⠀⠀⠀
    ⣾⡇⠁⠀⠀⠀⠀⠀⠐⢵⣿⣿⠿⠻⠈⢿⣿⣻⣿⡟⠠⣀⠤⠈⡙⠀⠀⠀
    ⣿⡅⠀⠀⢀⣠⣶⠀⠀⠞⠋⠁⠀⠀⠐⡿⡇⠑⠁⠀⠈⠁⠀⢰⠃⠀⠀⠀
    ⢿⡇⠀⠀⢼⣿⣿⣷⣶⣶⣀⡀⣀⣀⣀⣀⣬⣥⣤⣄⣀⠤⠆⠀⠙⣆⠀⠀
    ⣏⡇⠀⠀⠀⠻⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣃⠀⠠⠀⠀⠘⣦⠀
    ⡟⠇⠀⠀⠀⠀⠈⠛⠻⠟⢇⣀⣈⠻⠿⣿⣿⡿⠿⠛⠁⠀⠦⠀⠀⠀⠘⣆
    ⡇⡇⠀⠀⢠⠀⠀⠀⠑⠤⠀⢿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⢹
    ⠧⠧⢄⣰⠃⠀⠀⠀⠀⠀⠈⠑⠒⠂⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
    ⠀⠀⣰⠃⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠐⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ''')

if __name__=="__main__":
    main()