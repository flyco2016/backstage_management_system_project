import requests
from BMS_login import BMSLogin
import time

def getRunningEatRobotList(user_name="admin", password='123456'):
    """
    函数功能：获取正在运行的吃单机器人
    """
    from utils import get_API_info, get_BMS_url_info

    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    jsonString = get_API_info.get_running_eat_robot_list
    data = dict(jsonString=jsonString)
    r = requests.post(get_BMS_url_info.get_eat_robot_list_url, data=data, cookies=login_cookies)
    if r.json()['msg'] == '操作完成':
        return r.json()['data']
    else:
        print(r.json()['msg'])


def getStopedEatRobotList(user_name="admin", password='123456'):
    """
    函数功能：获取停止的吃单机器人
    """
    from utils import get_API_info, get_BMS_url_info
    
    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    jsonString = get_API_info.get_stoped_eat_robot_list
    data = dict(jsonString=jsonString)
    r = requests.post(get_BMS_url_info.get_eat_robot_list_url, data=data, cookies=login_cookies)
    if r.json()['msg'] == '操作完成':
        return r.json()['data']
    else:
        print(r.json()['msg'])

def getEatRobotInfoWithCoin(user_name="admin", password='123456', coin='NZ'):
    """
    函数功能：获取某个币种的吃单机器人信息
    """
    from utils import get_API_info, get_BMS_url_info

    login_cookies = BMSLogin(user_name=user_name, password=password).cookies
    jsonString = get_API_info.get_eat_robot_info %(repr(coin))
    data = dict(jsonString=jsonString)
    r = requests.post(get_BMS_url_info.get_eat_robot_info_url, data=data, cookies=login_cookies)
    if r.json()['msg'] == '操作完成':
        return r.json()['data']
    else:
        print(r.json()['msg'])

def addNewEatRobot(user_name="admin", password='123456', 
coin='NZ', target_price=None, start_date=None, end_date=None):
    """
    函数功能：增加吃单机器人
    """
    from utils import get_API_info, get_BMS_url_info
    
    start_date_timestamp = time.mktime(time.strptime(str(start_date), "%Y-%m-%d %H:%M:%S"))
    end_date_timestamp = time.mktime(time.strptime(str(end_date), "%Y-%m-%d %H:%M:%S"))
    print(start_date_timestamp, end_date_timestamp, sep='\n')

    login_cookies = BMSLogin(user_name=user_name, password=password).cookies

    jsonString = get_API_info.add_new_eat_robot %(repr(coin), target_price, start_date_timestamp,
    end_date_timestamp)
    data = dict(jsonString=jsonString)

    r = requests.post(get_BMS_url_info.add_new_eat_robot_url, data=data, cookies=login_cookies)

    if r.json()['msg'] == '操作完成':
        print('')
    else:
        print(r.json()['msg'])

def modifyEatRobot(user_name="admin", password='123456', 
coin='NZ', target_price=None, start_date=None, end_date=None):
    """
    函数功能：修改吃单机器人
    """
    from utils import get_API_info, get_BMS_url_info
    
    start_date_timestamp = int(time.mktime(time.strptime(str(start_date), "%Y-%m-%d %H:%M:%S")))
    end_date_timestamp = int(time.mktime(time.strptime(str(end_date), "%Y-%m-%d %H:%M:%S")))
    print(start_date_timestamp, end_date_timestamp, sep='\n')

    login_cookies = BMSLogin(user_name=user_name, password=password).cookies

    jsonString = get_API_info.add_new_eat_robot %(repr(coin), target_price, start_date_timestamp,
    end_date_timestamp)
    data = dict(jsonString=jsonString)

    r = requests.post(get_BMS_url_info.add_new_eat_robot_url, data=data, cookies=login_cookies)

    if r.json()['msg'] == '操作完成':
        print(r.json()['data'])
    else:
        print(r.json()['msg'])

def modifyEatRobot(user_name="admin", password='123456', 
coin='NZ', target_price=None, start_date=None, end_date=None):
    """
    函数功能：修改吃单机器人
    """
    from utils import get_API_info, get_BMS_url_info
    
    start_date_timestamp = int(time.mktime(time.strptime(str(start_date), "%Y-%m-%d %H:%M:%S")))
    end_date_timestamp = int(time.mktime(time.strptime(str(end_date), "%Y-%m-%d %H:%M:%S")))
    print(start_date_timestamp, end_date_timestamp, sep='\n')

    login_cookies = BMSLogin(user_name=user_name, password=password).cookies

    jsonString = get_API_info.add_new_eat_robot %(repr(coin), target_price, start_date_timestamp,
    end_date_timestamp)
    data = dict(jsonString=jsonString)

    r = requests.post(get_BMS_url_info.add_new_eat_robot_url, data=data, cookies=login_cookies)

    if r.json()['msg'] == '操作完成':
        print(r.json()['data'])
    else:
        print(r.json()['msg'])






if __name__ == "__main__":
    #print(getRunningEatRobotList())
    #print(getStopedEatRobotList())
    #print(getEatRobotInfoWithCoin(coin='NZ'))
    addNewEatRobot(coin='', target_price=2, start_date='2018-09-26 00:00:00', end_date='2018-09-27 00:00:00')
    #modifyEatRobot()




    


