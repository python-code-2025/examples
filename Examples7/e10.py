import json

# Read the JSON file
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)  # Load JSON data into a Python list

# Print the data in the required format
for person in data:
    print(f"Name={person['name']}, Age={person['age']}")