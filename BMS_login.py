import requests
import json
from utils import get_API_info
from utils import get_BMS_url_info


def BMSLogin(user_name='admin', password='123456'):
    r = requests.post(get_BMS_url_info.BMS_login_url %(user_name, password))
    return r

"""
def getLoginInfo(user_name='admin', password='123456'):
    r = BMSLogin(user_name=user_name, password=password)['data']

    info_dict = dict(
                     
    )
"""
   
if __name__ == '__main__':
    print(BMSLogin())