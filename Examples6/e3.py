my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)
my_set = {1, 2, 3, 4, 5}
my_dict = {"name": "Teppo", "age": 25, "city": "Oulu"}

#nested dictionary=dictionary with several rows
my_dict2={
    "Teppo":{"age":30,"city":"Oulu"},
    "Liisa":{"age":32,"city":"Tampere"},
    "Ville":{"age":43,"city":"Oulu"}
}

print("The whole collection:")
print(my_list)
print(my_tuple)
print(my_set)
print(my_dict)
print(my_dict2)

print("\nThe first items from the collections:")
print(f"\tList 1.={my_list[0]}")
print(f"\tTuple 1.={my_tuple[0]}")
print(f"\tSet 1.= {next(iter(my_set))}")
print(f"\tDict 1.={my_dict['name']}")

print("One row from the nested dictionary:")
print(f"\tDict 2.={my_dict2["Teppo"]}")

print("One value from the nested dictionary:")
print(f"\tDict 2.={my_dict2["Teppo"]["age"]}")

print("LOOP1:")
for key in my_dict:
    print(key, end=" ") 

print("\nLOOP2:")
for value in my_dict.values():
    print(value, end=" ")

print("\nLOOP3:")
for key, value in my_dict.items():
    print(f"{key}: {value}")  

print("\nLOOP4:")
for key, value in my_dict2.items():
    print(f"{key}: {value}")  

#add values to collections 
print("\nNew values to collections:")
my_list.append(9)
print(f"\tmy_list: {my_list}")

#can not add to tuple

my_dict['phone']="040-1234567"
print(f"\tmy_dict: {my_dict}")

my_dict2["Anna"] = {"age": 28, "city": "Helsinki"}
print("\nmy_dict2:")
for key, value in my_dict2.items():
    print(f"{key}: {value}")  