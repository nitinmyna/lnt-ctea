with open("example.txt", "r", encoding="utf-8") as file: # file will be closed implicitly
    content = file.read()
    print(content)
# print(content)
