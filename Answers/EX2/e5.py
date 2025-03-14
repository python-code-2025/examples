#pip install requests
import requests

# URL of the API (Example: JSON placeholder API)
url = "https://jsonplaceholder.typicode.com/todos/1"

try:
    # Send a GET request to fetch data
    response = requests.get(url)

    # Check if request was successful (Status Code 200)
    if response.status_code == 200:
        data = response.json()  # Convert response to JSON format
        print("Fetched Data:", data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
