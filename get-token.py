import requests

# Credentials
username = ''
password = ''

# Obtain the token 
token_response = requests.post('https://codius.tech/api-token-auth/', data={'username': username, 'password': password })

token = token_response.json()['token']

print(token)
