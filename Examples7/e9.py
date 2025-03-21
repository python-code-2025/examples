import json

# Define the list of objects
data = [
    {"name": "Teppo", "age": 33},
    {"name": "Liisa", "age": 30}
]

# Write JSON data to a file
with open("data.json", "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4)

print("JSON file 'data.json' created successfully!")