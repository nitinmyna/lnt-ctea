import csv

with open("people.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print(type(reader))
    for row in reader:
        print(row)
        #print(f"{row['Name']} is {row['Age']} years old and works as a {row['Profession']}.")
    print(type(row))