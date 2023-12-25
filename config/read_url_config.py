# coding:utf-8

import os
import configparser

# 读取DB配数据
# os.path.realpath(__file__)：返回当前文件的绝对路径
# os.path.dirname()： 返回（）所在目录

cur_path = os.path.dirname(os.path.realpath(__file__))
# print(cur_path)
configPath = os.path.join(cur_path, "url_config.ini")  # 路径拼接：/config/db_config.ini
# print(configPath)
# 实例化configparser 读取配置文件模块
conf = configparser.RawConfigParser()
conf.read(configPath, encoding="UTF-8")
# print(conf.sections())
# 读取配置PCRB url路径配置字段
hardware_url = conf.get("Hardware", "web_hardware")
emc_url = conf.get("EMC", "web_emc")
env_url = conf.get("ENV", "web_env")
homologation_url = conf.get("Homologation", "web_homologation")
perd_url = conf.get("PERD","web_perd")

print(perd_url)