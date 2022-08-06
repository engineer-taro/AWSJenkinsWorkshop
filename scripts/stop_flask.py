print('initial')
import requests

try:
    print('try')
    requests.post("http://127.0.0.1/shutdown")
except Exception as e:
    print('in exception')
    print(e)