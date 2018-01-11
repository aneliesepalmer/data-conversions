vegetables = [
 {"name": "eggplant"},
 {"name": "tomato"},
 {"name": "corn"},
 {"name": "potato"},
 {"name": "green bean"},
 {"name": "cucumber"},
 {"name": "carrot"},
]

# Write header file to csv
import csv

with open('veggiewrite.csv' , 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['vegetable' , 'length'])

# Loop through each vegetable
	for veggie in vegetables:
		name = veggie['name']
		length = len(name)
		writer.writerow([name, length])

# for each vegetable write a row to the csv