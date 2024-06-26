import requests
import os
from dotenv import load_dotenv
import redis
import json

# Load environment variables
load_dotenv()

# Set up Redis connection
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# API details
token = os.environ.get('TOKEN')
headers = {'Authorization': f'Token {token}'}
url = 'https://codius.tech/api/v1/user/interests/'

# Cache key
cache_key = 'user_interests'

# Function to get data from API
def get_from_api():
    response = requests.get(url, headers=headers)
    return response.json()

# Try to get data from Redis cache
cached_data = redis_client.get(cache_key)

if cached_data:
    # Data found in cache
    print("Data retrieved from cache:")
    data = json.loads(cached_data)
else:
    # Data not in cache, fetch from API
    print("Data not in cache, fetching from API:")
    data = get_from_api()
    
    # Store the data in Redis with an expiration time (e.g., 1 hour)
    redis_client.setex(cache_key, 3600, json.dumps(data))

# Process the data
print(data)
