import re
pattern = "[aeiou]"
result = re.findall(pattern, "hello world")

if result:
    print("match")
    print(result)  # Output: ['e', 'o', 'o']
else:
    print("No match")