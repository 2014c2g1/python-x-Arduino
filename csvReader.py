import csv
with open('example.csv','r') as file:
    r = csv.reader(file)
    for row in r:
        print(row)
