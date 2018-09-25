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

