import json
from organize import organize

with open('messed_file.json') as file:
    messed_list = json.load(file)
    organize(messed_list)



