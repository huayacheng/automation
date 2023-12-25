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
web.open_web("https://cowork.lenovo.com/departments/quality/Lists/Import%20Attachments/Item/newifs.aspx?List=a72c1958%2Dd604%2D4da6%2Dbc00%2Da2b6054c65fe&Source=https://cowork.lenovo.com/departments/quality/Lists/Import%20Attachments/AllItems.aspx&RootFolder=&Web=a09bbe21%2D1eb2%2D4a63%2D9eb5%2Dd99b56aec218")


# attachments title
attachments_txt1 = ele.get_emc_describe(
    "Title")
attachments_text1 = web.find_element(By.XPATH, attachments_txt1)
attachments_radio1_text = operate_excel.get_text_cols_data(attachments_text1.text)
attachments_radio1_value = operate_excel.get_value_cols_data(attachments_text1.text)
if attachments_radio1_text in attachments_text1.text and attachments_radio1_value:
    web.find_element(By.XPATH, ele.section1_attachments_input_1a).send_keys(
        attachments_radio1_value)  # mm
# attachments Attachments
attachments_txt2 = ele.get_emc_describe(
    "Attachments")
attachments_text2 = web.find_element(By.XPATH, attachments_txt2)

attachments_radio2_text = operate_excel.get_text_cols_data(attachments_text2.text)
attachments_radio2_value = operate_excel.get_value_cols_data(attachments_text2.text)

# attachments_annex = ele.get_emc_describe(
#     "单击此处以附加文件")
#
# if attachments_radio2_text in attachments_text2.text and attachments_radio2_value:
#
#
#     # 点击选择文件按钮
#     section1_click_a1 = web.find_element(By.XPATH, attachments_annex)
#     section1_click_a1.click()
#
#     xuan_file2 = web.find_element(By.XPATH, ele.select_file)
#     ActionChains(web.driver).move_to_element(xuan_file2).click().perform()
#
#     time.sleep(5)
#     edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
#                             ClassName="Edit")
#     print(edit)
#     # 获取当前文件的根目录
#     current_path = os.path.abspath(os.path.dirname((os.getcwd())))
#     file_path = os.path.join(current_path + "\\filedata", attachments_radio2_value)
#     # 输入文件的路径加名称
#     edit.SendKeys(file_path)
#     # 点击打开按钮，确定选中的文件
#     auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
#     # 附加按钮
#     fujia_file = web.find_element(By.XPATH, "//input[@id='DialogButton0']")
#     ActionChains(web.driver).move_to_element(fujia_file).click().perform()
#
#     # 上传成功后验证是否成功
#     attachments_file = web.find_element(By.XPATH, ele.section1_spfa_text1)
#     if attachments_file.text.find(attachments_radio2_value) != -1:
#         print("上传成功了！")
#     else:
#         print("上传失败了")

# attachments Related - PERD
# attachments_txt3 = ele.get_emc_describe(
#     "Related - PERD")
# attachments_text3 = web.find_element(By.XPATH, attachments_txt3)
# attachments_radio3_text = operate_excel.get_text_cols_data(attachments_text3.text)
# attachments_radio3_value = operate_excel.get_value_cols_data(attachments_text3.text)
# if attachments_radio3_text in attachments_text3.text and attachments_radio3_value:
#     section2_select = web.find_element(By.XPATH,ele.section1_attachments_select_3a)
#     # section2_select.select_by_visible_text("FNOT-2023-0012")
#     Select(section2_select).select_by_visible_text(attachments_radio3_value)

# attachments Section Name
# attachments_txt4 = ele.get_emc_describe(
#     "Section Name")
# attachments_text4 = web.find_element(By.XPATH, attachments_txt4)
# attachments_radio4_text = operate_excel.get_text_cols_data(attachments_text4.text)
# attachments_radio4_value = operate_excel.get_value_cols_data(
#     attachments_text4.text)
# if attachments_radio4_text in attachments_text4.text and attachments_radio4_value:
#     section3_select = web.find_element(By.XPATH,
#                                            ele.section1_attachments_select_4a)
#
#     print(Select(section3_select).options)
#     Select(section3_select).select_by_value(attachments_radio4_value)



# Description
attachments_txt5 = ele.get_emc_describe(
    "Description")
attachments_text5 = web.find_element(By.XPATH, attachments_txt5)
attachments_radio5_text =operate_excel.get_text_cols_data(attachments_text5.text)
attachments_radio5_value = operate_excel.get_value_cols_data(
    attachments_text5.text)
if attachments_radio5_text in attachments_text5.text and attachments_radio5_value:
   description_txt = web.find_element(By.XPATH, ele.section1_attachments_input_5a)
   web.driver.execute_script("arguments[0].value = 'New text';", description_txt)

# 填写完成后点击提交按钮
web.find_element(By.XPATH, ele.section1_attachments_savebut).click()
# 提交完成后，关闭当前的标签页
web.driver.close()

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


