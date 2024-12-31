import requests
import os

# def create_demo():
#     # Load the token from the file
#     token_path = os.path.expanduser('~/token')
#     if not os.path.exists(token_path):
#         raise FileNotFoundError(f"Token file not found at {token_path}")
    
#     with open(token_path, 'r') as f:
#         token = f.read().strip()

#     # Make the request to the seam-backend
#     url = 'http://seam-backend/endpoint'  # Replace with the actual URL of your service
#     headers = {'Authorization': f'Bearer {token}'}
#     response = requests.post(url, headers=headers)

#     if response.status_code == 200:
#         print("Created successfully! Not really! This is a mere show of potential.")
#     else:
#         print(f"Failed to create demo. Status code: {response.status_code}")
#         print(response.text)



def create_demo():
    print("hello world")
