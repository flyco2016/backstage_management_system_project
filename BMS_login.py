import requests
import json
from utils import get_API_info
from utils import get_BMS_url_info


def BMSLogin(user_name='admin', password='123456'):
    data = get_API_info.BMS_login_data % (repr(user_name), repr(password))
    print(data, type(data), type(json.dumps(data)), sep='\n')
    r = requests.post(get_BMS_url_info.BMS_login_url)
    print(r.text)

if __name__ == '__main__':
    BMSLogin()