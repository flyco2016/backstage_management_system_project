from utils import myconfig

BMS_url_config = myconfig.MyConfigParser()


"""
用户中心url
"""
# 登录
BMS_login_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_user_center_url", 'BMS_login_url')

"""
后台法币业务相关的
"""
# 获取买家申诉信息
get_buyer_appeal_info_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_curb_exchange_url", 'get_buyer_appeal_info_url')
# 获取卖家申诉信息
get_seller_appeal_info_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_curb_exchange_url", 'get_seller_appeal_info_url')
# 驳回申诉
reject_judge_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_curb_exchange_url", 'reject_judge_url')
# 判定卖家胜诉
appeal_judge_seller_win_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_curb_exchange_url", 'appeal_judge_seller_win_url')
# 判定买家胜诉
appeal_judge_buyer_win_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_curb_exchange_url", 'appeal_judge_buyer_win_url')

"""
后台币币相关业务
"""
# 获取吃单机器人列表
get_eat_robot_list_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_C2C_exchange_url", 'get_eat_robot_list_url')
# 根据币种获取吃单机器人
get_eat_robot_info_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_C2C_exchange_url", 'get_eat_robot_info_url')
# 增加新的吃单机器人
add_new_eat_robot_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_C2C_exchange_url", 'add_new_eat_robot_url')
# 修改吃单机器人
modify_eat_robot_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_C2C_exchange_url", 'modify_eat_robot_url')
# 删除吃单机器人
delete_eat_robot_url = BMS_url_config.get_config_value("BMSurlconfig", "BMS_C2C_exchange_url", 'delete_eat_robot_url')
