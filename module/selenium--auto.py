# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023/8/18 15:17
# File : selenium--auto.py

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

# 浏览器进入百度网站
driver.get("https://www.baidu.com")

# 设置浏览器宽800，高400
driver.set_window_size(800, 400)


# 等待3秒
sleep(3)

# 刷新页面
driver.refresh()

# 等待3秒
sleep(3)

# 最大化窗口
driver.maximize_window()

# 退出浏览器
# driver.quit()

