import requests # type: ignore

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

print("Status Code:", response.status_code)
print(response.json())