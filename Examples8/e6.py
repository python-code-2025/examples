#Read file data.txt and replace Teppo with Lisa
# Reading a text file
import re
with open("data.txt", "r") as file:
    content = file.read()
    result = re.sub("Teppo", "Lisa", content)
    print(result)

# Writing to a text file
with open("data.txt", "w") as file:
    file.write(result)