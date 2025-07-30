import requests
from settings import TOKEN

url_get_updates = f'https://api.telegram.org/bot{TOKEN}/getUpdates'
url_send_message = f'https://api.telegram.org/bot{TOKEN}/sendMessage'


with open('last_update.txt', 'r') as f:
    last_update_id = int(f.read())

while True:
    params = {
        'offset': last_update_id
    }
    r = requests.get(url_get_updates)

    data = r.json()
    result = data['result']

    # for update in result:
    #     msg = update['message']
    #     user = update['message']['from']

    #     text = msg['text']

    #     if text == '/start':
    #         params = {
    #             'chat_id': user['id'],
    #             'text': 'salom echo botga xush kelibsiz\nbu bot text yozsangiz echo qiladi.'
    #         }
    #         requests.get(url=url_send_message, params=params)
    #     else:
    #         params = {
    #             'chat_id': user['id'],
    #             'text': text
    #         }
    #         requests.get(url=url_send_message, params=params)

    last_update_id = result[-1]['update_id']
    with open('last_update.txt', 'w') as f:
        f.write(f'{last_update_id}')
        
    