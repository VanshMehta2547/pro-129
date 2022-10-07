import csv
dwarf_stars = []
with open("C:/Users/vansh/Downloads/dwarf_stars.csv") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        dwarf_stars.append(i)

bright_stars = []
with open("C:/Users/vansh/Downloads/bright_stars.csv") as f:
    csvreader = csv.reader(f)
    for i in csvreader:
        bright_stars.append(i)
    
header1 = dwarf_stars[0]
header2 = bright_stars[0]

header = header1 + header2

data1 = dwarf_stars[1:]
data2 = bright_stars[1:]

data = []
for i in data1:
    data.append(i)
for i in data2:
    data.append(i)

with open('total_stars.csv','w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(header)
    csvwriter.writerows(data)