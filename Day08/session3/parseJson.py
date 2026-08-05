import json

json_data = '''
{
"name":"Boopathi",
"age":26,
"city":"Dindigul"
}
'''

data = json.loads(json_data)

print(data["name"])
print(data["city"])