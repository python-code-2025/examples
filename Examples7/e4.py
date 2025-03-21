# Reading a text file
with open("data2.txt", "r") as file:
    content = file.read()
    print(content)