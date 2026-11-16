import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def crud_tour():
    # 1. CREATE
    new_post = {"title": "ახალი პოსტი", "body": "ტექსტი", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    new_id = response.json()["id"]
    print(f"CREATE: {response.status_code}, id={new_id}")

    # 2. READ
    response = requests.get(f"{BASE_URL}/posts/{new_id}")
    print(f"READ {new_id}: {response.status_code}")

    # 3. UPDATE (PUT)
    full_post = {"id": 1, "title": "სრულად შეცვლილი", "body": "ახალი ტექსტი", "userId": 1}
    response = requests.put(f"{BASE_URL}/posts/1", json=full_post)
    print(f"UPDATE (PUT): {response.status_code}, title={response.json()['title']}")

    # 4. UPDATE (PATCH)
    response = requests.patch(f"{BASE_URL}/posts/1", json={"title": "ნაწილობრივ შეცვლილი"})
    print(f"UPDATE (PATCH): {response.status_code}, title={response.json()['title']}")

    # 5. DELETE
    response = requests.delete(f"{BASE_URL}/posts/1")
    print(f"DELETE: {response.status_code}, {response.json()}")


crud_tour()
