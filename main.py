import pandas as pd
import random
import time

print('''
>>> k-tober Random.Gen <<<
>>> MuchaMocha <<<
runtime: 5 s
version: 1.0

-*-*-*-*-*-*-''')
time.sleep(1)
#name output with user spec
output=input('''
Enter output file title.
Press enter.
'output'= ''')

time.sleep(0.5)
print('''
-*-*-*-*-*-*-

preparing to pester the Pale Elf... 
''')

#kinktober df generator - bg3
oct_total=31

in1='characters.txt'
in2='kinks.txt'

with open (in1,'r') as f:
    lines=f.readlines()
with open (in2,'r') as f2:
    lines2=f2.readlines()
    
#characters dictionary
c1={}
for line in lines:
    number,value=line.split(':')
    key=int(number)
    value=value.strip(" ,\n")
    c1[key]=value

#kink dictionary
kink={}
for line in lines2:
    number,value=line.split(':')
    key=int(number)
    value=value.strip(" ,\n")
    kink[key]=value

#populate dataframe columns as lists, with an element for each day in october
character_top=[]
character_bottom=[]
counter=0
date_end=oct_total
for i in range(0,date_end):
    choicea=random.choice(c1)
    choiceb=random.choice(c1)
    #remove duplicate A,B characters:
    checking=True
    while checking:
        if choicea==choiceb:
            choiceb=random.choice(c1)
        else:
            checking=False
    character_top.append(choicea)
    character_bottom.append(choiceb)

time.sleep(1.5)
print('''...characters selected...
''')


kink_list=[]
counter=0
for i in range(0,date_end):
    if counter=='date_end':
        break
    choice3=random.choice(kink)
    kink_list.append(choice3)
    counter=0+1

time.sleep(1.5)
print('''...kinks randomized...
''')

date=[]
counter=0
for day in range(1,date_end+1):
    if counter=='date_end':
        break
    date.append(day)
    counter=counter+1


#populate dataframe 
dict={
    'Oct.':date,
    'A':character_top,
    'B':character_bottom,
    'Kink':kink_list,
}

#df gen
df=pd.DataFrame(dict)

#output files
df.to_csv(f'{output}.csv',index=False)
df.to_html(f'{output}.html',index=False)

time.sleep(1.5)
print(f'''...successfully generated 
"{output}" files.

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