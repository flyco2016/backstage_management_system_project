from utils import myconfig

param_config = myconfig.MyConfigParser()

"""
后台管理---用户中心jsonstring
"""
# 登录
BMS_login_data = param_config.get_config_value("BMSAPIConfig", "BMS_user_center", 'BMS_login_data')
