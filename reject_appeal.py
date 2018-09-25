import requests
from BMS_login import BMSLogin
from get_appeal_record import getBuyerAppealInfo, getSellerAppealInfo
from utils import get_API_info
from utils import get_BMS_url_info


def rejectBuyerAppeal(user_name="admin", password="123456", order_ID_NO=None):
    """
    函数功能：驳回买家申诉
    """
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    buyer_lawsuit_record_Id = getBuyerAppealInfo(user_name=user_name, password=password, order_ID_NO=order_ID_NO)['lawsuitRecordId']
    r = requests.post(get_BMS_url_info.reject_judge_url %(buyer_lawsuit_record_Id), cookies=login_cookies)
    print(r.json())

def rejectSellerAppeal(user_name="admin", password="123456", order_ID_NO=None):
    """
    函数功能：驳回卖家申诉
    """
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    seller_lawsuit_record_Id = getSellerAppealInfo(user_name=user_name, password=password, order_ID_NO=order_ID_NO)['lawsuitRecordId']
    r = requests.post(get_BMS_url_info.reject_judge_url %(seller_lawsuit_record_Id), cookies=login_cookies)
    print(r.json())

if __name__ == '__main__':
    rejectBuyerAppeal(order_ID_NO='1537862519314819135')
    rejectSellerAppeal(order_ID_NO='1537862519314819135')