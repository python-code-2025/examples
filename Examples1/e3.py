print("Loop 1")
for row in range(5):
    print(f"Row is {row}")

print("Loop 2")
for row in range(1,5):
    print(f"Row is {row}")

print("Loop 3")
for row in range(1,10,2):
    print(f"Row is {row}")

#print every value in new line
for x in range (1,5):
    print(x)
#print comma after every value
for x in range(1,5):
    print(x, end=",")
print()
print("do not write comma after the last value")
#do not write comma after the last value
for x in range(1,5):
    if x<4:
        print(x, end=',')
    else:
        print(x)