import requests

api_url = "https://opentdb.com/api.php"
# original api url = https://opentdb.com/api.php?amount=10&type=boolean
parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get(api_url, params=parameters)
response.raise_for_status()
question_data = response.json()["results"]
