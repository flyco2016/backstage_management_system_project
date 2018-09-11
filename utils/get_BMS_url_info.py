from utils import myconfig

BMS_url_config = myconfig.MyConfigParser()


"""
用户中心url
"""
# 登录
BMS_login_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_user_center_url", 'BMS_login_url')
