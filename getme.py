from pprint import pprint
import requests
from settings import TOKEN

url = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url)
pprint(response.url)