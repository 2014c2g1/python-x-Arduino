import csv
data = [[1,2,3],['a','b','c'],['Python','Arduino','Programming']]
with open('example.csv','w', newline='') as f:
    w = csv.writer(f)
    for row in data:
        w.writerow(row)
