import requests
        
response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code == 200:
    data=response.json()
    #print(data)
    for x in data:
        print(f"Name:{x['name']}, Address:{x['address']['street']}")
else:
    print("Some error")