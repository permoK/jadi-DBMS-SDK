import requests

token = TOKEN

headers = {'Authorization': f'Token {token}'}

response = requests.get('https://codius.tech/api/v1/user/interests/', headers=headers)

# Process the response
print(response.json())
