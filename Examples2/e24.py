#use try exception

def multiply(a,b):
    return a*b

try:
    x=int(input("number 1= "))
    y=int(input("number 2= "))

    print(f"The result is {multiply(x,y)}")
except Exception as e:
    print("ERROR:")
    print(e)
