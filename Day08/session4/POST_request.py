import requests # type: ignore

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Python Automation",
    "body": "Learning REST APIs",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print(response.json())