

import os
from random import randint

## Number of days you want to make commits
for i in range(1,60):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('file.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add .')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "first commit"')

## push the commit to github
os.system('git push -u origin master')