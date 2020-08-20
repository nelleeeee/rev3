import requests

TOKEN = "6c8cce4e59016edbc3682a6cd93c4113fa21dc96"

headers = {
    "Authorization": f"Token {TOKEN}",
}

res = requests.get("http://localhost:8000/post/1", headers=headers)
print(res.json())
