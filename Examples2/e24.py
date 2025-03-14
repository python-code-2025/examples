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

#in below syntax you have to convert the int variable
#to string using str()
sum=7
print("The sum of the numbers is "+str(sum))
name="Liisa"
print("The sum of the numbers is "+name)