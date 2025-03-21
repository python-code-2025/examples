import xml.etree.ElementTree as ET

# Create the root element
root = ET.Element("root")
people = ET.SubElement(root, "people")

# Define persons data
persons = [
    {"name": "Teppo", "age": "33"},
    {"name": "Liisa", "age": "30"}
]

# Add persons to the XML
for person_data in persons:
    person = ET.SubElement(people, "person")
    name = ET.SubElement(person, "name")
    name.text = person_data["name"]
    age = ET.SubElement(person, "age")
    age.text = person_data["age"]

# Create the tree and write it to a file
tree = ET.ElementTree(root)
with open("data.xml", "wb") as file:
    tree.write(file, encoding="utf-8", xml_declaration=True)

print("XML file 'data.xml' created successfully!")