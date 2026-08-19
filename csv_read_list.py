import csv

with open("people.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print('-' * 45)
    print('%-15s %-15s %s'%(header[0], header[1], header[2]))
    print('-' * 45)
    for row in reader:
        print('%-15s %-15s %s'%(row[0], row[1], row[2]))
        #print(f"{row['Name']} is {row['Age']} years old and works as a {row['Profession']}.")
    print('-' * 45)