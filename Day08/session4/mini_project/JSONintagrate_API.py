import requests # type: ignore

url = "https://jsonplaceholder.typicode.com/users"

response = requests.get(url)

if response.status_code == 200:

    users = response.json()

    print("=" * 60)
    print("EMPLOYEE DIRECTORY")
    print("=" * 60)

    for user in users:

        print(f"ID      : {user['id']}")
        print(f"Name    : {user['name']}")
        print(f"Username: {user['username']}")
        print(f"Email   : {user['email']}")
        print(f"Company : {user['company']['name']}")
        print("-" * 60)

else:

    print("Unable to fetch employee data.")