#write a function named multiply, which
#will take two integers as arguments
#and it will return the product
#Then ask two integers from user and print the product
#using the method multiply

def multiply(a,b):
    return a*b

x=int(input("number 1= "))
y=int(input("number 2= "))

print(f"The result is {multiply(x,y)}")