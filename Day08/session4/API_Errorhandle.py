import requests # type: ignore

url = "https://jsonplaceholder.typicode.com/invalid"

response = requests.get(url)

if response.status_code == 200:
    print("Success")
else:
    print("Error:", response.status_code)