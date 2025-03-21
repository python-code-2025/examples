# Writing to a text file
with open("data.txt", "a") as file:
    file.write("Hello, World again!")
    #writelines will add a line break
    file.writelines("New Line")
    file.writelines("New Line again")