import re
pattern = "hello"
result = re.search(pattern, "hello world")
print(f"The result={result}")
if result:
    print(result.group())  # Output: hello