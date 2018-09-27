from utils import myconfig

param_config = myconfig.MyConfigParser()

"""
后台管理---用户中心jsonstring
"""

"""
币币相关的业务
"""
# 获取执行中的吃单机器人列表
get_running_eat_robot_list = param_config.get_config_value("BMSAPIConfig", "BMS_C2C_exchange", 'get_running_eat_robot_list')
# 获取未执行的吃单机器人列表
get_stoped_eat_robot_list = param_config.get_config_value("BMSAPIConfig", "BMS_C2C_exchange", 'get_stoped_eat_robot_list')
# 获取未执行的吃单机器人列表
get_stoped_eat_robot_list = param_config.get_config_value("BMSAPIConfig", "BMS_C2C_exchange", 'get_stoped_eat_robot_list')
# 根据币种来获取吃单机器人信息
get_eat_robot_info = param_config.get_config_value("BMSAPIConfig", "BMS_C2C_exchange", 'get_eat_robot_info')
# 增加新的吃单机器人
add_new_eat_robot = param_config.get_config_value("BMSAPIConfig", "BMS_C2C_exchange", 'add_new_eat_robot')
# 修改吃单机器人
modify_eat_robot = param_config.get_config_value("BMSAPIConfig", "BMS_C2C_exchange", 'modify_eat_robot')
