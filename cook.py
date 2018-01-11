# Read vegtables into variable
import csv

with open('veggiewrite.csv') as vegtables:
    #Convert to JSON
    reader = csv.DictReader(vegtables)
    rows = list(reader)

for row in rows:
    print(row)

# Write vegtables variable into JSON

import json


with open('vegetables.json', 'w') as f:
    json.dump(rows, f, indent=2)