file = open("example.txt", "r", encoding="utf-8")
content = file.readlines() # returns a list of strings. Each string is a line of text in the file.
file.close() # we must close the file explicitly
for line in content:
    print(line.strip())

#print(content)


