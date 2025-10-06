import httpx

response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')

print(response.status_code)
print(response.json())

data = {
    "userId": 245,
    "title": "Ченить",
    "completed": True
}

response2 = httpx.post('https://jsonplaceholder.typicode.com/todos', json = data)

print(response2.status_code)
print(response2.json())