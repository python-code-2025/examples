from calculator15 import Calculator

try:
    x=float(input("Give number1: "))
    y=float(input("Give number2: "))
except:
    print("You should give numbers")

objectCalculator=Calculator
objectCalculator.multiply(x,y)

Calculator.divide(x,y)

#Testing wrong arguments
objectCalculator.multiply("a5","b")