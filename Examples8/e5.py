import re

# re.match()
#result = re.match("world", "hello world")
result = re.match("hello", "hello world")
#result = re.search("world", "hello world")

if result:
    print("match")
    print(result.group())
else:
    print("no match")