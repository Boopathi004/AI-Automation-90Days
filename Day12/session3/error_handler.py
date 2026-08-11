import requests #type: ignore

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url)

    print("Status Code:", response.status_code)
    print(response.json())

except requests.exceptions.RequestException as error:
    print("API Error:", error)