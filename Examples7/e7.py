import csv

# Open and read the CSV file
with open("data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)  # Reads as a dictionary

    # Print only the "Age" column
    for row in reader:
        print(row)
        #print(row["Age"])