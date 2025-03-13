# API check using request method

import requests

endpoint = "http://"

response = requests.get(endpoint)

# Checking if the request was successful

if response.status_code == 200:
    print("API is up and running.")
else:
    print("API is not running.")