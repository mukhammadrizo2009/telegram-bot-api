from pprint import pprint
import requests
from settings import TOKEN
import time

url_get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
url_send_message = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

with open('last_update.txt' , 'r') as file:
    last_update_id = int(file.read())

while True:
    params = {
        'offset': last_update_id
    }
    response = requests.get(url_get_updates)

    data = response.json()
    result = data['result']
    for update in result:
        last_update = result[-1]
        msg = last_update['message']
        user = last_update['message']['from']

        text = msg('text')
        
        if text == '/start':
            params = {
                'chat_id': user['id'],
                'text':"Salom , bizning botga\nXush kelibsiz!"
            }
            requests.get(url=url_send_message , params=params)
            time.sleep(0.3)
            
            
        else: 
            params = {
                    'chat_id': user['id'],
                        'text':text
                }
            requests.get(url=url_send_message , params=params)
            time.sleep(0.3)
            
        last_update_id = result[-1]['update_id']
        
        with open('last_update.txt' , 'w') as file:
            file.write(f"{last_update_id}")
            
    time.sleep(0.3)