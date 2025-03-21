import re
pattern = "a+?"
result = re.search(pattern, "The name of the Cat is Garfield")
if result:
    print(f"The index of fisrt a={result.start()}") 