import requests

response = requests.get('https://codius.tech/api/v1/user/')

# Process the response
print(response.json())
