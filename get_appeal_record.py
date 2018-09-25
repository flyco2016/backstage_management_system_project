import requests
from BMS_login import BMSLogin
from utils import get_BMS_url_info


def getBuyerAppealInfo(user_name="admin", password="123456", order_ID_NO=None):
    """
    函数功能：获取买家申诉信息
    """
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies  # 需要增加cookies才能不被拦截
    r = requests.post(get_BMS_url_info.get_buyer_appeal_info_url %(order_ID_NO), cookies=login_cookies)
    return r.json()['data'][0]

def getSellerAppealInfo(user_name="admin", password="123456", order_ID_NO=None):
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    #payload = {'fiatDealTradeOrderId': order_ID_NO}
    r = requests.post(get_BMS_url_info.get_seller_appeal_info_url %(order_ID_NO), cookies=login_cookies)
    return r.json()['data'][0]

if __name__ == '__main__':
    getBuyerAppealInfo(order_ID_NO='1537862519314819135')
