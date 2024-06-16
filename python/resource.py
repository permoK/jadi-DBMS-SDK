import requests

token = ''

headers = {'Authorization': f'Token {token}'}

response = requests.get('https://codius.tech/api/v1/user/resource/', headers=headers)

# Process the response
print(response.json())
