import re
pattern = "^hello"  # Matches 'hello' at the beginning of the string
result = re.search(pattern, "hello world")
print(bool(result))  # Output: True