class Display:
    def show(self, *args):
        if len(args) == 0:
            print("No arguments passed.")
        elif len(args) == 1:
            print(f"One argument passed: {args[0]}")
        elif len(args) == 2:
            print(f"Two arguments passed: {args[0]} and {args[1]}")
        else:
            print(f"{len(args)} arguments passed: {', '.join(map(str, args))}")

# Example usage:
display = Display()

# Simulating method overloading with different number of arguments
display.show()  # No arguments
display.show("Hello")  # One argument
display.show("Hello", "World")  # Two arguments
display.show("Hello", "World", 123, 4.56)  # More than two arguments