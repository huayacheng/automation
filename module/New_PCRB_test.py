# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023/8/24 14:36
# File : New_PCRB.py
import time
from lib.common.BasePage import *
from element.webelement_po import element_position
from config.operation_url_config import read_write_setting
from selenium.webdriver.support.ui import Select
from lib.common.operate_excel import OperateExcel
from selenium.webdriver import ActionChains
import uiautomation as auto
from lib.common.BasePage import *
from element.webelement_po import element_position
from config.read_url_config import *
from selenium.webdriver.support.ui import Select
import uiautomation as auto
from selenium.webdriver import ActionChains
from lib.common.operate_excel import OperateExcel
import os
# edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32")
# print(edit)
#
# edit.SendKeys('D:\\autotest-pr\PERD\\filedata\\Mechanical BOM Templet_20210125.xls')
#
# current_path = os.path.abspath(os.path.dirname((os.getcwd())))
#
# print("当前路径为：", current_path)
# bill3_input_value1 = "template for packaging collection-PS8 2023-06-05.xlsx"
# file_path = os.path.join(current_path + "\\filedata", bill3_input_value1)
# print(file_path)

#
ele = element_position()
operate_excel = OperateExcel('../data/PERDFormat_PS8.xlsx','Section 1')
web = BasePage("../docker/chromedriver.exe")
web.open_web("https://cowork.lenovo.com/departments/quality/_layouts/15/FormServer.aspx?XmlLocation=https%3a//cowork.lenovo.com/departments/quality/Product%20Description%20%20Section%201/LOPT-2023-0216.xml&Source=https%3a//cowork.lenovo.com/departments/quality/PERD%20Records/Forms/Default%20View.aspx&DefaultItemOpen=1")

get_section1_txt = ele.get_emc_describe("Peripheral description")
get_section1_text = web.find_element(By.XPATH, get_section1_txt)
selection_text = operate_excel.get_text_cols_data(get_section1_text.text)
selection_value = operate_excel.get_value_cols_data(get_section1_text.text)
if selection_text in get_section1_text.text:
    section1_select = web.find_element(By.XPATH, ele.section1_select)

    Select(section1_select).select_by_visible_text(selection_value)

# operate_excel = OperateExcel('../data/PERDFormat_PS8.xlsx','Section 7')
# get_section2_txt = element_position.get_emc_describe(
#                 None,"Will Lenovo provide the vendor a manufacturing process developed by Lenovo?")

# bill_mate = element_position.get_emc_describe(None,
#     "Bill of Materials")
# bill_mate_el = web.driver.find_element(By.XPATH, bill_mate)
# bill_mate_text = operate_excel.get_text_cols_data(bill_mate_el.text)



# bill3_txt_4a = element_position.get_div_describe(None,
#                     "Are there any flame retardant plastic materials in the bill of material(s)?")
# bill3_text_4a = web.driver.find_element(By.XPATH, bill3_txt_4a)
# bill3_select_text4 = operate_excel.get_text_cols_data(bill3_text_4a.text)
# bill3_select_value4 = operate_excel.get_value_cols_data(bill3_text_4a.text)
# web.driver.execute_script("arguments[0].scrollIntoView();", bill3_text_4a)
# if bill3_select_text4 in bill3_text_4a.text:
#     section1_select = web.driver.find_element(By.XPATH, element_position.section3_select2_2a)
#
#     Select(section1_select).select_by_value(bill3_select_value4)
#     print("成功")

# eSIS_tracking.click()
# web.driver.implicitly_wait(10)
# # 选择文件
# xuan_file = web.find_element(By.XPATH, "//input[@id='FileAttachmentUpload']")
# # web.driver.execute_script("arguments[0].scrollIntoView();", xuan_file)
# # web.driver.execute_script("arguments[0].style.display = 'block';", xuan_file)
# ActionChains(web.driver).move_to_element(xuan_file).click().perform()
#
# #
# time.sleep(5)
# edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",ClassName="Edit")
# print(edit)
# edit.SendKeys('D:\\autotest-pr\PERD\\filedata\\template for packaging collection-PS8 2023-06-05.xlsx')
# # 点击打开按钮，确定选中的文件
# open_but = auto.ButtonControl(foundIndex=1,AutomationId="1",ClassName="Button").Click()
# # 附加按钮
# fujia_file = web.find_element(By.XPATH, "//input[@id='DialogButton0']")
# ActionChains(web.driver).move_to_element(fujia_file).click().perform()
#
# # win = web.driver.current_window_handle
# # print(win)
# # all_handles = web.driver.window_handles
# # web.driver.switch_to.window(all_handles[1])
# # # 刷新当前页面
#
# get_section1_txt = element_position.get_a_describe(None,"template for packaging collection-PS8 2023-06-05.xlsx")
# print(get_section1_txt)
# xuan_file = web.find_element(By.XPATH, get_section1_txt)
#
# get_section1_text = web.find(By.XPATH, get_section1_txt)
# print(get_section1_text)
# if get_section1_text:
#     print("上传成功拉！")
# else:
#     print("上传失败拉！")


# section1_status = web.driver.find_elements(By.XPATH,element_position.section1_status)[3]
# web.driver.execute_script("arguments[0].scrollIntoView();", section1_status)
# web.driver.find_element(By.XPATH,element_position.section1_click_but).click()
# # 刷新当前页面
# get_section1_txt = element_position.get_emc_describe(None,"Peripheral description")
# print(get_section1_txt)
# get_section1_text = web.find_element(By.XPATH, get_section1_txt)
# print(get_section1_text)
# web.driver.execute_script("arguments[0].scrollIntoView();", get_section1_text)
# print(get_section1_text.text)
# if get_section1_txt in get_section1_text.text:
#     section1_select = web.find_element(By.XPATH, element_position.section1_select)
#
#     Select(section1_select).select_by_value("selection_value")


