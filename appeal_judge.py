import requests
import json
from BMS_login import BMSLogin
from utils import get_API_info
from utils import get_BMS_url_info


def judgeBuyerWin(user_name='admin', password='123456', order_ID_NO=None):

    #data = get_API_info.BMS_login_data % (repr(user_name), repr(password))
    #print(data, type(data), type(json.dumps(data)), sep='\n')
    BMSLogin(user_name=user_name, password=password)
    r = requests.post(get_BMS_url_info.appeal_judge_buyer_win_url % repr(order_ID_NO))
    #print(r.text)
    return r.json()

def judgeSellerWin(user_name='admin', password='123456', order_ID_NO=None):
    #data = get_API_info.BMS_login_data % (repr(user_name), repr(password))
    #print(data, type(data), type(json.dumps(data)), sep='\n')
    BMSLogin(user_name=user_name, password=password)
    r = requests.post(get_BMS_url_info.appeal_judge_seller_win_url % repr(order_ID_NO))
    #print(r.text)
    return r.json()

if __name__ == '__main__':
    print(judgeBuyerWin(order_ID_NO='1536132964574021461'))
    print(judgeBuyerWin(order_ID_NO='1536132964574021461'))