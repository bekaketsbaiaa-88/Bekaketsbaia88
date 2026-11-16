import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_user(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    if response.status_code == 404:
        return None
    response.raise_for_status()
    return response.json()


for user_id in [1, 2, 999]:
    user = get_user(user_id)
    if user is None:
        print(f"მომხმარებელი {user_id} ვერ მოიძებნა")
    else:
        print(f"{user['name']} | {user['email']} | {user['address']['city']}")
