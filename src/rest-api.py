# https://realpython.com/api-integration-in-python/
# https://thispointer.com/python-4-ways-to-print-items-of-a-dictionary-line-by-line/


import requests
import json

# Get
api_url = "https://jsonplaceholder.typicode.com/todos/1"
response = requests.get(api_url)

print('# response.json()')
print(response.json())

print(f'\n# Status code: {response.status_code}')

print(f'\n# Headers: {response.headers["Content-Type"]}')

print('\n# Print a dictionary line by line using for loop & dict.items()')
for key, value in response.json().items():
  print(key, ': ', value)

print('\n# Print a dictionary line by line by iterating over keys')
for key in response.json():
  print(key, ': ', response.json()[key])

print('\n# Print a dictionary line by line using List Comprehension')
[print(key, ':', value) for key, value in response.json().items()]

print('\n# Print a dictionary line by line using json.dumps()')
print(json.dumps(response.json(), indent=4))


# Post
data_post = {
  "userId": 1,
  "title": "Buy milk",
  "completed": False
}

api_url = "https://jsonplaceholder.typicode.com/todos"
# when you use json keyword argument, 'json=data_to_post', requests.post() autommatically sets the request's HTTP header Content-Type to application/json. It also serializes data_to_post into a json string, which it appends to the body of the request.
response = requests.post(api_url, json=data_post)
print(response.json())
print(response.status_code)


# if you don't use the json keyword argument to supply json data, then you need to set Content-Type accordingly and serialize the json manually. Here's an equivalent version to the previous code
data_post_header = {
  "userId": 2,
  "title": "Buy beer",
  "completed": True
}
headers = {"Content-Type": "application/json"}
response = requests.post(api_url, data=json.dumps(data_post_header), headers=headers)
print(response.json())
print(response.status_code)


# Patch
data_patch = {"title": "Mow lawn"}
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.patch(api_url, json=data_patch)
print(response.json())
print(response.status_code)

# Delete
api_url = "https://jsonplaceholder.typicode.com/todos/10"
response = requests.delete(api_url)
print(response.json())
print(response.status_code)
