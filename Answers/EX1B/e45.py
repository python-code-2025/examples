x=int(input("Give me number: "))
for num in range(1, x):
    if num % 7 == 0:
        print("First multiple of 7:", num)
        break