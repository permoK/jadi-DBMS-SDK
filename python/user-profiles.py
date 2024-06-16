import requests
import os
from dotenv import load_dotenv

load_dotenv()

token =  os.environ.get('TOKEN')

# Make a request to the protected view with the token
headers = {'Authorization': f'Token {token}'}
response = requests.get('http://127.0.0.1:8000/api/v1/user/interests/')

# Process the response
print(response.json())
