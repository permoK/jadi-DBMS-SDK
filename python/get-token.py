import requests
import os
from dotenv import load_dotenv

load_dotenv()


# Credentials
username = os.environ.get('USERNAME')
password = os.environ.get('PASSWORD')

# Obtain the token 
token_response = requests.post('https://codius.tech/api-token-auth/', data={'username': username, 'password': password })

token = token_response.json()['token']

print(token)
