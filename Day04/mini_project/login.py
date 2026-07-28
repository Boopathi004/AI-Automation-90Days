username = input("Username: ")
password = input("Password: ")

try:

    if username != "admin":
        raise Exception("Invalid Username")

    if password != "1234":
        raise Exception("Invalid Password")

    print("Login Successful")

except Exception as e:
    print(e)