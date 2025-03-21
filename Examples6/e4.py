my_list = ["Teppo","Liisa","Jussi",34]
print(my_list)
print(f"Second element={my_list[1]}")

print("All in one row:")
for x in my_list:
    print(x, end= " ")
print()
print("all in new row:")

for x in my_list:
    print(f"name={x}")

test=my_list.index("Liisa")
print(f"Index of Liisa={test}")
for index, value in enumerate(my_list):
    print(f"{index} : {value}")