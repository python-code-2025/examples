with open("data2.txt", "a") as file:

    for x in range(5):
        file.writelines(["Row ",str(x)])