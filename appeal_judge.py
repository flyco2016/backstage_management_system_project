import requests
from BMS_login import BMSLogin
from utils import get_API_info
from utils import get_BMS_url_info


def judgeBuyerWin(user_name="admin", password="123456", order_ID_NO=None):
    """
    函数功能：判定买家胜诉
    """
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    r = requests.post(get_BMS_url_info.appeal_judge_buyer_win_url %(order_ID_NO), cookies=login_cookies)
    print(r.json())

def judgeSellerWin(user_name="admin", password="123456", order_ID_NO=None):
    """
    函数功能：判定卖家胜诉
    """
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    r = requests.post(get_BMS_url_info.appeal_judge_seller_win_url %(order_ID_NO), cookies=login_cookies)
    print(r.json())

if __name__ == '__main__':
    #judgeBuyerWin(order_ID_NO='1537862519314819135')
    judgeSellerWin(order_ID_NO='1537874367604835126')