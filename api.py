import requests
from tinydb import TinyDB

db = TinyDB('data.json', indent=4)

base_url = "https://randomuser.me/api/"

def get_users_by_gender(gender: str, n: int) -> list[dict]:
    payload = {
        'results': n,
        'gender': gender
    }

    resp = requests.get(base_url, params=payload)

    if resp.status_code == 200:
        users = []
        for user in resp.json()['results']:
            users.append({
                "first_name": user['name']['first'],
                "last_name": user['name']['last'],
                'age': user['dob']['age'],
                'country': user['location']['country']
            })

        return users

    return []

males = db.table('males')
females = db.table('females')

males.insert_multiple(get_users_by_gender('male', 443))
females.insert_multiple(get_users_by_gender('female', 321))
