# Writing to a binary file
with open("data.bin", "wb") as file:
    data = b"Hello, Binary World!"  # Binary string (bytes)
    file.write(data)

# Reading a binary file 
with open("data.bin", "rb") as file:
    data = file.read()  # Read the binary data
    print(data)  # Print the raw binary content