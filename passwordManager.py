# This program is a password manager that will take user input [website name], ie. 'facebook' (without quotes),
# and create a secure password for that website, that is easy for the user to remember, but hard for others to guess because it is based off a forumla.
# It will also store these passwords into an excel file for the user to access.

# Formula: ABCnx[website name][#letters in website name]nDEF[#ABCDEF].*

# Explaination of formula:
    # ABCDEF represents 6 things important to the user in someway; something they would always remember (ie. your 6 favorite fruits)
        # Those 6 items need to each start with a unique letter for this to work.
    # The n in the equation stands for a number, something the user would remember, (ie. a favorite number)
    # The x stands for a letter, which can also be changed to any random letter meaningful to the user.
    # [website name], ie. 'facebook'
    # [#letters in website name], ie. 'facebook' has 8 letters so the number would be 8
    # [#ABCDEF] (numFavs) is the number of these (so 0-6), which end up appearing in this particular result, ie. the number of letters that appear in the website name.
        # ie. for facebook it would be 5 for these particular letters.
    # The brackets are not part of the formula.
    # Obviously, the special characters at the end could be changed as well if desired, but would have to be edited further down in the program.
    
# Key. Here is where you would change any parts of the formula you desire.

a = 'A'
b = 'B'
c = 'C'
d = 'D'
e = 'E'
f = 'F'
x = 'x'
n = '5'

newPW = ''

# get user input for what website they need a password for
print('Please enter name of website for which you need a password')
input = input()
input = input.upper()

# find part1 = ABC5x
part1 = ''
for i in input:
    print(i)
    if i == a or i == a:
        if i not in part1:
            part1 = i
for i in input:
    if i == b or i == b:
        if i not in part1:
            part1 += i
for i in input:
    if i == c or i == c:
        if i not in part1:
            part1 += i
part1 = part1.upper() + str(n)+'x'

# find part2 = [website][#letters in website]x
part2 = ''
count = 0
part2 += str(input[0].lower()) + str(input[-1].lower())
for i in input:
    count += 1
part2 += str(count) + 'x'

# find part3 = DEF[#ABCDEF].*
part3 = ''
numFavs = 0
for i in input:
    if i == d or i == d:
        if i not in part3:
            part3 = i
for i in input:
    if i == e or i == e:
        if i not in part3:
            part3 += i
for i in input:
    if i == f or i == f:
        if i not in part3:
            part3 += i
part3 = part3.upper()            
for i in part1:
    if i == a or i == b or i == c:
        numFavs += 1
for i in part3:
    if i == d or i == e or i == f:
        numFavs += 1
part3 += str(numFavs) + '.*'

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
