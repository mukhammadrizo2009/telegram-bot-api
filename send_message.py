import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

params = {
    'chat_id':6293681152,
        'text':'It is great!'
}

response = requests.get(url=url , params=params)

print(response.status_code)