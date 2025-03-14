def sum_numbers(*args):
    return sum(args)

x=sum_numbers(1,2,8)
print(f"sum is {x}")

def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print("test1")
display_info(name="Alice", age=30, city="New York")
print("test2")
display_info(brand="Volvo", model="s70")

def introduce(name, age, city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city}.")

introduce('Teppo',45,'Oulu')
introduce(name="Alice", age=30, city="New York")
introduce(age=30, city="New York", name="Jussi")