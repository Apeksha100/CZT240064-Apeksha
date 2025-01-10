import requests

def fetch_user_data(user_id):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        user_data = response.json()
        
        print(f"Name: {user_data['name']}")
        print(f"Email: {user_data['email']}")
        print(f"Address: {user_data['address']['street']}, {user_data['address']['city']}")
    else:
        print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")

fetch_user_data(2)
