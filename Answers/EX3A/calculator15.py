class Calculator:
    def multiply(a,b):
        try:
            print(f"{a}*{b} = {a*b}")
        except Exception as e:
            print(e)

    @staticmethod
    def divide(a,b):
        try:
            if(b==0):
                print("You can not divide by zero")
            else:
                print(f"{a}/{b} = {round(a/b,2)}")
        except Exception as e:
            print(e)