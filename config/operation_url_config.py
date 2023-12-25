# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2022/12/22 15:03
import configparser
import os

class read_write_setting:

    def __init__(self):
        cur_path = os.path.dirname(os.path.realpath(__file__))
        self.configpath = os.path.join(cur_path,"url_config.ini") # 路径拼接：/config/sttings_config.ini
        # 实例化configparser 读取配置文件模块
        self.conf = configparser.RawConfigParser()
        self.conf.read(self.configpath,encoding="UTF-8")
        self.configure = "PERD"
        self.App = "web_perd"

        self.read_setting()

    def read_setting(self):
        # 读取配置Softwareconf配置字段
        self.web_url = self.conf.get(self.configure,self.App)
        print(self.web_url)


        # print(self.software_name,self.software_exe,self.software_path)
    def write_set_url(self,value):
        # 修改执行软件的名字
        self.conf.set(self.configure,self.App,value)
        self.conf.write(open(self.configpath, "w"))
        print(f"更新:{self.configure}的URL:{self.App}的路径为：{value}")
    #
    # def write_setting_exe(self,value):
    #     # 修改执行软件的可执行
    #     self.conf.set(self.configure, self.programexe, value)
    #     self.conf.write(open(self.configpath, "w"))
    #     print(f"8、设置setion:{self.configure}下的option:{self.programexe}的值为：{value}")
    #
    # def write_software_path(self,value):
    #     # 修改执行软件的可执行
    #     self.conf.set(self.configure, self.program_path, value)
    #     self.conf.write(open(self.configpath, "w"))
    #     print(f"9、设置setion:{self.configure}下的option:{self.programexe}的值为：{value}")

if __name__ == '__main__':
    read = read_write_setting()
    # if read.software_exe in read.software_path and "exe" in read.software_path:
    #     print(read.software_path)
    # read.write_software_path("111111111111111111111111")
    # read.write_setting_exe("LenovoGoCentralUI.exe")