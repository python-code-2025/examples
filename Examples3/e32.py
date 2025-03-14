from my_module import greet

print(f"{greet("Liisa")}")

def greet(name):
    print("This is local greet")

greet("Jussi")

def greet(name):
    print("This is the new greet")

greet("Ville")