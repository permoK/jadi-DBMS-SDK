import requests
import os
from dotenv import load_dotenv

load_dotenv()

token =  os.environ.get('TOKEN')


headers = {'Authorization': f'Token {token}'}

response = requests.get('https://codius.tech/api/v1/user/resource/', headers=headers)

# Process the response
print(response.json())
