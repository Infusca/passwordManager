# This program will take user input [website name] and create a random looking, hard to guess password, that is easy to remember.
# WTPKLO is based off 6 cats that I have had, but the user could of course tweak this program and replace those letters with any 6 things easy to remember for themselves.

# PW formula is WTP4x[wbst][# letters in wbst]xKLO[#cats].*
newPW = ''

# get user input for what website they need a password for
print('Please enter name of website for which you need a password')
input = input()

# find part1 = WTP4x
part1 = ''
for i in input:
    if i == 'W' or i == 'w':
        if i not in part1:
            part1 = i
for i in input:
    if i == 'T' or i == 't':
        if i not in part1:
            part1 += i
for i in input:
    if i == 'P' or i == 'p':
        if i not in part1:
            part1 += i
part1 = part1.upper() + '4x'

# find part2 = [wbst][# letters in wbst]x
part2 = ''
count = 0
part2 += str(input[0]) + str(input[-1])
for i in input:
    count += 1
part2 += str(count) + 'x'

# find part3 = KLO[#cats].*
part3 = ''
numCats = 0
for i in input:
    if i == 'K' or i == 'k':
        if i not in part3:
            part3 = i
for i in input:
    if i == 'L' or i == 'l':
        if i not in part3:
            part3 += i
for i in input:
    if i == 'O' or i == 'o':
        if i not in part3:
            part3 += i
part3 = part3.upper()            
for i in part1:
    if i == 'W' or i == 'T' or i == 'P':
        numCats += 1
for i in part3:
    if i == 'K' or i == 'L' or i == 'O':
        numCats += 1
part3 += str(numCats) + '.*'

newPW = part1 + part2 + part3
print("You're new password is: " + newPW)



# save pw to excel file
import pandas as pd
from os.path import exists

df = pd.DataFrame([[input, newPW]],
    columns=['Website','Password'])

# check to see if file exists. if True, append file. if False, create file.
file_exists = exists('savedPWs.xlsx')
if file_exists == False:
    df.to_excel('savedPWs.xlsx', index=False)
else:
    if file_exists == True:
        source = pd.read_excel('savedPWs.xlsx')
        update = pd.concat([source, df])
        update.to_excel('savedPWs.xlsx', index=False)


# read newly saved pw file and print it back for verification purposes
df = pd.read_excel('savedPWs.xlsx')
# print(df)
