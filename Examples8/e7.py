import re
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

email=input("give your email: ")

result = re.match(pattern, email)

if result:
    print("valid email")

else:
    print("Not valid email")