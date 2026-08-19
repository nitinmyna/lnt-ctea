import csv

data = [
    ["Name", "Age", "Profession"],
    ["Alice", 30, "Engineer"],
    ["Bob", 25, "Designer"],
    ["Charlie", 35, "Manager"],
]
with open("people.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerows(data)
