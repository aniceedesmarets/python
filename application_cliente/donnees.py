import requests


def getDonnees():
    r = requests.get("http://localhost:5000/data/")
    data=r.json()
    print(data)
    return data