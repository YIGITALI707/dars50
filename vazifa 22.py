import requests
from vazifa21 import db

URL = "https://dummyjson.com/comments"
def main():
    r = requests.get(URL)
    data = r.json()
    print(data)
    db.add_user(data['userss'])

if __name__ == "__main__":
    main()