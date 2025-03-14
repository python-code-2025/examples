import random

# List all attributes of the random module
all_functions = dir(random)

# Filter only functions (ignoring dunder methods and variables)
random_functions = [func for func in all_functions if not func.startswith("__")]

# Print the list of functions
print(random_functions)
