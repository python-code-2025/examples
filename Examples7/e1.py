# Writing to a text file
with open("data.txt", "w") as file:
    file.writelines("Row 1")
    file.writelines("Row 2")
    #writelines will add a line break
    #file.writelines("Hello, World!")

# Reading a text file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)