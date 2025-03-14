#you can add a word pass if you are going to write the
#impementation of the code later. And then there is no error
x=5
if x<10:
    pass
print("hi")

#function starts with a word def

def sayHello(name):
    print(f"Hello {name}")

sayHello("Teppo Testi")

def sumOfNumbers(a,b):
    print(f"The sum of {a} and {b} = {a+b}")

sumOfNumbers(4,6)

def secondSum(a,b):
    return a+b

sum=secondSum(3,7)
print(f"Sum of  and 7 ={sum}")

print(f"Sum of 5 and 8 ={secondSum(5,8)}")