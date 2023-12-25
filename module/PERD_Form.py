# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023/8/30 10:46
# File : PERD_Form.py
import time

from lib.common.BasePage import *
from element.webelement_po import element_position
from config.operation_url_config import read_write_setting
from selenium.webdriver.support.select import Select
from lib.common.operate_excel import OperateExcel
from selenium.webdriver import ActionChains
import uiautomation as auto
import os
import sys
class PERD():

    def __init__(self,file_path,packaging_path,web_url):
        if getattr(sys, 'frozen', False):
            self.application_path = os.path.dirname(sys.executable)  # 打包EXE后的运行路径
            print("打包之后的application_path",self.application_path)
        elif __file__:
            # self.application_path = os.path.abspath(os.path.dirname(os.path.dirname(os.getcwd()))) # 未打包时的运行路径 获取到template
            self.application_path = os.path.abspath(os.path.dirname(os.getcwd()))  # 未打包时的运行路径 获取到template  代码调试路径
            print("self.application_path:未打包路径1",self.application_path)
        # 浏览器DW路径
        browser_path = os.path.join(self.application_path + "\\docker", "chromedriver.exe")
        self.web = BasePage(browser_path)
        print(self.web)
        # self.web = BasePage("..//docker/chromedriver.exe")
        # print(self.web)
        self.ele = element_position()
        self.read_conf = read_write_setting()
        self.file_path = file_path
        self.packaging_path = packaging_path
        # 启动浏览器
        self.web.open_web(web_url)
        self.results = bool
        self.end = bool
        self.current = ''
        self.cases_end = bool
        pass

    def updata_file(self,element_text,element_but):

        element_txt = self.ele.get_emc_describe(element_text)
        get_element_text = self.web.find_element(By.XPATH, element_txt)

        get_data_text = self.operate_excel.get_text_cols_data(get_element_text.text)
        get_data_value = self.operate_excel.get_value_cols_data(get_element_text.text)
        if element_text in get_data_text and get_data_value:
            # 点击附件文件按钮
            element_click_but = self.web.find_element(By.XPATH, element_but)
            element_click_but.click()

            xuan_file2 = self.web.find_element(By.XPATH, self.ele.select_file)
            ActionChains(self.web.driver).move_to_element(xuan_file2).click().perform()

            time.sleep(5)
            edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32", ClassName="Edit")
            print(edit)
            # 获取当前文件的根目录
            file_path = os.path.join(self.application_path + "\\filedata", get_data_value)
            # 输入文件的路径加名称
            edit.SendKeys(file_path)
            # 点击打开按钮，确定选中的文件
            auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
            # 附加按钮
            fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
            ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()
            print(self.web.find_element(By.XPATH, element_but).text)
            # 上传成功后验证是否成功
            if self.web.find_element(By.XPATH, element_but).text.find(get_data_value) != -1:
                print("上传成功了！")
            else:
                print("上传失败了")
    def updata_div_file(self,element_text,element_but):

        element_txt = self.ele.get_div_describe(element_text)
        get_element_text = self.web.find_element(By.XPATH, element_txt)

        get_data_text = self.operate_excel.get_text_cols_data(get_element_text.text)
        get_data_value = self.operate_excel.get_value_cols_data(get_element_text.text)
        if element_text in get_data_text and get_data_value:
            # 点击附件文件按钮
            element_click_but = self.web.find_element(By.XPATH, element_but)
            element_click_but.click()

            xuan_file2 = self.web.find_element(By.XPATH, self.ele.select_file)
            ActionChains(self.web.driver).move_to_element(xuan_file2).click().perform()

            time.sleep(5)
            edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32", ClassName="Edit")
            print(edit)
            # 获取当前文件的根目录
            current_path = os.path.abspath(os.path.dirname((os.getcwd())))
            file_path = os.path.join(self.application_path + "\\filedata", get_data_value)
            # 输入文件的路径加名称
            edit.SendKeys(file_path)
            # 点击打开按钮，确定选中的文件
            auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
            # 附加按钮
            fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
            ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()
            print(self.web.find_element(By.XPATH, element_but).text)
            # 上传成功后验证是否成功
            if self.web.find_element(By.XPATH, element_but).text.find(get_data_value) != -1:
                print("上传成功了！")
            else:
                print("上传失败了")

    def updata_li_file(self,element_text,element_but):

        element_txt = self.ele.get_li_describe(element_text)
        get_element_text = self.web.find_element(By.XPATH, element_txt)

        get_data_text = self.operate_excel.get_text_cols_data(element_text)
        get_data_value = self.operate_excel.get_value_cols_data(element_text)
        if get_data_value:
            # 点击附件文件按钮
            element_click_but = self.web.find_element(By.XPATH, element_but)
            element_click_but.click()

            xuan_file2 = self.web.find_element(By.XPATH, self.ele.select_file)
            ActionChains(self.web.driver).move_to_element(xuan_file2).click().perform()

            time.sleep(5)
            edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32", ClassName="Edit")
            print(edit)
            # 获取当前文件的根目录
            current_path = os.path.abspath(os.path.dirname((os.getcwd())))
            file_path = os.path.join(self.application_path + "\\filedata", get_data_value)
            # 输入文件的路径加名称
            edit.SendKeys(file_path)
            # 点击打开按钮，确定选中的文件
            auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
            # 附加按钮
            fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
            ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()
            print(self.web.find_element(By.XPATH, element_but).text)
            # 上传成功后验证是否成功
            if self.web.find_element(By.XPATH, element_but).text.find(get_data_value) != -1:
                print("上传成功了！")
            else:
                print("上传失败了")



    def section_input(self,txt_input,ele_input):
        # 输入文本 1.input
        txt_input = self.ele.get_emc_describe(txt_input)
        text_input = self.web.find_element(By.XPATH, txt_input)
        input_text_cols = self.operate_excel.get_text_cols_data(text_input.text)
        input_text_cols_value = self.operate_excel.get_value_cols_data(text_input.text)
        if input_text_cols_value:
            self.web.find_element(By.XPATH, ele_input).click()
            self.web.find_element(By.XPATH, ele_input).send_keys(input_text_cols_value)  # w

    def section_input_num(self,txt_input,ele_input,ele_num):
        # 输入文本 1.input
        txt_input = self.ele.get_emc_describe(txt_input)
        text_input = self.web.find_element(By.XPATH, txt_input)
        input_text_cols = self.operate_excel.get_text_cols_data(text_input.text)
        input_text_cols_value = self.operate_excel.get_cols_data(text_input.text)[ele_num]
        if input_text_cols_value:
            self.web.find_element(By.XPATH, ele_input).click()
            self.web.find_element(By.XPATH, ele_input).send_keys(input_text_cols_value)  # w

    def section_input_text(self,txt_input,ele_input):
        # 输入文本 1.input
        input_text_cols = self.operate_excel.get_text_cols_data(txt_input)
        input_text_cols_value = self.operate_excel.get_value_cols_data(txt_input)
        if input_text_cols and input_text_cols_value:
            self.web.find_element(By.XPATH, ele_input).click()
            self.web.find_element(By.XPATH, ele_input).send_keys(input_text_cols_value)  # w

    def section_dev_input(self,txt_input,ele_input):
        # 输入文本 1.input
        txt_input = self.ele.get_div_describe(txt_input)
        text_input = self.web.find_element(By.XPATH, txt_input)
        input_text_cols = self.operate_excel.get_text_cols_data(text_input.text)
        input_text_cols_value = self.operate_excel.get_value_cols_data(text_input.text)
        if input_text_cols_value:
            self.web.find_element(By.XPATH, ele_input).click()
            self.web.find_element(By.XPATH, ele_input).send_keys(input_text_cols_value)  # w

    def section_input_list(self,txt_input,ele_input,lis):
        # 输入文本 1.input
        # txt_input = self.ele.get_emc_describe(txt_input)
        # text_input = self.web.find_element(By.XPATH, txt_input)
        # input_text_cols = self.operate_excel.get_text_cols_data(text_input.text)
        print("txt_input::::",txt_input)
        input_text_cols_value = self.operate_excel.get_value_cols_list(txt_input)
        if input_text_cols_value:
            self.web.find_element(By.XPATH, ele_input).click()
            self.web.find_element(By.XPATH, ele_input).send_keys(input_text_cols_value[lis])  # w

    def section_lists(self,txt_input,ele_input,lis):
        # 输入文本 1.input
        # txt_input = self.ele.get_emc_describe(txt_input)
        # text_input = self.web.find_element(By.XPATH, txt_input)
        # input_text_cols = self.operate_excel.get_text_cols_data(text_input.text)
        print("txt_input::::",txt_input)
        input_text_cols_value = self.operate_excel.get_value_cols_data(txt_input)
        input_value_list = input_text_cols_value.split(',')
        if input_text_cols_value:
            self.web.find_element(By.XPATH, ele_input).click()
            self.web.find_element(By.XPATH, ele_input).send_keys(input_value_list[lis])  # w

    def section_select(self,txt_select,ele_select):
        select_txt = self.ele.get_div_describe(txt_select)
        select_text = self.web.find_element(By.XPATH, select_txt)
        select_cols_text = self.operate_excel.get_text_cols_data(select_text.text)
        select_cols_value = self.operate_excel.get_value_cols_data(select_text.text)
        if select_cols_value:
            # 下拉选择项目
            self.web.find_element(By.XPATH, ele_select).click()
            select_text.click()
            section1_select = self.web.find_element(By.XPATH, ele_select)

            Select(section1_select).select_by_visible_text(select_cols_value)

    def section_span_select(self,txt_select,ele_select):
        select_txt = self.ele.get_emc_describe(txt_select)
        select_text = self.web.find_element(By.XPATH, select_txt)
        select_cols_text = self.operate_excel.get_text_cols_data(select_text.text)
        select_cols_value = self.operate_excel.get_value_cols_data(select_text.text)
        if select_cols_value:
            # 下拉选择项目
            self.web.find_element(By.XPATH, ele_select).click()
            select_text.click()
            section1_select = self.web.find_element(By.XPATH, ele_select)

            Select(section1_select).select_by_visible_text(select_cols_value)

    def test_section(self):
        # 读取excel文档，根据选中的section3，读取section3内容
        self.operate_excel = OperateExcel('../data/PERDFormat_PS8.xlsx', 'Section 3')
        # self.operate_excel.get_sheet("Section 3")
        # 启动浏览器
        self.web.open_web(self.read_conf.web_url)
        # 检查项目的section3状态
        section3_status = self.web.driver.find_elements(By.XPATH, self.ele.section3_status)[3]
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section3_status)
        if section3_status != "Section Owner":
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section2执行用例
            self.web.driver.find_element(By.XPATH, self.ele.section3_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 3.1 Bill of Materials
            bill_mate = self.ele.get_emc_describe(
                "Bill of Materials")
            bill_mate_el = self.web.find_element(By.XPATH, bill_mate)
            bill_mate_text = self.operate_excel.get_text_cols_data(bill_mate_el.text)
            print(bill_mate_el.text)
            print(bill_mate_text)
            if bill_mate_text in bill_mate_el.text:
                # 3.1.1
                bill_txt_1a = self.ele.get_emc_describe(
                    "Does this product contain part assemblies that have their own PERD documents?")
                bill_text_1a = self.web.find_element(By.XPATH, bill_txt_1a)
                bill_select_text1 = self.operate_excel.get_text_cols_data(bill_text_1a.text)
                bill_select_value1 = self.operate_excel.get_value_cols_data(bill_text_1a.text)
                self.web.driver.execute_script("arguments[0].scrollIntoView();", bill_text_1a)
                print("bill_select_text1:",bill_select_text1)
                print("bill_text_1a:", bill_text_1a.text)
                if bill_select_value1:

                    if "Yes" in bill_select_value1:
                        # 下拉选择项目

                        self.web.find_element(By.XPATH, self.ele.section3_select_1a).click()
                        bill_text_1a.click()
                        section1_select = self.web.find_element(By.XPATH, self.ele.section3_select_1a)
                        Select(section1_select).select_by_visible_text(bill_select_value1)
                        # 出现隐藏的输入框 3
                        self.section_input("Please list the relevant component PERD reference(s)",
                                           self.ele.section3_input_1a)
                        # Comments
                        self.section_dev_input("Comments", self.ele.section3_input_2a)
                    else:
                        # 下拉选择项目
                        self.web.find_element(By.XPATH, self.ele.section3_select_1a).click()
                        bill_text_1a.click()
                        section1_select = self.web.find_element(By.XPATH, self.ele.section3_select_1a)
                        Select(section1_select).select_by_value(bill_select_value1)

    # def packaging_record(self):
    #
    #     # 读取excel文档，根据选中的section4，读取section4内容
    #     self.operate_excel = OperateExcel(self.packaging_path, '1200x1000mm栈板')
    #     # self.operate_excel.get_sheet("Section 4")
    #     # 启动浏览器
    #     self.web.open_web("https://cowork.lenovo.com/departments/quality/Lists/Geo%20Packaging/Item/displayifs.aspx?ID=8206&Source=https://cowork.lenovo.com/departments/quality/SitePages/Packaging%20Data.aspx")
    #
    #     #
    #     # Geo Packaging Record
    #     self.web.driver.implicitly_wait(10)
    #     # 进入编辑模式
    #     self.web.driver.find_element(By.XPATH, self.ele.section4_click_but).click()
    #     self.web.driver.implicitly_wait(5)
    #     # 切换到最后一个标签页刷新界面
    #     win = self.web.driver.current_window_handle
    #     print(win)
    #     all_handles = self.web.driver.window_handles
    #     self.web.driver.switch_to.window(all_handles[-1])
    #     # 刷新当前页面
    #     self.web.driver.refresh()


    def section4_packaging(self,sheet_name,opution):
        # 读取excel文档，根据选中的section4，读取section4内容
        self.operate_excel = OperateExcel(self.packaging_path, sheet_name)
        # 启动浏览器
        # self.web.open_web(
        #     "https://cowork.lenovo.com/departments/quality/Lists/Geo%20Packaging/Item/displayifs.aspx?ID=8363&Source=https://cowork.lenovo.com/departments/quality/SitePages/Packaging%20Data.aspx")

        # Geo Packaging Record
        self.web.driver.implicitly_wait(10)
        # 切换到最后一个标签页刷新界面
        win = self.web.driver.current_window_handle
        print(win)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 刷新当前页面
        self.web.driver.refresh()
        # 进入编辑模式
        self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
        self.web.driver.implicitly_wait(5)


        # 填写，Overall size of sales packaging
        # 填写 Overall size of sales package Width (mm)
        section4_width_txt = "Width (mm)"
        section4_width_text = self.operate_excel.get_text_cols_data(section4_width_txt)
        section4_width_value = self.operate_excel.get_value_cols_data(section4_width_txt)
        if section4_width_text and section4_width_value:
            section1_input_general_1a = self.web.find_element(By.XPATH, self.ele.section4_packaging_input_1a)
            section1_input_general_1a.clear()
            section1_input_general_1a.send_keys(section4_width_value)  # mm
        # Height (mm)
        section4_Height_txt = "Height (mm)"
        section4_Height_text = self.operate_excel.get_text_cols_data(section4_Height_txt)
        section4_Height_value = self.operate_excel.get_value_cols_data(section4_Height_txt)
        if section4_Height_text and section4_Height_value:
            section1_input_general_1a = self.web.find_element(By.XPATH, self.ele.section4_packaging_input_2a)
            section1_input_general_1a.clear()
            section1_input_general_1a.send_keys(section4_Height_value)  # mm

        # Length (mm)
        section4_Length_txt = "Length (mm)"
        section4_Length_text = self.operate_excel.get_text_cols_data(section4_Length_txt)
        section4_Length_value = self.operate_excel.get_value_cols_data(section4_Length_txt)
        if section4_Length_text and section4_Length_value:
            section1_input_general_1a = self.web.find_element(By.XPATH, self.ele.section4_packaging_input_3a)
            section1_input_general_1a.clear()
            section1_input_general_1a.send_keys(section4_Length_value)  # mm

        # 填写 How many units per pallet
        section4_pallet_txt = "Total Units on Pallet"
        section4_pallet_text1 = self.operate_excel.get_text_cols_data(section4_pallet_txt)
        section4_pallet_value1 = self.operate_excel.get_value_cols_data(section4_pallet_txt)
        if section4_pallet_text1 and section4_pallet_value1:
            section1_input_general_1a = self.web.find_element(By.XPATH, self.ele.section4_packaging_input_4a)
            section1_input_general_1a.clear()
            section1_input_general_1a.send_keys(section4_pallet_value1)  # mm
        # 填写 How many units per pallet
        section4_pallet_txt2 = "Units per Repack"
        section4_pallet_text2 = self.operate_excel.get_text_cols_data(section4_pallet_txt2)
        section4_pallet_value2 = self.operate_excel.get_value_cols_data(section4_pallet_txt2)
        if section4_pallet_text2 and section4_pallet_value2:
            section1_input_general_1a = self.web.find_element(By.XPATH, self.ele.section4_packaging_input_5a)
            section1_input_general_1a.clear()
            section1_input_general_1a.send_keys(section4_pallet_value2)  # mm



        # 填写完成后，新建 Create Packaging Detail
        packaging_type = 'Sales'
        # 获取sales 的个数，从而创建多少次，Packaging
        packaging_sales_list = self.operate_excel.get_sales_component("Component")

        if self.web.find(By.XPATH,self.ele.section4_sales_input_a) != True:
            # 点击创建
            print("创建第一个")
            time.sleep(5)
            self.web.find_element(By.XPATH, self.ele.section4_create_input_but).click()
            time.sleep(10)
            self.web.driver.close()
            time.sleep(10)
            # 切换到最后一个标签页刷新界面
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 重新进入Geo Packaging Record
            self.web.find_element(By.XPATH, opution).click()
            # 点击编辑，再点击刷新
            self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
            self.web.find_element(By.XPATH, self.ele.section4_refresh_input_but).click()
            # 进入编辑模式
            self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
            self.web.driver.implicitly_wait(5)
        else:
            pass

        all_sales_element = []
        for i in range((len(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)))):
            if self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[i].text != '':
                all_sales_element.append(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[i])
        print("all_sales_element::",all_sales_element)
        for i in range(len(packaging_sales_list)):
            print(i)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # print(all_sales_element[i].text)
            try:
                if all_sales_element[i] and all_sales_element[i].text == "Click to view":

                    print("当前已经创建过，直接点击进入")
                    # 点击进入Click to view
                    all_sales_element[i].click()
            except IndexError:
                # 点击创建
                print("创建一个")
                time.sleep(5)
                self.web.find_element(By.XPATH, self.ele.section4_create_input_but).click()
                time.sleep(5)
                self.web.driver.close()
                time.sleep(10)
                # 切换到最后一个标签页刷新界面
                all_handles = self.web.driver.window_handles
                self.web.driver.switch_to.window(all_handles[-1])
                # 刷新当前页面
                self.web.driver.refresh()

                # 重新进入Geo Packaging Record
                self.web.find_element(By.XPATH, opution).click()
                # 点击编辑，再点击刷新
                print("再次进入包装页，进行编辑")
                all_handles = self.web.driver.window_handles
                self.web.driver.switch_to.window(all_handles[-1])
                # 刷新当前页面
                self.web.driver.refresh()
                self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
                self.web.find_element(By.XPATH, self.ele.section4_refresh_input_but).click()
                time.sleep(5)
                # all_sales_element  更新加入新创建的“Click to view”
                all_sales_element = []
                for j in range((len(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)))):
                    if self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[j].text != '':
                        print(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[j].text)
                        all_sales_element.append(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[j])
                # 进入编辑模式
                print("all_sales_element",all_sales_element)

                # 点击进入Click to view
                print(all_sales_element[-1].text)
                all_sales_element[-1].click()

            # 点击进入Click to view

            # 进入新的页面编辑内容，编辑完成后退出
            # 获取当前数据文件一行的数据
            get_row_data = self.operate_excel.get_cols_data(packaging_sales_list[i])
            print(get_row_data)
            time.sleep(5)
            # all_handles = self.web.driver.window_handles
            # self.web.driver.switch_to.window(all_handles[-1])
            # self.web.driver.close()
            self.packaging_record(get_row_data,packaging_type)



        # 切换到最后一个标签页刷新界面
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 刷新当前页面
        self.web.driver.refresh()

        # 填写完成后，新建 Create Packaging Detail
        packaging_type_2 = 'Transport'
        # 获取sales 的个数，从而创建多少次，Packaging
        packaging_Transport_list = self.operate_excel.get_transport_component("Component")
        # 点击第六个试试
        all_tran_element = []
        # print(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a))
        for i in range((len(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)))):
            print(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[i].text)
            if self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[i].text != '':
                all_tran_element.append(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[i])

        print("all_tran_element::::",all_tran_element)
        # all_element[6].click()
        # self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[5].click()
        # 遍历数据条数，创建并输入数据
        for i in range(len(packaging_Transport_list)):
            print(i)
            # 切掉前5个
            des_all_element=all_tran_element[len(packaging_sales_list):]
            print("des_all_element___-1:",des_all_element)
            des_all_element = des_all_element[::-1]
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            try:
                if des_all_element[i] and des_all_element[i].text == "Click to view":


                    print("已创建，并存在，不用创建，直接进入")
                    # 点击进入Click to view
                    #
                    des_all_element[i].click()
                    pass

            except IndexError:
                # 点击创建
                print("创建一个")
                time.sleep(5)
                self.web.find_element(By.XPATH, self.ele.section4_create_input_but).click()
                time.sleep(5)
                self.web.driver.close()
                time.sleep(10)
                # 切换到最后一个标签页刷新界面
                all_handles = self.web.driver.window_handles
                self.web.driver.switch_to.window(all_handles[-1])
                # 刷新当前页面
                self.web.driver.refresh()

                # 重新进入Geo Packaging Record
                self.web.find_element(By.XPATH,opution).click()
                # 点击编辑，再点击刷新
                print("再次进入包装页，进行编辑")
                all_handles = self.web.driver.window_handles
                self.web.driver.switch_to.window(all_handles[-1])
                # 刷新当前页面
                self.web.driver.refresh()
                self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
                self.web.find_element(By.XPATH, self.ele.section4_refresh_input_but).click()
                time.sleep(5)
                # all_sales_element  更新加入新创建的“Click to view”
                all_tran_element = []
                for j in range((len(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)))):

                    if self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[j].text != '':
                        print(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[j].text)
                        all_tran_element.append(self.web.find_elements(By.XPATH, self.ele.section4_sales_input_a)[j])
                print("all_tran_element::",all_tran_element)
                # 进入编辑模式
                # self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
                time.sleep(5)
                print(len(packaging_sales_list))
                print(all_tran_element[len(packaging_sales_list)].text)
                all_tran_element[len(packaging_sales_list)].click()
                print("一点击")




            # 进入新的页面编辑内容，编辑完成后退出
            # 获取当前数据文件一行的数据
            get_row_data = []
            for li in packaging_sales_list:
                if packaging_Transport_list[i] == li:
                    get_row_data = self.operate_excel.get_cols_data(packaging_Transport_list[i],1)
                    break
                else:
                    get_row_data = self.operate_excel.get_cols_data(packaging_Transport_list[i])
            print(get_row_data)
            time.sleep(15)

            # all_handles = self.web.driver.window_handles
            # self.web.driver.switch_to.window(all_handles[-1])
            # self.web.driver.close()

            self.packaging_record(get_row_data, packaging_type_2)
        # 切换到最后一个标签页刷新界面
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 刷新当前页面
        self.web.driver.refresh()

        # 数据表填写完成后，提交
        # 当填写完成时，提交并退出
        if self.web.find_element(By.XPATH, self.ele.packaging_submit_but):
            # 填写完后，点击提交按钮
            self.web.find_element(By.XPATH, self.ele.packaging_submit_but).click()
            time.sleep(5)
            print("页面表格填写完成，提交！")
            self.web.driver.implicitly_wait(10)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            self.web.driver.close()


    def packaging_record(self,row_data,type):
        # 当进入新页面时，刷新该页面
        # 切换到最后一个标签页刷新界面

        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 刷新当前页面
        self.web.driver.refresh()

        # 优先判断是否已经有输入
        # print("self.web.find_element(By.XPATH, self.ele.packaging_record_input_2a).text:",self.web.find_element(By.XPATH, self.ele.packaging_record_input_2a).get_attribute("value"))
        if self.web.find_element(By.XPATH, self.ele.packaging_record_input_2a).get_attribute("value") == '' \
                or self.web.find_element(By.XPATH, self.ele.packaging_record_input_select_2a).get_attribute("value") != row_data[1]:
            print("进行编辑")
            # 进入编辑
            self.web.find_element(By.XPATH, self.ele.section4_packaging_edit).click()
            # 编辑 Select Packaging Type
            Record_txt_radio1 = self.ele.get_emc_describe(
                "Select Packaging Type")
            Record_text_radio1 = self.web.find_element(By.XPATH, Record_txt_radio1)
            # 获取一行的数据
            if Record_text_radio1:
                self.web.find_element(By.XPATH, self.ele.packaging_record_select_1a).click()
                Record_text_radio1.click()
                section_select = self.web.find_element(By.XPATH, self.ele.packaging_record_select_1a)

                self.select_option_whitespace(Select(section_select), type)

            # 编辑 Select Form
            Record_txt_radio2 = self.ele.get_emc_describe(
                "Select Form")
            Record_text_radio2 = self.web.find_element(By.XPATH, Record_txt_radio2)
            # 获取一行的数据
            if Record_text_radio2:
                self.web.find_element(By.XPATH, self.ele.packaging_record_select_2a).click()
                Record_text_radio2.click()
                section1_select = self.web.find_element(By.XPATH, self.ele.packaging_record_select_2a)

                # Select(section1_select).select_by_visible_text(row_data[1])
                if row_data[1] == "Pallet":
                    row_data[1] = "Palette"
                self.select_option_whitespace(Select(section1_select),row_data[1])

            # 编辑 Select Material
            Record_txt_radio3 = self.ele.get_emc_describe(
                "Select Material")
            Record_text_radio3 = self.web.find_element(By.XPATH, Record_txt_radio3)
            # 获取一行的数据
            if Record_text_radio3:
                self.web.find_element(By.XPATH, self.ele.packaging_record_select_3a).click()
                Record_text_radio3.click()
                section2_select = self.web.find_element(By.XPATH, self.ele.packaging_record_select_3a)

                # Select(section2_select).select_by_visible_text(row_data[2])
                self.select_option_whitespace(Select(section2_select), row_data[2])

            # 编辑 Enter % of Post Consumer Content (PCC)
            Record_txt_radio5 = self.ele.get_emc_describe(
                "Post Consumer Content (PCC)")
            Record_text_radio5 = self.web.find_element(By.XPATH, Record_txt_radio5)
            # 获取一行的数据
            if Record_text_radio5:
                Record_text_radio4_input = self.web.find_element(By.XPATH, self.ele.packaging_record_input_1a)
                Record_text_radio4_input.clear()
                Record_text_radio4_input.send_keys(row_data[4])  # mm

            # 编辑 nter Weight (g)
            Record_txt_radio4 = self.ele.get_emc_describe(
                "Enter Weight (g)")
            Record_text_radio4 = self.web.find_element(By.XPATH, Record_txt_radio4)
            # 获取一行的数据
            if Record_text_radio4:
                Record_text_radio4_input = self.web.find_element(By.XPATH, self.ele.packaging_record_input_2a)
                Record_text_radio4_input.clear()
                Record_text_radio4_input.send_keys(row_data[3])  # mm

            # 当填写完成时，提交并退出
            if self.web.find_element(By.XPATH, self.ele.packaging_Record_save_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.packaging_Record_save_but).click()
                time.sleep(10)
                print("填写完成，保存提交！")
                self.web.driver.implicitly_wait(10)
                win = self.web.driver.current_window_handle
                print(win)
                all_handles = self.web.driver.window_handles
                self.web.driver.switch_to.window(all_handles[-1])
                self.web.driver.close()

        else:
            print("已经添加过了")
            self.web.driver.implicitly_wait(10)

            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            self.web.driver.close()



    #
    def select_option_whitespace(self,select_element, text):
        options = [option.text.lower().replace(" ", "") for option in select_element.options]
        # print(options)
        text = text.lower().replace(" ", "")
        # print(text)

        for option in select_element.options:
            # print(option)
            if option.text.lower().replace(" ", "") == text:
                option.click()
                break

    def perd_section1(self):
        # 读取excel文档，根据选中的section1，读取section1内容
        self.operate_excel = OperateExcel(self.file_path,'Section 1')

        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section1状态
        time.sleep(10)
        section1_status = self.web.driver.find_element(By.XPATH,self.ele.setion1_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section1_status)

        print("section1:当前状态",section1_status.get_attribute("value"))
        time.sleep(5)
        if section1_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section1_status.get_attribute("value"):

            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section1执行用例
            self.web.driver.find_element(By.XPATH,self.ele.section1_click_but).click()
            self.web.driver.implicitly_wait(15)
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            print(all_handles)
            for i in all_handles:
                if i != win:
                    self.web.driver.switch_to.window(i)
                    # 刷新当前页面
                    self.web.driver.refresh()
            # 1.1 Product Description
            get_section1_txt = self.ele.get_emc_describe("Peripheral description")
            get_section1_text = self.web.find_element(By.XPATH, get_section1_txt)
            selection_text = self.operate_excel.get_text_cols_data(get_section1_text.text)
            selection_value = self.operate_excel.get_value_cols_data(get_section1_text.text)
            if selection_text in get_section1_text.text and selection_value:
                self.web.find_element(By.XPATH, self.ele.section1_select).click()
                get_section1_text.click()
                section1_select = self.web.find_element(By.XPATH, self.ele.section1_select)

                Select(section1_select).select_by_value(selection_value)
            # 1.2 Additional Product Description
            get_section2_txt = self.ele.get_emc_describe(
                "Is there additional product description or application to be entered.")
            get_section2_text = self.web.find_element(By.XPATH, get_section2_txt)
            selection2_text = self.operate_excel.get_text_cols_data(get_section2_text.text)
            selection2_value = self.operate_excel.get_value_cols_data(get_section2_text.text)
            if selection2_text in get_section2_text.text:
                if selection2_value == "Yes" or selection2_value == 'yes':
                    self.web.find_element(By.XPATH, self.ele.section1_option_1a_yes).click()
                    # 当选择yes的时候，继续输入隐藏输入框
                    # 1.2，1a输入框
                    Enter_txt1 = "Enter additional product description or application information here (general)"
                    general_input_text1 = self.operate_excel.get_text_cols_data(Enter_txt1)
                    general_input_value1 = self.operate_excel.get_value_cols_data(Enter_txt1)
                    if general_input_text1 in Enter_txt1 and general_input_value1:

                        section1_input_general_1a = self.web.find_element(By.XPATH, self.ele.section1_input_general_1a)
                        section1_input_general_1a.clear()
                        section1_input_general_1a.send_keys(general_input_value1)  # mm

                else:
                    self.web.find_element(By.XPATH, self.ele.section1_option_1a_no).click()

            # 1.3 Dimensions & Weight
            # get_section3_txt = self.ele.get_emc_describe(
            #     "nsions & Weight")
            # get_section3_text = self.web.find_element(By.XPATH, get_section3_txt)
            # self.web.driver.execute_script("arguments[0].scrollIntoView(false);", get_section3_text)
            # if 'Dimensions & Weight' in get_section3_text.text:
            weight1_txt = self.ele.get_emc_describe(
                "Weight (enter kilograms OR pounds)")
            weight1_text = self.web.find_element(By.XPATH, weight1_txt)
            selection_weight1_text = self.operate_excel.get_text_cols_data(weight1_text.text)
            selection_weight1_value = self.operate_excel.get_value_cols_data(weight1_text.text)[:-2]
            if selection_weight1_text in weight1_text.text:
                # self.web.find_element(By.XPATH, self.ele.section1_input_1t).send_keys(selection_weight1_value)  # kg
                section1_input_1t = self.web.find_element(By.XPATH, self.ele.section1_input_1t)
                # section1_input_1t.clear()
                section1_input_1t.send_keys(selection_weight1_value)  # mm
                # for i in range(len(selection_weight1_value)):

                    # self.web.find_element(By.XPATH, self.ele.section1_input_2t).send_keys(selection_weight1_value[i])  # lb
            weight2_txt = self.ele.get_emc_describe(
                "Height (enter millimeters OR inches)")
            weight2_text = self.web.find_element(By.XPATH, weight2_txt)
            selection_weight2_text = self.operate_excel.get_text_cols_data(weight2_text.text)
            selection_weight2_value = self.operate_excel.get_value_cols_data(weight2_text.text)[:-2]
            if selection_weight2_text in weight2_text.text:
                # self.web.find_element(By.XPATH, self.ele.section1_input_3t).send_keys(
                #     selection_weight2_value)  # mm

                section1_input_3t = self.web.find_element(By.XPATH, self.ele.section1_input_3t)
                # section1_input_3t.clear()
                section1_input_3t.send_keys(selection_weight2_value)  # mm
                # for i in range(len(selection_weight2_value)):
                #     self.web.find_element(By.XPATH, self.ele.section1_input_1t).send_keys(
                #         selection_weight2_value[i])  # kg
                #     self.web.find_element(By.XPATH, self.ele.section1_input_2t).send_keys(
                #         selection_weight2_value[i])  # lb
            weight3_txt = self.ele.get_emc_describe(
                "Width (enter millimeters OR inches)")
            weight3_text = self.web.find_element(By.XPATH, weight3_txt)
            selection_weight3_text = self.operate_excel.get_text_cols_data(weight3_text.text)
            selection_weight3_value = self.operate_excel.get_value_cols_data(weight3_text.text)[:-2]
            if selection_weight3_text in weight3_text.text:
                # self.web.find_element(By.XPATH, self.ele.section1_input_5t).send_keys(
                #     selection_weight3_value)  # mm

                section1_input_5t = self.web.find_element(By.XPATH, self.ele.section1_input_5t)
                # section1_input_5t.clear()
                section1_input_5t.send_keys(selection_weight3_value)  # mm
                # for i in range(len(selection_weight3_value)):
                #     self.web.find_element(By.XPATH, self.ele.section1_input_1t).send_keys(
                #         selection_weight3_value[i])  # kg
                #     self.web.find_element(By.XPATH, self.ele.section1_input_2t).send_keys(
                #         selection_weight3_value[i])  # lb


            weight4_txt = self.ele.get_emc_describe(
                "Depth (enter millimeters OR inches)")
            weight4_text = self.web.find_element(By.XPATH, weight4_txt)
            selection_weight4_text = self.operate_excel.get_text_cols_data(weight4_text.text)
            selection_weight4_value = self.operate_excel.get_value_cols_data(weight4_text.text)[:-2]
            if selection_weight4_text in weight4_text.text:
                # self.web.find_element(By.XPATH, self.ele.section1_input_7t).send_keys(
                #     selection_weight4_value)  # kg

                section1_input_7t = self.web.find_element(By.XPATH, self.ele.section1_input_7t)
                # section1_input_7t.clear()
                section1_input_7t.send_keys(selection_weight4_value)  # kg
                # for i in range(len(selection_weight4_value)):
                #     self.web.find_element(By.XPATH, self.ele.section1_input_1t).send_keys(
                #         selection_weight4_value[i])  # kg
                #     self.web.find_element(By.XPATH, self.ele.section1_input_2t).send_keys(
                #         selection_weight4_value[i])  # lb

            section5_radio = "no"
            weight5_txt = self.ele.get_emc_describe(
                "Does this product have a screen?")
            get_section5_text = self.web.find_element(By.XPATH, weight5_txt)
            selection5_text = self.operate_excel.get_text_cols_data(get_section5_text.text)
            selection5_value = self.operate_excel.get_value_cols_data(get_section5_text.text)
            if selection5_text in get_section5_text.text:
                if selection5_value == "Yes" or selection5_value == 'yes':
                    self.web.find_element(By.XPATH, self.ele.section1_option_da_yes).click()
                    # 当选择yes的时候，继续输入隐藏输入框
                    # 1.3，1a输入框
                    Screen_input_text1 = self.operate_excel.get_text_cols_data("Screen width")
                    Screen_input_value1 = self.operate_excel.get_value_cols_data("Screen width")[:-2]
                    if Screen_input_text1 in 'Screen width' and Screen_input_value1:
                        section1_input_screen_1a = self.web.find_element(By.XPATH, self.ele.section1_input_screen_1a)
                        section1_input_screen_1a.clear()
                        section1_input_screen_1a.send_keys(Screen_input_value1)  # mm
                    # 1.3，2a输入框
                    Screen_txt2 = "Screen height"
                    Screen_input_text2 = self.operate_excel.get_text_cols_data(Screen_txt2)
                    Screen_input_value2 = self.operate_excel.get_value_cols_data(Screen_txt2)[:-2]
                    if Screen_input_text2 in Screen_txt2 and Screen_input_value2:

                        section1_input_screen_2a = self.web.find_element(By.XPATH, self.ele.section1_input_screen_2a)
                        section1_input_screen_2a.clear()
                        section1_input_screen_2a.send_keys(Screen_input_value2)  # mm
                    # 1.3，3a输入框

                    self.web.find_element(By.XPATH, self.ele.section1_click_screen_3a).click()

                else:
                    self.web.find_element(By.XPATH, self.ele.section1_option_da_no).click()

            # 1.4 Manufacturing Location
            get_section6_txt = self.ele.get_emc_describe(
                "Manufacturing Location")
            get_section6_text = self.web.find_element(By.XPATH, get_section6_txt)
            if 'Manufacturing Location' in get_section6_text.text:
                # 1.4.1 Will Lenovo provide the vendor a manufacturing process developed by Lenovo?

                will_txt1 = self.ele.get_emc_describe(
                    "Will Lenovo provide the vendor a manufacturing process developed by Lenovo?")
                will_text1 = self.web.find_element(By.XPATH, will_txt1)

                will_radio1_text = self.operate_excel.get_text_cols_data(will_text1.text)
                will_radio1_value = self.operate_excel.get_value_cols_data(will_text1.text)

                if will_radio1_text in will_text1.text:
                    if will_radio1_value == "Yes" or will_radio1_value == 'yes':
                        self.web.find_element(By.XPATH, self.ele.section1_will_option_yes).click()
                    else:
                        element = self.web.find_element(By.XPATH, self.ele.section1_will_option_no)

                        self.web.driver.execute_script("arguments[0].click();", element)

                # 1.4.2 Will Lenovo prescribe to the vendor chemicals, manufacturing equipment, or procedures that are unique to the vendor?

                will_txt2 = self.ele.get_emc_describe(
                    "Will Lenovo prescribe to the vendor chemicals, manufacturing equipment, or procedures that are unique to the vendor?")
                will_text2 = self.web.find_element(By.XPATH, will_txt2)
                will_radio2_text = self.operate_excel.get_text_cols_data(will_text2.text)
                will_radio2_value = self.operate_excel.get_value_cols_data(will_text2.text)
                if will_radio2_text in will_text2.text:
                    if will_radio2_value == "Yes" or will_radio2_value == 'yes':
                        self.web.find_element(By.XPATH, self.ele.section2_will_option_yes).click()
                    else:
                        element1 = self.web.find_element(By.XPATH, self.ele.section2_will_option_no)
                        self.web.driver.execute_script("arguments[0].click();", element1)

                # 1.4.3 Will Lenovo furnish the vendor with chemicals or chemical using equipment?

                will_txt3 = self.ele.get_emc_describe(
                    "Will Lenovo furnish the vendor with chemicals or chemical using equipment?")
                will_text3 = self.web.find_element(By.XPATH, will_txt3)
                will_radio3_text = self.operate_excel.get_text_cols_data(will_text3.text)
                will_radio3_value = self.operate_excel.get_value_cols_data(will_text3.text)
                if will_radio3_text in will_text3.text:
                    if will_radio3_value == "Yes" or will_radio3_value == 'yes':
                        self.web.find_element(By.XPATH, self.ele.section3_will_option_yes).click()
                    else:
                        element2 = self.web.find_element(By.XPATH, self.ele.section3_will_option_no)
                        self.web.driver.execute_script("arguments[0].click();", element2)

                # 1.5.1 Is this product being designed, manufactured or sold to another company for sale and distribution under the other company's logo?
                will_txt4 = self.ele.get_emc_describe(
                    "Is this product being designed")
                will_text4 = self.web.find_element(By.XPATH, will_txt4)
                will_radio4_text = self.operate_excel.get_text_cols_data(will_text4.text)
                will_radio4_value = self.operate_excel.get_value_cols_data(will_text4.text)
                if will_radio4_text in will_text4.text:
                    if will_radio4_value == "Yes" or will_radio4_value == 'yes':
                        self.web.find_element(By.XPATH, self.ele.section4_will_option_yes).click()

                        # 当选择YES的时候，需要输入inputs
                        # 1a Company Name文本框
                        Company_txt1 = self.ele.get_emc_describe(
                            "Company Name")
                        Company_text1 = self.web.find_element(By.XPATH, Company_txt1)
                        Company_radio1_text = self.operate_excel.get_text_cols_data(Company_text1.text)
                        Company_radio1_value = self.operate_excel.get_value_cols_data(Company_text1.text)
                        if Company_radio1_text in Company_text1.text and Company_radio1_value:
                            self.web.find_element(By.XPATH, self.ele.section1_company_input_1a).send_keys(
                                Company_radio1_value)  # mm
                        # 2a Company Name文本框
                        Company_txt2 = self.ele.get_emc_describe(
                            "Company address")
                        Company_text2 = self.web.find_element(By.XPATH, Company_txt2)
                        Company_radio2_text = self.operate_excel.get_text_cols_data(Company_text2.text)
                        Company_radio2_value = self.operate_excel.get_value_cols_data(Company_text2.text)
                        if Company_radio2_text in Company_text2.text and Company_radio2_value:
                            self.web.find_element(By.XPATH, self.ele.section1_company_input_2a).send_keys(
                                Company_radio2_value)  # mm
                        # 3a Company address 文本框
                        Company_txt3 = self.ele.get_emc_describe(
                            "Company City")
                        Company_text3 = self.web.find_element(By.XPATH, Company_txt3)
                        Company_radio3_text = self.operate_excel.get_text_cols_data(Company_text3.text)
                        Company_radio3_value = self.operate_excel.get_value_cols_data(Company_text3.text)
                        if Company_radio3_text in Company_text3.text and Company_radio3_value:
                            self.web.find_element(By.XPATH, self.ele.section1_company_input_3a).send_keys(
                                Company_radio3_value)  # mm
                        # 4a Company State/province文本框
                        Company_txt4 = self.ele.get_emc_describe(
                            "Company State/province")
                        Company_text4 = self.web.find_element(By.XPATH, Company_txt4)
                        Company_radio4_text = self.operate_excel.get_text_cols_data(Company_text4.text)
                        Company_radio4_value = self.operate_excel.get_value_cols_data(Company_text4.text)
                        if Company_radio4_text in Company_text4.text and Company_radio4_value:
                            self.web.find_element(By.XPATH, self.ele.section1_company_input_4a).send_keys(
                                Company_radio4_value)  # mm
                        # 5a Company Country 文本框
                        Company_txt5 = self.ele.get_emc_describe(
                            "Company Country")
                        Company_text5 = self.web.find_element(By.XPATH, Company_txt5)
                        Company_radio5_text = self.operate_excel.get_text_cols_data(Company_text5.text)
                        Company_radio5_value = self.operate_excel.get_value_cols_data(Company_text5.text)
                        if Company_radio5_text in Company_text5.text and Company_radio5_value:
                            self.web.find_element(By.XPATH, self.ele.section1_company_input_5a).send_keys(
                                Company_radio5_value)  # mm

                        # 当选择yes的时候，需点击上传按钮
                        attachments_txt1 = self.ele.get_emc_describe(
                            "Click to add attachments")

                        attachments_radio1_value = self.operate_excel.get_value_cols_data("Title")
                        if attachments_radio1_value:
                            self.web.find_element(By.XPATH, attachments_txt1).click()
                            # 切换到最后一个标签页刷新界面
                            win = self.web.driver.current_window_handle
                            print(win)
                            all_handles = self.web.driver.window_handles
                            self.web.driver.switch_to.window(all_handles[-1])
                            # 刷新当前页面
                            self.web.driver.refresh()
                            # attachments title
                            attachments_txt1 = self.ele.get_emc_describe(
                                "Title")
                            attachments_text1 = self.web.find_element(By.XPATH, attachments_txt1)
                            attachments_radio1_text = self.operate_excel.get_text_cols_data(attachments_text1.text)
                            attachments_radio1_value = self.operate_excel.get_value_cols_list(attachments_text1.text)
                            if attachments_radio1_text in attachments_text1.text and attachments_radio1_value:
                                self.web.find_element(By.XPATH, self.ele.section1_attachments_input_1a).send_keys(
                                    attachments_radio1_value[-1])  # mm
                            # attachments Attachments
                            attachments_txt2 = self.ele.get_emc_describe(
                                "Attachments")
                            attachments_text2 = self.web.find_element(By.XPATH, attachments_txt2)

                            attachments_radio2_text = self.operate_excel.get_text_cols_data(attachments_text2.text)
                            attachments_radio2_value = self.operate_excel.get_value_cols_list(attachments_text2.text)

                            attachments_annex = self.ele.get_emc_describe(
                                "单击此处以附加文件")

                            if attachments_radio2_text in attachments_text2.text and attachments_radio2_value[-1]:


                                # 点击选择文件按钮
                                section1_click_a1 = self.web.find_element(By.XPATH, attachments_annex)
                                section1_click_a1.click()

                                xuan_file2 = self.web.find_element(By.XPATH, self.ele.select_file)
                                ActionChains(self.web.driver).move_to_element(xuan_file2).click().perform()

                                time.sleep(5)
                                edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                                        ClassName="Edit")
                                print(edit)
                                # 获取当前文件的根目录
                                current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                                file_path = os.path.join(self.application_path + "\\filedata", attachments_radio2_value[-1])
                                # 输入文件的路径加名称
                                edit.SendKeys(file_path)
                                # 点击打开按钮，确定选中的文件
                                auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                                # 附加按钮
                                fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                                ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()

                                # 上传成功后验证是否成功
                                attachments_file = self.web.find_element(By.XPATH, self.ele.section1_spfa_text1)
                                if attachments_file.text.find(attachments_radio2_value[-1]) != -1:
                                    print("上传成功了！")
                                else:
                                    print("上传失败了")

                            # attachments Related - PERD
                            attachments_txt3 = self.ele.get_emc_describe(
                                "Related - PERD")
                            attachments_text3 = self.web.find_element(By.XPATH, attachments_txt3)
                            attachments_radio3_text = self.operate_excel.get_text_cols_data(attachments_text3.text)
                            attachments_radio3_value = self.operate_excel.get_value_cols_data(attachments_text3.text)
                            if attachments_radio3_text in attachments_text3.text and attachments_radio3_value:
                                try:
                                    section2_select = self.web.find_element(By.XPATH, self.ele.section1_attachments_select_3a)

                                    Select(section2_select).select_by_visible_text(attachments_radio3_value)
                                except:
                                    print("找不到选项")
                            # attachments Section Name
                            attachments_txt4 = self.ele.get_emc_describe(
                                "Section Name")
                            attachments_text4 = self.web.find_element(By.XPATH, attachments_txt4)
                            attachments_radio4_text = self.operate_excel.get_text_cols_data(attachments_text4.text)
                            attachments_radio4_value = self.operate_excel.get_value_cols_data(
                                attachments_text4.text)
                            if attachments_radio4_text in attachments_text4.text and attachments_radio4_value:
                                try:
                                    section3_select = self.web.find_element(By.XPATH,
                                                                            self.ele.section1_attachments_select_4a)

                                    Select(section3_select).select_by_value(attachments_radio4_value)
                                except:
                                    print("找不到选项")

                            # Description
                            attachments_txt5 = self.ele.get_emc_describe(
                                "Description")
                            attachments_text5 = self.web.find_element(By.XPATH, attachments_txt5)
                            attachments_radio5_text = self.operate_excel.get_text_cols_data(attachments_text5.text)
                            attachments_radio5_value = self.operate_excel.get_value_cols_list(
                                attachments_text5.text)
                            if attachments_radio5_text in attachments_text5.text and attachments_radio5_value:
                                description_text = self.web.find_element(By.XPATH, self.ele.section1_attachments_input_5a)
                                description_text.click()
                                description_text.send_keys(attachments_radio5_value[-1])  # mm

                            # 填写完成后点击提交按钮
                            self.web.find_element(By.XPATH, self.ele.section1_attachments_savebut).click()
                            # 提交完成后，关闭当前的标签页
                            self.web.driver.close()

                    else:
                        element3 = self.web.find_element(By.XPATH, self.ele.section4_will_option_no)
                        self.web.driver.execute_script("arguments[0].click();", element3)

            if self.web.find_element(By.XPATH, self.ele.submit_completed_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()

                time.sleep(15)
                self.web.driver.close()
                print("填写完成，提交！")

    def perd_section2(self):
        # 读取excel文档，根据选中的section2，读取section2内容
        self.operate_excel = OperateExcel(self.file_path, 'Section 2')
        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section2状态
        time.sleep(10)
        section2_status = self.web.driver.find_element(By.XPATH,self.ele.setion2_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section2_status)
        if section2_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section2_status.get_attribute("value"):
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section2执行用例
            self.web.driver.find_element(By.XPATH,self.ele.section2_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 2.1 Power Consumption
            does_txt1 = self.ele.get_div_describe("Does this product consume any power? (Consider power consumption of the product when fully featured.)")
            does_text1 = self.web.find_element(By.XPATH, does_txt1)
            does_radio2_text = self.operate_excel.get_text_cols_data(does_text1.text)
            does_radio2_value = self.operate_excel.get_value_cols_data(does_text1.text)
            if does_radio2_text in does_text1.text:
                if does_radio2_value == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section2_option_2a_yes).click()
                    # 当点击yes 的时候，隐藏项填写输入
                    # 2.2 Power Modes
                    does_txt2 = self.ele.get_emc_describe(
                        "Power Modes")
                    does_text2 = self.web.find_element(By.XPATH, does_txt2)
                    self.web.driver.execute_script("arguments[0].scrollIntoView();", does_text2)
                    if 'Power Modes' in does_text2.text:
                        # 2.2.1
                        does_txt3 = self.ele.get_emc_describe(
                            "Is this product Energy Star Certified?")
                        does_text3 = self.web.find_element(By.XPATH, does_txt3)
                        does_radio3_text = self.operate_excel.get_text_cols_data(does_text3.text)
                        does_radio3_value = self.operate_excel.get_value_cols_data(does_text3.text)
                        if does_radio3_text in does_text3.text:
                            self.web.find_element(By.XPATH, self.ele.section2_option_3a_yes).click()
                            self.web.find_element(By.XPATH, self.ele.section2_option_3a_no).click()
                            if does_radio3_value == "Yes":
                                self.web.find_element(By.XPATH, self.ele.section2_option_3a_yes).click()
                                # 隐藏上传
                                # 2.2.2.a 点击附件上传  section2_click_a

                                does_txt22a = "Attach the OFFICIAL 'Third Party' Test Report."
                                does_radio22a_text = self.operate_excel.get_text_cols_data(does_txt22a)
                                does_radio22a_value = self.operate_excel.get_value_cols_data(does_txt22a)

                                if does_radio22a_value:
                                    # self.web.find_element(By.XPATH, self.ele.section2_click1_2a).click()
                                    #
                                    # attachments_annex1 = self.ele.get_emc_describe(
                                    #     "单击此处以附加文件")
                                    # 点击附件文件按钮
                                    section2_click25_aa1 = self.web.find_element(By.XPATH, self.ele.section2_click1_2a)
                                    section2_click25_aa1.click()

                                    xuan_file1 = self.web.find_element(By.XPATH, self.ele.select_file)
                                    ActionChains(self.web.driver).move_to_element(xuan_file1).click().perform()

                                    time.sleep(5)
                                    edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                                            ClassName="Edit")
                                    print(edit)
                                    # 获取当前文件的根目录
                                    current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                                    file_path = os.path.join(self.application_path + "\\filedata", does_radio22a_value)
                                    # 输入文件的路径加名称
                                    edit.SendKeys(file_path)
                                    # 点击打开按钮，确定选中的文件
                                    auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                                    # 附加按钮
                                    fujia_file1 = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                                    ActionChains(self.web.driver).move_to_element(fujia_file1).click().perform()

                                    # 上传成功后验证是否成功
                                    if self.web.find_element(By.XPATH, self.ele.section2_click1_2a).text.find(does_radio22a_value) != -1:
                                        print("上传成功了！")
                                    else:
                                        print("上传失败了")

                                # 2.2.2.b 点击附件上传  Attach the Energy Star Test Certificate.
                                does_txt22b = "Attach the Energy Star Test Certificate."
                                does_radio22b_text = self.operate_excel.get_text_cols_data(does_txt22b)
                                does_radio22b_value = self.operate_excel.get_value_cols_data(does_txt22b)

                                if does_radio22b_text in does_txt22b and does_radio22b_value:

                                    # 点击上传附件文件按钮
                                    section2_click25_aa2 = self.web.find_element(By.XPATH, self.ele.section2_click2_2a)
                                    section2_click25_aa2.click()

                                    xuan_file2 = self.web.find_element(By.XPATH, self.ele.select_file)
                                    ActionChains(self.web.driver).move_to_element(xuan_file2).click().perform()

                                    time.sleep(5)
                                    edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                                            ClassName="Edit")
                                    print(edit)
                                    # 获取当前文件的根目录
                                    file_path = os.path.join(self.application_path + "\\filedata", does_radio22b_value)
                                    # 输入文件的路径加名称
                                    edit.SendKeys(file_path)
                                    # 点击打开按钮，确定选中的文件
                                    auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                                    # 附加按钮
                                    fujia_file2 = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                                    ActionChains(self.web.driver).move_to_element(fujia_file2).click().perform()

                                    # 上传成功后验证是否成功
                                    if self.web.find_element(By.XPATH, self.ele.section2_click2_2a).text.find(does_radio22b_value) != -1:
                                        print("上传成功了！")
                                    else:
                                        print("上传失败了")

                            else:
                                self.web.find_element(By.XPATH, self.ele.section2_option_3a_no).click()
                                # 2.2.2.a 点击附件上传  section2_click_a
                                # 调用封装方法
                                self.updata_file(
                                    "Attach the In-House Power Consumption Test Report.",
                                    self.ele.section2_click_a)

                        # 2.2.3
                        does_txt23 = self.ele.get_div_describe(
                            "Provide the rating of the power supply (maximum allowed power draw).")
                        does_text23 = self.web.find_element(By.XPATH, does_txt23)
                        does_radio23_text = self.operate_excel.get_text_cols_data(does_text23.text)
                        does_radio23_value = self.operate_excel.get_value_cols_data(does_text23.text)
                        if does_radio23_value:
                            section2_input_txt = self.web.find_element(By.XPATH, self.ele.section2_input)
                            if section2_input_txt.get_attribute("value") != None:
                                section2_input_txt.clear()
                            else:
                                self.web.find_element(By.XPATH, self.ele.section2_input).send_keys(does_radio23_value)  # w

                        # 2.2.4
                        does_txt24 = self.ele.get_div_describe(
                            "Does this personal computer product (laptops, desktops) have an external power supply (AC adapter(s)) that are sold with the product as a unit?")
                        does_text24 = self.web.find_element(By.XPATH, does_txt24)
                        does_radio24_text = self.operate_excel.get_text_cols_data(does_text24.text)
                        does_radio24_value = self.operate_excel.get_value_cols_data(does_text24.text)
                        if does_radio24_text in does_text24.text:
                            if does_radio24_value == "Yes":
                                self.web.find_element(By.XPATH, self.ele.section2_option_4a_yes).click()
                                # 点yes后才会有后续显示
                                # 2.2.5
                                does_txt25 = self.ele.get_emc_describe(
                                    "Provide watts for external power supply(s) in no load condition.")
                                does_text25 = self.web.find_element(By.XPATH, does_txt25)
                                # 输入文本 1.input
                                does_txt25_input1 = self.ele.get_emc_describe(
                                    "watts at 100V")
                                does_text25_input1 = self.web.find_element(By.XPATH, does_txt25_input1)
                                does_radio25_input1_text = self.operate_excel.get_text_cols_data(
                                    does_text25_input1.text)
                                does_radio25_input1_value = self.operate_excel.get_value_cols_data(
                                    does_text25_input1.text)
                                if does_radio25_input1_value:
                                    self.web.find_element(By.XPATH, self.ele.section2_input2_5a).click()
                                    self.web.find_element(By.XPATH, self.ele.section2_input2_5a).send_keys(
                                        does_radio25_input1_value)  # w
                                # 输入文本 2.input
                                does_txt25_input2 = self.ele.get_emc_describe(
                                    "watts at 115V")
                                does_text25_input2 = self.web.find_element(By.XPATH, does_txt25_input2)
                                does_radio25_input2_text = self.operate_excel.get_text_cols_data(
                                    does_text25_input2.text)
                                does_radio25_input2_value = self.operate_excel.get_value_cols_data(
                                    does_text25_input2.text)
                                if does_radio25_input2_value:
                                    self.web.find_element(By.XPATH, self.ele.section2_input3_5a).click()
                                    self.web.find_element(By.XPATH, self.ele.section2_input3_5a).send_keys(
                                        does_radio25_input2_value)  # w
                                # 输入文本 3.input
                                does_txt25_input3 = self.ele.get_emc_describe(
                                    "watts at 230V")
                                does_text25_input3 = self.web.find_element(By.XPATH, does_txt25_input3)
                                does_radio25_input3_text = self.operate_excel.get_text_cols_data(
                                    does_text25_input3.text)
                                does_radio25_input3_value = self.operate_excel.get_value_cols_data(
                                    does_text25_input3.text)
                                if does_radio25_input3_value:
                                    self.web.find_element(By.XPATH, self.ele.section2_input4_5a).click()
                                    self.web.find_element(By.XPATH, self.ele.section2_input4_5a).send_keys(
                                        does_radio25_input3_value)  # w
                                # 2.2.5
                                # 2.2.5.1
                                # 调用封装方法
                                self.updata_li_file(
                                    "Attach Power Consumption Test report for external power supply.",
                                    self.ele.section2_click25_a1)
                                # 2.2.5.2
                                # 调用封装方法
                                self.updata_li_file(
                                    "Attach NRCan Amendment 11 Certification/Registration report.",
                                    self.ele.section2_click25_a2)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section2_option_4a_no).click()



                    #2.3 Measured Heat Output
                    # 2.3.1
                    does_txt23ou = self.ele.get_emc_describe(
                        "Measured Heat Output")
                    does_text23ou = self.web.find_element(By.XPATH, does_txt23ou)
                    does_radio23_input1_text = self.operate_excel.get_text_cols_data(
                        does_text23ou.text)
                    if does_radio23_input1_text in does_text23ou.text:
                        # 输入文本 1.input
                        does_txt25_input1 = self.ele.get_div_describe("Provide the product")
                        does_text23_input1 = self.web.find_element(By.XPATH, does_txt25_input1)
                        does_radio23_input1_text = self.operate_excel.get_text_cols_data(
                            does_text23_input1.text)
                        does_radio23_input1_value = self.operate_excel.get_value_cols_data(
                            does_text23_input1.text)
                        if does_radio23_input1_text in does_text23_input1.text and does_radio23_input1_value:
                            does_list = does_radio23_input1_value.split(',')
                            self.web.find_element(By.XPATH, self.ele.section2_measured_input_a1).send_keys(does_list[0])  # w
                            self.web.find_element(By.XPATH, self.ele.section2_measured_input_a2).send_keys(
                                does_list[1])  # w
                    # 2.3.2 Select the JEL Product type
                    get_section2_txt = self.ele.get_div_describe("Select the JEL Product type")
                    get_section2_text = self.web.find_element(By.XPATH, get_section2_txt)
                    selection_text = self.operate_excel.get_text_cols_data(get_section2_text.text)
                    selection_value = self.operate_excel.get_value_cols_data(get_section2_text.text)
                    if selection_text in get_section2_text.text and selection_value:
                        # 下拉选择项目
                        self.web.find_element(By.XPATH, self.ele.section2_select_a).click()
                        get_section2_text.click()
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_a)
                        Select(section1_select).select_by_value(selection_value)


                        # 输入文本 2.Inputs
                        does_txt24_input2 = self.ele.get_div_describe(
                            "Inputs")
                        does_text24_input2 = self.web.find_element(By.XPATH, does_txt24_input2)
                        does_radio24_input2_text = self.operate_excel.get_text_cols_data(
                            does_text24_input2.text)
                        does_radio24_input2_value = self.operate_excel.get_value_cols_data(
                            does_text24_input2.text)
                        if does_radio24_input2_text in does_text24_input2.text and does_radio24_input2_value:

                            self.web.find_element(By.XPATH, self.ele.section2_select_inputs).send_keys(
                                does_radio24_input2_value)  # w



                else:
                    self.web.find_element(By.XPATH, self.ele.section2_option_2a_no).click()

                #2.5
                does_txt_radio25 = self.ele.get_emc_describe(
                    "Was China Energy conservation Program(CECP) certificate required?")
                does_text_radio25 = self.web.find_element(By.XPATH, does_txt_radio25)
                does_radio25_text = self.operate_excel.get_text_cols_data(does_text_radio25.text)
                does_radio25_value = self.operate_excel.get_value_cols_data(does_text_radio25.text)
                if does_radio25_value:
                    if does_radio25_value == "Yes":
                        self.web.find_element(By.XPATH, self.ele.section2_option_5a_yes).click()
                        # 2.5.2 隐藏元素
                        # 调用封装方法
                        self.updata_file(
                            "Attach the CECP Certificate and/or CECP Test Report.",
                            self.ele.section2_click_cecp_a)
                        # 输入文本 2.5.Exclusions
                        does_txt25_input2 = self.ele.get_emc_describe(
                            "Exclusions")
                        does_text25_input2 = self.web.find_element(By.XPATH, does_txt25_input2)
                        does_radio25_input2_text = self.operate_excel.get_text_cols_data(
                            does_text25_input2.text)
                        does_radio25_input2_value = self.operate_excel.get_value_cols_data(
                            does_text25_input2.text)
                        if does_radio25_input2_text in does_text25_input2.text and does_radio25_input2_value:
                            self.web.find_element(By.XPATH, self.ele.section2_select_inputs).send_keys(
                                does_radio25_input2_value)  # w
                    else:
                        self.web.find_element(By.XPATH, self.ele.section2_option_5a_no).click()

                # 2.6.1
                does_txt_radio26 = self.ele.get_div_describe(
                    "Does this product contain rechargeable battery/battery circuit or stand alone battery charger?")
                does_text_radio26 = self.web.find_element(By.XPATH, does_txt_radio26)
                does_radio26_text = self.operate_excel.get_text_cols_data(does_text_radio26.text)
                does_radio26_value = self.operate_excel.get_value_cols_data(does_text_radio26.text)

                if does_radio26_text in does_text_radio26.text:
                    if does_radio26_value == "Yes":
                        self.web.find_element(By.XPATH, self.ele.section2_option_6a_yes).click()
                        # 2.6.1 隐藏选项
                        # 调用封装方法
                        self.updata_div_file(
                            "California Appliance Battery Charger Data",
                            self.ele.section2_option_6a_click_a)
                    else:
                        self.web.find_element(By.XPATH, self.ele.section2_option_6a_no).click()
                # 2.7.1
                does_txt_radio27 = self.ele.get_emc_describe(
                    "Is this product a Monitor?")
                does_text_radio27 = self.web.find_element(By.XPATH, does_txt_radio27)
                does_radio27_text = self.operate_excel.get_text_cols_data(does_text_radio27.text)
                does_radio27_value = self.operate_excel.get_value_cols_data(does_text_radio27.text)

                if does_radio27_text in does_text_radio27.text:
                    if does_radio27_value == "Yes":
                        self.web.find_element(By.XPATH, self.ele.section2_option_7a_yes).click()
                        # 2.7.2 Will this product ship to Israel?
                        does_txt_radio272 = self.ele.get_emc_describe(
                            "Will this product ship to Israel?")
                        does_text_radio272 = self.web.find_element(By.XPATH, does_txt_radio272)
                        does_radio272_text = self.operate_excel.get_text_cols_data(does_text_radio272.text)
                        does_radio272_value = self.operate_excel.get_value_cols_data(does_text_radio272.text)
                        if does_radio272_text in does_text_radio272.text and does_radio272_value:
                            if does_radio272_value == "Yes":
                                self.web.find_element(By.XPATH, self.ele.section2_option2_7a_yes).click()
                            else:
                                self.web.find_element(By.XPATH, self.ele.section2_option2_7a_no).click()
                        # 输入日期文本 2.7.3 What is the target date of Product Certification?
                        does_txt273_input2 = self.ele.get_emc_describe(
                            "What is the target date of Product Certification?")
                        does_text273_input2 = self.web.find_element(By.XPATH, does_txt273_input2)
                        does_radio273_input2_text = self.operate_excel.get_text_cols_data(
                            does_text273_input2.text)
                        does_radio273_input2_value = self.operate_excel.get_value_cols_data(
                            does_text273_input2.text)
                        if does_radio273_input2_text in does_text273_input2.text and does_radio273_input2_value:
                            self.web.find_element(By.XPATH, self.ele.section2_input_date).send_keys(
                                does_radio273_input2_value)  # w


                    else:
                        self.web.find_element(By.XPATH, self.ele.section2_option_7a_no).click()
                # 2.8.1
                does_txt_radio28 = self.ele.get_emc_describe(
                    "Will this product ship to Australia/New Zealand")
                does_text_radio28 = self.web.find_element(By.XPATH, does_txt_radio28)
                does_radio28_text = self.operate_excel.get_text_cols_data(does_text_radio28.text)
                does_radio28_value = self.operate_excel.get_value_cols_data(does_text_radio28.text)
                if does_radio28_text in does_text_radio28.text:
                    if does_radio28_value == "Yes":
                        self.web.find_element(By.XPATH, self.ele.section2_option_8a_yes).click()
                    else:
                        self.web.find_element(By.XPATH, self.ele.section2_option_8a_no).click()
                # 2.9.1
                does_txt_radio29 = self.ele.get_emc_describe(
                    "Will this product ship to the EU?")
                does_text_radio29 = self.web.find_element(By.XPATH, does_txt_radio29)
                does_radio29_text = self.operate_excel.get_text_cols_data(does_text_radio29.text)
                does_radio29_value = self.operate_excel.get_value_cols_data(does_text_radio29.text)
                if does_radio29_text in does_text_radio29.text:
                    if does_radio29_value == "Yes":
                        self.web.find_element(By.XPATH, self.ele.section2_option_9a_yes).click()
                    else:
                        self.web.find_element(By.XPATH, self.ele.section2_option_9a_no).click()

                # 2.9.2
                does_txt_radio29_1a = self.ele.get_emc_describe(
                    "Identify the Product/Technology Family")
                does_text_radio29_1a = self.web.find_element(By.XPATH, does_txt_radio29_1a)
                does_radio29_text2 = self.operate_excel.get_text_cols_data(does_text_radio29_1a.text)
                does_radio29_value2 = self.operate_excel.get_value_cols_data(does_text_radio29_1a.text)
                if does_radio29_text2 in does_text_radio29_1a.text and does_radio29_value2:
                    # 下拉选择项目
                    self.web.find_element(By.XPATH, self.ele.section2_select_9a).click()
                    does_text_radio29_1a.click()
                    section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                    Select(section1_select).select_by_visible_text("Select...")
                    if does_radio29_value2 == 'Desktop':
                        # 下拉选择项目
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                        Select(section1_select).select_by_value(does_radio29_value2)

                        # 单选按钮选择
                        does_txt_radio293 = self.ele.get_emc_describe(
                            "Does this Product have an external power supply (AC Adapter(s)) that are sold with the product as a unit?")
                        does_text_radio293 = self.web.find_element(By.XPATH, does_txt_radio293)
                        does_radio293_text = self.operate_excel.get_text_cols_data(does_text_radio293.text)
                        does_radio293_value = self.operate_excel.get_value_cols_data(does_text_radio293.text)
                        if does_radio293_text in does_text_radio293.text and does_radio293_value:
                            if does_radio29_value == "Yes":
                                self.web.find_element(By.XPATH, self.ele.section2_option_10a_yes).click()
                                # 调用封装方法
                                self.updata_file(
                                    "Please attach the required ErP Lot 3 and/or ErP Lot 7 test Report",
                                    self.ele.section2_click294_a1)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section2_option_10a_no).click()
                                # 调用封装方法
                                self.updata_file("Please attach the required ErP Lot 3 Test Report",
                                                 self.ele.section2_click294_a2)
                    elif does_radio29_value2 == 'Monitors':
                        # 下拉选择项目
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                        Select(section1_select).select_by_value(does_radio29_value2)
                        # 调用封装方法
                        self.updata_file("Please attach the required ErP Lot 5 OR ErP Lot 6 Test Report",
                                         self.ele.section2_click293_a1)
                    elif does_radio29_value2 == 'NoteBook':
                        # 下拉选择项目
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                        Select(section1_select).select_by_value(does_radio29_value2)
                        # 调用封装方法
                        self.updata_file(
                            "Please attach the required ErP Lot 3, ErP Lot 6 and/or ErP Lot 7 Test Report",
                            self.ele.section2_click293_a2)
                    elif does_radio29_value2 == 'Options':
                        # 下拉选择项目
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                        Select(section1_select).select_by_value(does_radio29_value2)

                        get_data_value = self.operate_excel.get_value_cols_data("Please attach the required ErP Lot 6/Lot 26 and/or ErP Lot 7 Test Report")

                        # 调用封装方法
                        self.updata_file(
                            "Please attach the required ErP Lot 6/Lot 26 and/or ErP Lot 7 Test Report",
                            self.ele.section2_click293_a3)
                    elif does_radio29_value2 == 'Server':
                        # 下拉选择项目
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                        Select(section1_select).select_by_value(does_radio29_value2)
                        # 调用封装方法
                        self.updata_file("Please attach the required ErP Lot 3 OR ErP Lot 9 Test Report",
                                         self.ele.section2_click293_a4)
                    elif does_radio29_value2 == 'Workstation':
                        # 下拉选择项目
                        section1_select = self.web.find_element(By.XPATH, self.ele.section2_select_9a)
                        Select(section1_select).select_by_value(does_radio29_value2)
                        # 调用封装方法
                        self.updata_file("Please attach the required ErP Lot 3 Test Report",
                                         self.ele.section2_click293_a5)

            if self.web.find_element(By.XPATH, self.ele.submit_completed_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()
                time.sleep(15)
                self.web.driver.close()
                print("填写完成，提交！")

    def perd_section3(self):
        # 读取excel文档，根据选中的section3，读取section3内容
        self.operate_excel = OperateExcel(self.file_path, 'Section 3')
        # self.operate_excel.get_sheet("Section 3")
        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section3状态
        time.sleep(10)
        section3_status = self.web.driver.find_element(By.XPATH,self.ele.setion3_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section3_status)
        if section3_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section3_status.get_attribute("value"):
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section2执行用例
            self.web.driver.find_element(By.XPATH,self.ele.section3_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 3.1 Bill of Materials
            bill_mate = self.ele.get_emc_describe(
                "Bill of Materials")
            bill_mate_el = self.web.find_element(By.XPATH, bill_mate)
            bill_mate_text = self.operate_excel.get_text_cols_data(bill_mate_el.text)
            print(bill_mate_el.text)
            print(bill_mate_text)
            if bill_mate_text in bill_mate_el.text:
                # 3.1.1
                bill_txt_1a = self.ele.get_emc_describe(
                    "Does this product contain part assemblies that have their own PERD documents?")
                bill_text_1a = self.web.find_element(By.XPATH, bill_txt_1a)
                bill_select_text1 = self.operate_excel.get_text_cols_data(bill_text_1a.text)
                bill_select_value1 = self.operate_excel.get_value_cols_data(bill_text_1a.text)
                self.web.driver.execute_script("arguments[0].scrollIntoView();", bill_text_1a)
                if bill_select_value1:
                    if "Yes" in bill_select_value1:
                        # 下拉选择项目
                        self.web.find_element(By.XPATH, self.ele.section3_select_1a).click()
                        bill_text_1a.click()
                        section1_select = self.web.find_element(By.XPATH, self.ele.section3_select_1a)
                        Select(section1_select).select_by_visible_text(bill_select_value1)
                        # 出现隐藏的输入框 3
                        self.section_input("Please list the relevant component PERD reference(s)",self.ele.section3_input_1a)
                        # Comments
                        self.section_dev_input("Comments",self.ele.section3_input_2a)
                    else:
                        # 下拉选择项目
                        self.web.find_element(By.XPATH, self.ele.section3_select_1a).click()
                        bill_text_1a.click()
                        section1_select = self.web.find_element(By.XPATH, self.ele.section3_select_1a)
                        Select(section1_select).select_by_visible_text(bill_select_value1)

                # 3.1.2
                bill3_txt_2a = self.ele.get_div_describe(
                    "Does this product contain at least one type of plastic material weighing 25 grams or more?")
                bill3_text_2a = self.web.find_element(By.XPATH, bill3_txt_2a)
                bill3_select_text2 = self.operate_excel.get_text_cols_data(bill3_text_2a.text)
                bill3_select_value2 = self.operate_excel.get_value_cols_data(bill3_text_2a.text)
                if bill3_select_value2:
                    # 下拉选择项目
                    self.web.find_element(By.XPATH, self.ele.section3_select_2a).click()
                    bill3_text_2a.click()
                    section1_select = self.web.find_element(By.XPATH, self.ele.section3_select_2a)

                    Select(section1_select).select_by_visible_text(bill3_select_value2)
                    # # 3.1.2 上传
                    self.updata_file("Please create a mechanical bill of material for all major parts.",
                                     self.ele.section3_click_a)
                    # 判断下拉选择是否为yes选项
                    if "Yes" in bill3_select_value2:
                        # Comments
                        self.section_input_list("Comments", self.ele.section3_input_3a, 0)



                # # 3.1.2 上传
                # bill3_input_1a = self.ele.get_emc_describe(
                #     "Please create a mechanical bill of material for all major parts.")
                # bill3_input_1a = self.web.find_element(By.XPATH, bill3_input_1a)
                # bill3_input_text1 = self.operate_excel.get_text_cols_data(bill3_input_1a.text)
                # bill3_input_value1 = self.operate_excel.get_value_cols_data(bill3_input_1a.text)
                # self.web.driver.execute_script("arguments[0].scrollIntoView();", bill3_input_1a)
                # if bill3_input_value1:
                #     # 点击附件文件按钮
                #     section3_click_a = self.web.find_element(By.XPATH, self.ele.section3_click_a)
                #     section3_click_a.click()
                #
                #     # 选择文件
                #     xuan_file = self.web.find_element(By.XPATH, self.ele.select_file)
                #     ActionChains(self.web.driver).move_to_element(xuan_file).click().perform()
                #
                #     time.sleep(5)
                #     edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32", ClassName="Edit")
                #     print(edit)
                #     # 获取当前文件的根目录
                #     self.application_path = os.path.abspath(os.path.dirname((os.getcwd())))
                #     file_path = os.path.join(current_path + "\\filedata", bill3_input_value1)
                #     # 输入文件的路径加名称
                #     edit.SendKeys(file_path)
                #     # 点击打开按钮，确定选中的文件
                #     auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click() # 打开
                #     # 附加按钮
                #     fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                #     ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()
                #
                #     # 上传成功后验证是否成功
                #     if section3_click_a.text.find(bill3_input_value1) != -1:
                #         print("上传成功了！")
                #     else:
                #         print("上传失败了")

                # 3.2.1
                bill3_txt_3a = self.ele.get_div_describe(
                    "Does this product contain beryllium compounds at greater than 0.02% by weight (200 parts per million) of product? (If yes, fill out information about beryllium compounds in a reportable substance list.).")
                bill3_text_3a = self.web.find_element(By.XPATH, bill3_txt_3a)
                bill3_select_text3 = self.operate_excel.get_text_cols_data(bill3_text_3a.text)
                bill3_select_value3 = self.operate_excel.get_value_cols_data(bill3_text_3a.text)
                if bill3_select_value3:
                    # 下拉选择项目
                    self.web.find_element(By.XPATH, self.ele.section3_select2_1a).click()
                    bill3_text_3a.click()
                    section1_select = self.web.find_element(By.XPATH, self.ele.section3_select2_1a)

                    Select(section1_select).select_by_visible_text(bill3_select_value3)

                    if 'Yes' in bill3_select_value3:
                        # 3.2.1a  Provide the method used to determine beryllium concentration.
                        # 下拉选择项目
                        self.section_select("Provide the method used to determine beryllium concentration.",self.ele.section3_select2_1a2)

                # 3.2.2
                bill3_txt_4a = self.ele.get_div_describe(
                    "Does this product contain any mercury (e.g., fluorescent lamps containing mercury in LCD screen, scanner, backlight for touchscreen; mercury vapor lamps in projectors; etc.)?")
                bill3_text_4a = self.web.find_element(By.XPATH, bill3_txt_4a)
                bill3_select_text4 = self.operate_excel.get_text_cols_data(bill3_text_4a.text)
                bill3_select_value4 = self.operate_excel.get_value_cols_data(bill3_text_4a.text)
                if bill3_select_value4:
                    if bill3_select_value4 == "Yes" or bill3_select_value4 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_1a_yes).click()
                        # 3.2.2.a For Products Containing mercury, indicate the following:
                        # # 下拉选择项目
                        # self.section_select("Provide the method used to determine beryllium concentration.",
                        #                     self.ele.section3_select2_1a2)
                        bill3_select_txt4a = self.ele.get_emc_describe("Provide the method used to determine beryllium concentration.")
                        bill3_select_text4a = self.web.find_element(By.XPATH, bill3_select_txt4a)
                        select_cols_text = self.operate_excel.get_text_cols_data(bill3_select_text4a.text)
                        select_cols_value = self.operate_excel.get_value_cols_list(bill3_select_text4a.text)[1]
                        if select_cols_text in bill3_select_text4a.text and select_cols_value:
                            # 下拉选择项目
                            self.web.find_element(By.XPATH, self.ele.section3_select3a_1a).click()
                            bill3_select_text4a.click()
                            section1_select = self.web.find_element(By.XPATH, self.ele.section3_select3a_1a)

                            Select(section1_select).select_by_visible_text(select_cols_value)

                            if select_cols_value == 'Other':
                                # input
                                self.section_input_list("If other, define.",self.ele.section3_select_input3a_2a,0)
                        # 3.2.2.b
                        # How many mercury containing components ( as listed in 3.2.2.a) are present in the product?
                        self.section_input("How many mercury containing components ( as listed in 3.2.2.a) are present in the product?",self.ele.section3_input3b_2a)
                        # 3.2.2.c
                        # How many mercury containing components ( as listed in 3.2.2.a) are present in the product?
                        self.section_input(
                            "List the mercury content of each component.",
                            self.ele.section3_input3c_3a)
                        # 3.2.2.d
                        # How many mercury containing components ( as listed in 3.2.2.a) are present in the product?
                        self.section_input(
                            "What is the total amount of mercury in the entire product.",
                            self.ele.section3_input3d_4a)

                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_1a_no).click()
                # 3.2.3
                bill3_txt_4a = self.ele.get_div_describe(
                    "Are there any flame retardant plastic materials in the bill of material(s)?")
                bill3_text_4a = self.web.find_element(By.XPATH, bill3_txt_4a)
                bill3_select_text4 = self.operate_excel.get_text_cols_data(bill3_text_4a.text)
                bill3_select_value4 = self.operate_excel.get_value_cols_data(bill3_text_4a.text)
                if bill3_select_value4:
                    # 下拉选择项目
                    self.web.find_element(By.XPATH, self.ele.section3_select2_2a).click()
                    bill3_text_4a.click()
                    section1_select = self.web.find_element(By.XPATH, self.ele.section3_select2_2a)

                    Select(section1_select).select_by_visible_text(bill3_select_value4)
                # 3.2.4
                bill3_3244_text = "Does the product contain Other reportable substances?"
                bill3_txt_5a = self.ele.get_div_describe(
                    bill3_3244_text)
                bill3_text_5a = self.web.find_element(By.XPATH, bill3_txt_5a)
                bill3_select_text5 = self.operate_excel.get_text_cols_data(bill3_3244_text)
                bill3_select_value5 = self.operate_excel.get_value_cols_data(bill3_3244_text)

                if bill3_select_value5:
                    # 下拉选择项目
                    self.web.find_element(By.XPATH, self.ele.section3_select2_3a).click()
                    bill3_text_5a.click()
                    section1_select = self.web.find_element(By.XPATH, self.ele.section3_select2_3a)

                    Select(section1_select).select_by_visible_text(bill3_select_value5)
                    if 'Yes' in bill3_select_value5:
                        # 输入框 input Comments
                        self.section_input_list("Comments",self.ele.section3_input2_3a,2)

                # 3.2.5
                bill3_txt_6a = self.ele.get_div_describe(
                    "Does the product contain any Waste Electrical and Electronic Equipment (WEEE) Components?")
                bill3_text_6a = self.web.find_element(By.XPATH, bill3_txt_6a)
                bill3_select_text6 = self.operate_excel.get_text_cols_data(bill3_text_6a.text)
                bill3_select_value6 = self.operate_excel.get_value_cols_data(bill3_text_6a.text)
                if bill3_select_value6:
                    if bill3_select_value6 == "Yes" or bill3_select_value6 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_2a_yes).click()
                        # 选择yes后，显示3.2.5后选项
                        # 3.2.5 a
                        bill3_txt_7a = self.ele.get_div_describe(
                            "Does the product contain Gas discharge lamps?")
                        bill3_text_7a = self.web.find_element(By.XPATH, bill3_txt_7a)
                        bill3_select_text7 = self.operate_excel.get_text_cols_data(bill3_text_7a.text)
                        bill3_select_value7 = self.operate_excel.get_value_cols_data(bill3_text_7a.text)
                        if bill3_select_value7:
                            if bill3_select_value7 == "Yes" or bill3_select_value7 == "yes":
                                self.web.find_element(By.XPATH, self.ele.section3_option_3a_yes).click()
                                # 输入框  Identify the location.1
                                self.section_input_list("Identify the location.",self.ele.section3_option_3a_input,0)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_3a_no).click()
                        # 3.2.5 b
                        bill3_txt_8a = self.ele.get_div_describe(
                            "Does the product contain Capacitors with PCBs?")
                        bill3_text_8a = self.web.find_element(By.XPATH, bill3_txt_8a)
                        bill3_select_text8 = self.operate_excel.get_text_cols_data(bill3_text_8a.text)
                        bill3_select_value8 = self.operate_excel.get_value_cols_data(bill3_text_8a.text)
                        if bill3_select_value8:
                            if bill3_select_value8 == "Yes" or bill3_select_value8 == "yes":
                                self.web.find_element(By.XPATH, self.ele.section3_option_4a_yes).click()
                                # 输入框  Identify the location.2
                                self.section_input_list("Identify the location.", self.ele.section3_option_4a_input, 0)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_4a_no).click()

                        # 3.2.5 c
                        bill3_txt_9a = self.ele.get_div_describe(
                            "Does the product contain Capacitors with substances of concern")
                        bill3_text_9a = self.web.find_element(By.XPATH, bill3_txt_9a)
                        bill3_select_text9 = self.operate_excel.get_text_cols_data(bill3_text_9a.text)
                        bill3_select_value9 = self.operate_excel.get_value_cols_data(bill3_text_9a.text)
                        if bill3_text_9a.text and bill3_select_value9:
                            if bill3_select_value9 == "Yes" or bill3_select_value9 == "yes":
                                self.web.find_element(By.XPATH, self.ele.section3_option_5a_yes).click()
                                # 输入框  Identify the location.3.a
                                self.section_input_list("Identify the location.", self.ele.section3_option_5a_input1, 2)
                                # 输入框  Identify the location.3.b
                                self.section_input("Identify the electrolyte(s) for each capacitor meeting or exceeding this size limit.", self.ele.section3_option_5a_input2)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_5a_no).click()
                        # 3.2.5 d
                        bill3_txt_10a = self.ele.get_div_describe(
                            "Does the product contain Refractory ceramic fibers?")
                        bill3_text_10a = self.web.find_element(By.XPATH, bill3_txt_10a)
                        bill3_select_text10 = self.operate_excel.get_text_cols_data(bill3_text_10a.text)
                        bill3_select_value10 = self.operate_excel.get_value_cols_data(bill3_text_10a.text)
                        if bill3_text_10a.text and bill3_select_value10:
                            if bill3_select_value10 == "Yes" or bill3_select_value10 == "yes":
                                self.web.find_element(By.XPATH, self.ele.section3_option_6a_yes).click()
                                # 输入框  Identify the location.4
                                self.section_input_list("Identify the location.", self.ele.section3_option_6a_input, 3)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_6a_no).click()
                        # 3.2.5 e
                        bill3_txt_11a = self.ele.get_emc_describe(
                            "Does the product contain Gasses (CFCs, HFCs, HCFCs, HBFCs, carbon tetrachloride)?")
                        bill3_text_11a = self.web.find_element(By.XPATH, bill3_txt_11a)
                        bill3_select_text11 = self.operate_excel.get_text_cols_data(bill3_text_11a.text)
                        bill3_select_value11 = self.operate_excel.get_value_cols_data(bill3_text_11a.text)
                        if bill3_text_11a.text and bill3_select_value11:
                            if bill3_select_value11 == "Yes" or bill3_select_value11 == "yes":
                                self.web.find_element(By.XPATH, self.ele.section3_option_7a_yes).click()
                                # 输入框  Identify the location.4.1
                                self.section_input_list("Type of gas:", self.ele.section3_option_7a_input1, 1)
                                # 输入框  Identify the location.4.2
                                self.section_input_list("Properties:", self.ele.section3_option_7a_input2, 1)
                                # 输入框  Identify the location.4.3
                                self.section_input_list("Volume and/or weight:", self.ele.section3_option_7a_input3, 0)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_7a_no).click()
                        # 3.2.5 f
                        bill3_txt_12a = self.ele.get_emc_describe(
                            "Does the product contain any Liquids? If volume > 10 cl (or equivalence in weight, e.g. for PCB, oil)")
                        bill3_text_12a = self.web.find_element(By.XPATH, bill3_txt_12a)
                        bill3_select_text12 = self.operate_excel.get_text_cols_data(bill3_text_12a.text)
                        bill3_select_value12 = self.operate_excel.get_value_cols_data(bill3_text_12a.text)
                        if bill3_text_12a.text and bill3_select_value12:
                            if bill3_select_value12 == "Yes" or bill3_select_value12 == "yes":
                                self.web.find_element(By.XPATH, self.ele.section3_option_8a_yes).click()
                                # 输入框  Identify the location.f.1
                                self.section_input_list("Type of liquid:", self.ele.section3_option_8a_input1,1)
                                # 输入框  Identify the location.f.2
                                self.section_input_list("Discharge method:", self.ele.section3_option_8a_input2,1)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_8a_no).click()


                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_2a_no).click()


                # # 文本框输入内容
                # bill3_input1_txt = self.ele.get_div_describe(
                #     "Are there batteries contained in this product?")
                # bill3_input1_text = self.web.find_element(By.XPATH, bill3_input1_txt)
                # bill3_select_value15_text1 = self.operate_excel.get_value_cols_list(bill3_input1_text.text)[0]
                # if bill3_select_value15_text1:
                #     self.web.find_element(By.XPATH, self.ele.section3_option_4a_input).send_keys(
                #         bill3_select_value15_text1)
                # 3.2.6
                bill3_txt_13a = self.ele.get_emc_describe(
                    "Will WEEE labels be placed on this product?")
                bill3_text_13a = self.web.find_element(By.XPATH, bill3_txt_13a)
                bill3_select_text13 = self.operate_excel.get_text_cols_data(bill3_text_13a.text)
                bill3_select_value13 = self.operate_excel.get_value_cols_data(bill3_text_13a.text)
                self.web.driver.execute_script("arguments[0].scrollIntoView();", bill3_text_13a)
                if bill3_select_text13 in bill3_text_13a.text:
                    if bill3_select_value13 == "Yes" or bill3_select_value13 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_9a_yes).click()
                        # Reportable substances are defined in Corporate Standard C-S-1-9700-020. Use the
                        # Reportable Substances table below to document all of the substances identified in Corporate Standard.
                        self.section_span_select("Chemical / Substance",self.ele.section3_option_9a_select1)
                        # 输入框  CAS Number 1
                        self.section_input("CAS Number", self.ele.section3_option_9a_input2)
                        # 输入框  CAS Number 2
                        self.section_input("Reportable Quantity (g)", self.ele.section3_option_9a_input3)
                        # 输入框  CAS Number 3
                        self.section_input("Compound Used and Estimated Amount (specific units)", self.ele.section3_option_9a_input4)
                        # 输入框  CAS Number 4
                        self.section_input("Location in Product (specify part number if known)", self.ele.section3_option_9a_input5)
                        # 输入框  CAS Number 5
                        self.section_input("Part Number(s)", self.ele.section3_option_9a_input6)
                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_9a_no).click()

                # 3.3 Battery Information
                bill3_txt_14a = self.ele.get_div_describe(
                    "Are there batteries contained in this product?")
                bill3_text_14a = self.web.find_element(By.XPATH, bill3_txt_14a)
                bill3_select_text14 = self.operate_excel.get_text_cols_data(bill3_text_14a.text)
                bill3_select_value14 = self.operate_excel.get_value_cols_data(bill3_text_14a.text)
                if bill3_select_text14 in bill3_text_14a.text:
                    if bill3_select_value14 == "Yes" or bill3_select_value14 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_10a_yes).click()
                        # 后期写入
                        # self.web.find_element(By.XPATH, self.ele.section3_click_10a_but2).click()
                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_10a_no).click()

                # 3.4 Lasers
                bill3_txt_15a = self.ele.get_div_describe(
                    "Are there any lasers contained in this product?")
                bill3_text_15a = self.web.find_element(By.XPATH, bill3_txt_15a)
                bill3_select_text15 = self.operate_excel.get_text_cols_data(bill3_text_15a.text)
                bill3_select_value15 = self.operate_excel.get_value_cols_data(bill3_text_15a.text)
                if bill3_select_text15 in bill3_text_15a.text:
                    if bill3_select_value15 == "Yes" or bill3_select_value15 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_11a_yes).click()
                        #  Please indicate how you will provide the laser data. 选项
                        bill3_txt_34a = self.ele.get_emc_describe(
                            "Please indicate how you will provide the laser data.")
                        bill3_text_34a = self.web.find_element(By.XPATH, bill3_txt_34a)
                        bill3_select_text34 = self.operate_excel.get_text_cols_data(bill3_text_34a.text)
                        bill3_select_value34 = self.operate_excel.get_value_cols_data(bill3_text_34a.text)
                        if bill3_select_text34 in bill3_text_34a.text and bill3_select_value34:
                            if bill3_select_value34 == "Attachment":
                                self.web.find_element(By.XPATH, self.ele.section3_option_11a_Attachment).click()
                                # 上传 Please attach spreadsheet
                                self.updata_file("Please attach spreadsheet",self.ele.section3_option_11a_click_a)
                            else:
                                self.web.find_element(By.XPATH, self.ele.section3_option_11a_LaserTable).click()
                                # 表格输入
                                # 下拉选择项目 1
                                self.section_span_select("Laser Type",self.ele.section3_select_11a_1a)
                                # 下拉选择项目 2
                                self.section_span_select("Laser Media", self.ele.section3_select_11a_2a)
                                # 下拉选择项目 3
                                self.section_span_select("Laser Class", self.ele.section3_select_11a_3a)
                                # 下拉选择项目 1
                                self.section_input("FDA/CDRH Accession Number", self.ele.section3_input_11a_1a)

                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_11a_no).click()
                        # 文本框输入内容
                        bill3_input_txt2 = self.ele.get_div_describe(
                            "Please Comment on your selected answer")
                        bill3_input_text2 = self.web.find_element(By.XPATH, bill3_input_txt2)
                        bill3_select_value15_text2 = self.operate_excel.get_value_cols_list(bill3_input_text2.text)[0]
                        if bill3_select_value15_text2:
                            self.web.find_element(By.XPATH, self.ele.section3_option_11a_input).send_keys(bill3_select_value15_text2)
                            # 先取文本框内容

                # 3.5 Pressurized Parts
                bill3_txt_16a = self.ele.get_div_describe(
                    "Are there any pressurized, hydraulic accumulators or pneumatic parts contained in the product?")
                bill3_text_16a = self.web.find_element(By.XPATH, bill3_txt_16a)
                bill3_select_text16 = self.operate_excel.get_text_cols_data(bill3_text_16a.text)
                bill3_select_value16 = self.operate_excel.get_value_cols_data(bill3_text_16a.text)
                if bill3_select_text16 and bill3_select_value16:
                    if bill3_select_value16 == "Yes" or bill3_select_value16 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_12a_yes).click()
                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_12a_no).click()
                # 文本框输入内容
                bill3_input_txt3 = self.ele.get_div_describe(
                    "Please Comment on your selected answer.")
                bill3_input_text3 = self.web.find_element(By.XPATH, bill3_input_txt3)
                bill3_select_value15_text3 = self.operate_excel.get_value_cols_list(bill3_input_text3.text)[1]
                if bill3_select_value15_text3:
                    self.web.find_element(By.XPATH, self.ele.section3_option_12a_input).send_keys(
                        bill3_select_value15_text3)
                    if bill3_select_value16 == "Yes" or bill3_select_value16 == "yes":
                        self.section_input_list("Part Number", self.ele.section3_option_12a_list_1a,2)
                        self.section_input_list("Part Name", self.ele.section3_option_12a_list_2a, 0)


                # 3.6 Finishes
                bill3_txt_16a = self.ele.get_div_describe(
                    "Are there any parts utilizing a powder paint finish?")
                bill3_text_16a = self.web.find_element(By.XPATH, bill3_txt_16a)
                bill3_select_text16 = self.operate_excel.get_text_cols_data(bill3_text_16a.text)
                bill3_select_value16 = self.operate_excel.get_value_cols_data(bill3_text_16a.text)
                self.web.driver.execute_script("arguments[0].scrollIntoView();", bill3_text_16a)
                if bill3_select_text16 in bill3_text_16a.text:
                    if bill3_select_value16 == "Yes" or bill3_select_value16 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_13a_yes).click()
                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_13a_no).click()
                # 文本框输入内容
                bill3_input_txt4 = self.ele.get_div_describe(
                    "Please comment on your selected answer.")
                bill3_input_text4 = self.web.find_element(By.XPATH, bill3_input_txt4)
                bill3_select_value15_text4 = self.operate_excel.get_value_cols_list(bill3_input_text4.text)[2]
                if bill3_select_value15_text4:
                    self.web.find_element(By.XPATH, self.ele.section3_option_13a_input).click()
                    self.web.find_element(By.XPATH, self.ele.section3_option_13a_input).send_keys(
                        bill3_select_value15_text4)

                # 3.7 Finishes
                bill3_txt_17a = self.ele.get_div_describe(
                    "Does the product literature provide information to the customer about applicable programs for the return, reutilization, recycling or disposal of "
                    "batteries, supplies (e.g. toner cartridges), replaceable parts or the entire product?")
                bill3_text_17a = self.web.find_element(By.XPATH, bill3_txt_17a)
                bill3_select_text17 = self.operate_excel.get_text_cols_data(bill3_text_17a.text)
                bill3_select_value17 = self.operate_excel.get_value_cols_data(bill3_text_17a.text)
                self.web.driver.execute_script("arguments[0].scrollIntoView();", bill3_text_17a)
                if bill3_select_text17 in bill3_text_17a.text:
                    if bill3_select_value17 == "Yes" or bill3_select_value17 == "yes":
                        self.web.find_element(By.XPATH, self.ele.section3_option_14a_yes).click()
                    else:
                        self.web.find_element(By.XPATH, self.ele.section3_option_14a_no).click()
                # 文本框输入内容
                bill3_input_txt5 = self.ele.get_div_describe(
                    "Please comment on your selected answer.")
                bill3_input_text5 = self.web.find_element(By.XPATH, bill3_input_txt5)
                bill3_select_value15_text5 = self.operate_excel.get_value_cols_list(bill3_input_text5.text)[3]
                if bill3_select_value15_text5:
                    self.web.find_element(By.XPATH, self.ele.section3_option_14a_input).click()
                    self.web.find_element(By.XPATH, self.ele.section3_option_14a_input).send_keys(
                        bill3_select_value15_text5)
                # list parts
                if bill3_select_value17 == "Yes" or bill3_select_value17 == "yes":
                    self.section_input_list("Part Number", self.ele.section3_option_14a_list_1a, -1)
                    self.section_input_list("Part Name", self.ele.section3_option_14a_list_2a, -1)
                    self.section_input_list("Program", self.ele.section3_option_14a_list_3a, -1)

            if self.web.find_element(By.XPATH, self.ele.submit_completed_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()
                time.sleep(15)
                self.web.driver.close()
                print("填写完成，提交！")

    def perd_section4(self):
        # 读取excel文档，根据选中的section4，读取section4内容
        self.operate_excel = OperateExcel(self.file_path, 'Section 4')
        # self.operate_excel.get_sheet("Section 4")
        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section3状态
        time.sleep(10)
        section4_status = self.web.driver.find_element(By.XPATH,self.ele.setion4_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section4_status)
        if section4_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section4_status.get_attribute("value"):
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section4执行用例
            self.web.driver.find_element(By.XPATH,self.ele.section4_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 4.1 Field Use Material (FUM)
            field4_txt_radio = self.ele.get_emc_describe(
                "Are there any Field Use Material (FUM) chemical items that will be shipped with the product or")
            field4_text_radio = self.web.find_element(By.XPATH, field4_txt_radio)
            field4_select_text = self.operate_excel.get_text_cols_data(field4_text_radio.text)
            field4_select_value = self.operate_excel.get_value_cols_data(field4_text_radio.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", field4_text_radio)
            if field4_select_value:
                if field4_select_value == "Yes" or field4_select_value == "yes":
                    self.web.find_element(By.XPATH, self.ele.section4_option_1a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section4_option_1a_no).click()

                # 文本框输入内容
                field4_txt_radio1 = self.ele.get_emc_describe(
                    "Please comment on your selected answer.")
                field4_text_radio1 = self.web.find_element(By.XPATH, field4_txt_radio1)
                field4_select_value15_text1 = self.operate_excel.get_value_cols_list(field4_text_radio1.text)
                if field4_select_value15_text1[0]:
                    self.web.find_element(By.XPATH, self.ele.section4_option_input_1a).send_keys(
                        field4_select_value15_text1[0])
                # FUM  (ICDS: International Chemical Data System)
                if field4_select_value == "Yes" or field4_select_value == "yes":

                    self.section_input_list("Part Number", self.ele.section4_option_1a_list_1a, 0)
                    self.section_input_list("Part Name", self.ele.section4_option_1a_list_2a, 0)
                    self.section_input_list("ICDS Number", self.ele.section4_option_1a_list_3a, 0)
                    self.section_input_list("Method of use", self.ele.section4_option_1a_list_4a, 0)
                    self.section_input_list("Usage Rate (Specify Unit)", self.ele.section4_option_1a_list_5a, 0)
                    # 下拉选择项目 Shipped with product
                    self.section_span_select("Shipped with product", self.ele.section4_option_1a_select6)

            # 4.2 Additional Chemicals
            field4_txt_radio2 = self.ele.get_emc_describe(
                "Are there any additional chemicals that are specified for use with the")
            field4_text_radio2 = self.web.find_element(By.XPATH, field4_txt_radio2)
            field4_select_text2 = self.operate_excel.get_text_cols_data(field4_text_radio2.text)
            field4_select_value2 = self.operate_excel.get_value_cols_data(field4_text_radio2.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", field4_text_radio2)
            if field4_select_value2:
                if field4_select_value2 == "Yes" or field4_select_value2 == "yes":
                    self.web.find_element(By.XPATH, self.ele.section4_option_2a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section4_option_2a_no).click()
            # 文本框输入内容
            field4_input_txt2 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            field4_input_text2 = self.web.find_element(By.XPATH, field4_input_txt2)
            field4_select_value_text2 = self.operate_excel.get_value_cols_list(field4_input_text2.text)
            if field4_select_value_text2[1]:
                self.web.find_element(By.XPATH, self.ele.section4_option_2a_input).send_keys(
                    field4_select_value_text2[1])

            # Additional Chemicals
            if field4_select_value2 == "Yes" or field4_select_value2 == "yes":
                self.section_input_list("Chemical Name", self.ele.section4_option_2a_list_1a, 0)
                self.section_input_list("Method of use", self.ele.section4_option_2a_list_2a, 1)
                self.section_input_list("Usage Rate (Specific Unit)", self.ele.section4_option_2a_list_3a, 0)


            # 4.3 Chemical Waste
            field4_txt_radio3 = self.ele.get_div_describe(
                "Does the product produce chemical waste during normal operation and maintenance?")
            field4_text_radio3 = self.web.find_element(By.XPATH, field4_txt_radio3)
            field4_select_text3 = self.operate_excel.get_text_cols_data(field4_text_radio3.text)
            field4_select_value3 = self.operate_excel.get_value_cols_data(field4_text_radio3.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", field4_text_radio3)
            if field4_select_text3 in field4_text_radio3.text and field4_select_value3:
                if field4_select_value3 == "Yes" or field4_select_value3 == "yes":
                    self.web.find_element(By.XPATH, self.ele.section4_option_3a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section4_option_3a_no).click()
            # 文本框输入内容
            field4_input_txt3 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            field4_input_text3 = self.web.find_element(By.XPATH, field4_input_txt3)
            field4_select_value_text3 = self.operate_excel.get_value_cols_list(field4_input_text3.text)
            if field4_select_value_text3[2]:
                self.web.find_element(By.XPATH, self.ele.section4_option_3a_input).send_keys(
                    field4_select_value_text3[2])
            # Waste Type
            if field4_select_value3 == "Yes" or field4_select_value3 == "yes":
                self.section_input_list("Waste Type", self.ele.section4_option_3a_list_1a, 0)

            # 4.4 Packaging Information
            field4_create_packaging = self.ele.get_input_but("Create Geo Packaging")
            field4_create_packaging_but = self.web.find(By.XPATH, field4_create_packaging)
            if field4_create_packaging_but:
                self.web.find_element(By.XPATH, field4_create_packaging).click()
                self.web.find_element(By.XPATH,self.ele.get_input_but("OK")).click()
                self.web.find_element(By.XPATH, self.ele.get_input_but("Refresh Geo Packaging")).click()
                time.sleep(60)
                self.web.driver.refresh()
            # 4.4,1 click1
            if self.web.find_element(By.XPATH, self.ele.section4_option_4a_status_1).get_attribute("value") == "New":
                self.web.find_element(By.XPATH, self.ele.section4_option_4a_1a).click()
                # 进行编辑packaging
                # self.section4_packaging("1200x1000mm栈板", self.ele.section4_option_4a_1a)
                try:
                    self.section4_packaging("1200x1000mm栈板", self.ele.section4_option_4a_1a)
                except Exception as e:
                    # 将错误信息打印到控制台
                    print(f"程序执行出错：{e}")
                    self.web.driver.close()

            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 4.4,2 click2
            if self.web.find_element(By.XPATH, self.ele.section4_option_4a_status_2).get_attribute("value") == "New":
                self.web.find_element(By.XPATH, self.ele.section4_option_4a_2a).click()
                # 进行编辑packaging
                try:
                    self.section4_packaging("1200x800mm栈板",self.ele.section4_option_4a_2a)
                except Exception as e:
                    # 将错误信息打印到控制台
                    print(f"程序执行出错：{e}")
                    self.web.driver.close()

            # 包装数据填写完成提交后，点击刷新一下状态
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            time.sleep(20)
            self.web.driver.refresh()
            if self.web.find(By.XPATH, self.ele.section4_refresh_packaging_input_but):
                self.web.find_element(By.XPATH, self.ele.section4_refresh_packaging_input_but).click()
            time.sleep(20)
            if self.web.find_element(By.XPATH, self.ele.submit_completed_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()
                time.sleep(15)
                print("填写完成，提交！")
                self.web.driver.close()



    def perd_section5(self):
        # 读取excel文档，根据选中的section5，读取section5内容
        self.operate_excel = OperateExcel(self.file_path, 'Section 5')
        # self.operate_excel.get_sheet("Section 5")
        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section3状态
        time.sleep(10)
        section5_status = self.web.driver.find_element(By.XPATH,self.ele.setion5_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section5_status)
        if section5_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section5_status.get_attribute("value"):
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section5执行用例
            self.web.driver.find_element(By.XPATH,self.ele.section5_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 5.1 Product Features
            perd_txt_radio1 = self.ele.get_div_describe(
                "Does this product contain any energy efficiency or savings features (both hardware and software)?")
            perd_text_radio1 = self.web.find_element(By.XPATH, perd_txt_radio1)
            perd_select_text1 = self.operate_excel.get_text_cols_data(perd_text_radio1.text)
            perd_select_value1 = self.operate_excel.get_value_cols_data(perd_text_radio1.text)
            if perd_select_value1:
                if perd_select_value1 == "Yes" or "Yes" in perd_select_value1:
                    self.web.find_element(By.XPATH, self.ele.section5_option_1a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_1a_no).click()
            # 文本框输入内容
            perd_input_txt1 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text1 = self.web.find_elements(By.XPATH, perd_input_txt1)[0]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text1)
            perd_select_value_text1 = self.operate_excel.get_value_cols_list(perd_input_text1.text)[0]
            if perd_select_value_text1:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_1a).send_keys(
                    perd_select_value_text1)

            # 5.2 Energy Controls
            perd_txt_radio2 = self.ele.get_div_describe(
                "Are all energy savings controls or settings fully described in the product user manual?")
            perd_text_radio2 = self.web.find_element(By.XPATH, perd_txt_radio2)
            perd_select_text2 = self.operate_excel.get_text_cols_data(perd_text_radio2.text)
            perd_select_value2 = self.operate_excel.get_value_cols_data(perd_text_radio2.text)
            if perd_select_text2 in perd_text_radio2.text:
                if perd_select_value2 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section5_option_2a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_2a_no).click()
            # 文本框输入内容
            perd_input_txt2 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text2 = self.web.find_elements(By.XPATH, perd_input_txt2)[1]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text2)
            perd_select_value_text2 = self.operate_excel.get_value_cols_list(perd_input_text2.text)[1]
            if perd_select_value_text2:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_2a).send_keys(
                    perd_select_value_text2)

            # 5.3 Product Disposal
            perd_txt_radio3 = self.ele.get_div_describe(
                "Are all hazardous parts and components requiring special disposal identified in the product literature?")
            perd_text_radio3 = self.web.find_element(By.XPATH, perd_txt_radio3)
            perd_select_text3 = self.operate_excel.get_text_cols_data(perd_text_radio3.text)
            perd_select_value3 = self.operate_excel.get_value_cols_data(perd_text_radio3.text)
            if perd_select_text3 in perd_text_radio3.text:
                if perd_select_value3 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section5_option_3a_yes).click()
                elif perd_select_value3 == "No":
                    self.web.find_element(By.XPATH, self.ele.section5_option_3a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_3a_no_parts).click()
            # 文本框输入内容
            perd_input_txt3 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text3 = self.web.find_elements(By.XPATH, perd_input_txt3)[2]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text3)
            perd_select_value_text3 = self.operate_excel.get_value_cols_list(perd_input_text3.text)[2]
            if perd_select_value_text3:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_3a).send_keys(
                    perd_select_value_text3)

            # 5.4 Common Parts
            perd_txt_radio4 = self.ele.get_emc_describe(
                "Does product have common mechanical packages (such as covers and chassis) or common parts or components that are used for multiple models in the product "
                "family in multiple generations of the same product, allowing the reuse of common parts (excluding screws or fasteners)")
            perd_text_radio4 = self.web.find_element(By.XPATH, perd_txt_radio4)
            perd_select_text4 = self.operate_excel.get_text_cols_data(perd_text_radio4.text)
            perd_select_value4 = self.operate_excel.get_value_cols_data(perd_text_radio4.text)
            if perd_select_value4:
                if perd_select_value4 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section5_option_4a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_4a_no).click()
            # 文本框输入内容
            perd_input_txt4 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text4 = self.web.find_elements(By.XPATH, perd_input_txt4)[3]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text4)
            perd_select_value_text4 = self.operate_excel.get_value_cols_list(perd_input_text4.text)[3]
            if perd_select_value_text4:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_4a).send_keys(
                    perd_select_value_text4)

            # 5.5 Product Documentation
            perd_txt_radio5 = self.ele.get_div_describe(
                "Select any environmental attributes that apply to the product documentation/manuals.")
            perd_text_radio5 = self.web.find_element(By.XPATH, perd_txt_radio5)
            perd_select_text5 = self.operate_excel.get_text_cols_data(perd_text_radio5.text)
            perd_select_value5 = self.operate_excel.get_value_cols_data(perd_text_radio5.text)
            if perd_select_text5 and perd_select_value5:
                perd_list = perd_select_value5.split(',')
                for i in perd_list:
                    print(self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_7b).is_selected())
                    if self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_7b).is_selected() == True:
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_7b).click()
                    if i == "a":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_1b).click()
                    elif i == "b":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_2b).click()
                        # 输入文本
                        self.section_input("Specify which component contains recycled material and recycled content:",self.ele.section5_textarea_5a_input1)
                    elif i == "c":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_3b).click()
                    elif i == "d":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_4b).click()
                    elif i == "e":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_5b).click()
                    elif i == "f":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_6b).click()
                        # 输入文本
                        self.section_input("Other, please describe:",
                                           self.ele.section5_textarea_5a_input2)
                    else:
                        if self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_7b).is_selected() == False:
                            self.web.find_element(By.XPATH, self.ele.section5_checkbox_5a_7b).click()
            # # 文本框输入内容
            # perd_input_txt5 = self.ele.get_div_describe(
            #     "Please comment on your selected answer")
            # perd_input_text5 = self.web.find_element(By.XPATH, perd_input_txt5)
            # perd_select_value_text5 = self.operate_excel.get_value_cols_list(perd_input_text5.text)[3]
            # if perd_select_value_text5:
            #     self.web.find_element(By.XPATH, self.ele.section5_design_input_4a).send_keys(
            #         perd_select_value_text5)

            # 5.6 Product Documentation
            perd_txt_radio6 = self.ele.get_div_describe(
                "Select any product feature which promotes upgradeability and expandability and then fill in the appropriate information below.")
            perd_text_radio6 = self.web.find_element(By.XPATH, perd_txt_radio6)
            perd_select_text6 = self.operate_excel.get_text_cols_data(perd_text_radio6.text)
            perd_select_value6 = self.operate_excel.get_value_cols_data(perd_text_radio6.text)
            if perd_select_text6 and perd_select_value6:
                perd_list = perd_select_value6.split(',')
                print("perd_list:::",perd_list)
                for i in perd_list:
                    print(i)
                    if self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_9b).is_selected() == True:
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_9b).click()

                    if i == "a":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_1b).click()
                        # 输入文本
                        self.section_input("Enter the amount of memory in MB:",
                                           self.ele.section5_text_6a_input1_1a)
                    elif i == "b":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_2b).click()
                    elif i == "c":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_3b).click()
                        # 输入文本
                        self.section_lists("Enter the products total number of card slots / products total number of card slots that are available:",
                                           self.ele.section5_text_6a_input2_2c1,0)
                        # 输入文本
                        self.section_lists("Enter the products total number of card slots / products total number of card slots that are available:",
                                           self.ele.section5_text_6a_input2_2c2,1)
                    elif i == "d":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_4b).click()
                        # 输入文本
                        self.section_lists(
                            "Enter the products total number of bays / products total number of bays that are available:",
                            self.ele.section5_text_6a_input3_3d1, 0)
                        # 输入文本
                        self.section_lists(
                            "Enter the products total number of bays / products total number of bays that are available:",
                            self.ele.section5_text_6a_input3_3d2, 1)
                    elif i == "e":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_5b).click()
                        # 输入文本
                        self.section_input("Enter the HDD size in GB:",
                                           self.ele.section5_text_6a_input4_4e)
                    elif i == "f":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_6b).click()
                        # 输入文本
                        self.section_input("Enter the HDD size in GB:",
                                           self.ele.section5_text_6a_input5_5f)
                    elif i == "g":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_7b).click()
                    elif i == "h":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_8b).click()
                        # 输入文本
                        self.section_input("Enter the HDD size in GB:",
                                           self.ele.section5_text_6a_input6_6h)
                    else:
                        if self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_9b).is_selected() == False:
                            self.web.find_element(By.XPATH, self.ele.section5_checkbox_6a_9b).click()
            perd_txt_radio6 = self.ele.get_div_describe(
                "Can system be easily upgraded by customer? (i.e., no special tools required.)")
            perd_text_radio6 = self.web.find_element(By.XPATH, perd_txt_radio6)
            perd_select_text6 = self.operate_excel.get_text_cols_data(perd_text_radio6.text)
            perd_select_value6 = self.operate_excel.get_value_cols_data(perd_text_radio6.text)
            if perd_select_text6 in perd_text_radio6.text and perd_select_value6:
                if perd_select_value6 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section5_option_6a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_6a_no).click()
            # 文本框输入内容
            perd_input_txt6 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text6 = self.web.find_elements(By.XPATH, perd_input_txt6)[4]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text6)
            perd_select_value_text6 = self.operate_excel.get_value_cols_list(perd_input_text6.text)[4]
            if perd_select_value_text6:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_6a).send_keys(
                    perd_select_value_text6)

            # 5.7 Ease of Repair
            perd_txt_radio7 = self.ele.get_div_describe(
                "Select all product features which promote ease of repair or longer product life.")
            perd_text_radio7 = self.web.find_element(By.XPATH, perd_txt_radio7)
            perd_select_text7 = self.operate_excel.get_text_cols_data(perd_text_radio7.text)
            perd_select_value7 = self.operate_excel.get_value_cols_data(perd_text_radio7.text)
            if perd_select_text7 in perd_text_radio7.text:
                perd_list = perd_select_value7.split(',')
                for i in perd_list:
                    if self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_5b).is_selected() == True:
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_5b).click()

                    if i == "a":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_1b).click()
                    elif i == "b":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_2b).click()
                    elif i == "c":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_3b).click()
                    elif i == "d":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_4b).click()
                        # 输入文本
                        self.section_input("Other, please describe:",
                                           self.ele.section5_text_7a_input1_d)
                    else:
                        if self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_5b).is_selected() == False:
                            self.web.find_element(By.XPATH, self.ele.section5_checkbox_7a_5b).click()
            # 5.8 Plastic Parts
            perd_txt_radio8 = self.ele.get_div_describe(
                "Is the same plastic type used for all plastic parts 25 grams or greater?")
            perd_text_radio8 = self.web.find_element(By.XPATH, perd_txt_radio8)
            perd_select_text8 = self.operate_excel.get_text_cols_data(perd_text_radio8.text)
            perd_select_value8 = self.operate_excel.get_value_cols_data(perd_text_radio8.text)
            if perd_select_value8:
                if perd_select_value8 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section5_option_8a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_8a_no).click()
            # 文本框输入内容
            perd_input_txt8 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text8 = self.web.find_elements(By.XPATH, perd_input_txt8)[5]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text8)
            perd_select_value_text8 = self.operate_excel.get_value_cols_list(perd_input_text8.text)[5]
            if perd_select_value_text8:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_8a).send_keys(
                    perd_select_value_text8)

            # 5.9 Recycled Content
            perd_txt_radio9 = self.ele.get_div_describe(
                "Does this product contain plastic parts that contain recycled content?")
            perd_text_radio9 = self.web.find_element(By.XPATH, perd_txt_radio9)
            perd_select_text9 = self.operate_excel.get_text_cols_data(perd_text_radio9.text)
            perd_select_value9 = self.operate_excel.get_value_cols_data(perd_text_radio9.text)
            if perd_select_text9 in perd_text_radio9.text:
                if perd_select_value9 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section5_option_9a_yes).click()
                    # 隐藏 Enter Product total PCC recycled plastic percentage %

                    # 输入文本 1.input
                    txt9_input = self.ele.get_div_describe("Enter Product total PCC recycled plastic percentage")
                    text9_input = self.web.find_element(By.XPATH, txt9_input)
                    input9_text_cols = self.operate_excel.get_text_cols_data(text9_input.text)
                    input9_text_cols_value = self.operate_excel.get_value_cols_data(text9_input.text) * 100  # 转化百分比
                    if input9_text_cols_value:
                        self.web.find_element(By.XPATH, self.ele.section5_design_input1_9a).click()
                        self.web.find_element(By.XPATH, self.ele.section5_design_input1_9a).send_keys(input9_text_cols_value)  # w
                    # List information for those plastic parts identified as containing recycled content.
                    # 填表
                    # 输入框  CAS Number 1
                    self.section_input("Part Name", self.ele.section5_design_textarea_1a)
                    # 输入框  CAS Number 2
                    self.section_input_text("PCC Material Name", self.ele.section5_design_textarea_2a)
                    # 输入框  CAS Number 3
                    self.section_input_text("PCC Supplier Name",
                                       self.ele.section5_design_textarea_3a)
                    # 输入框  CAS Number 4
                    self.section_input("Weight of plastics (g)",
                                       self.ele.section5_design_textarea_4a)
                    # 输入框  CAS Number 5
                    self.section_input("Weight of PCC (g)",
                                       self.ele.section5_design_textarea_5a)
                else:
                    self.web.find_element(By.XPATH, self.ele.section5_option_9a_no).click()

            # 文本框输入内容
            perd_input_txt9 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text9 = self.web.find_elements(By.XPATH, perd_input_txt9)[6]
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text9)
            perd_select_value_text9 = self.operate_excel.get_value_cols_list(perd_input_text9.text)[6]
            if perd_select_value_text9:
                self.web.find_element(By.XPATH, self.ele.section5_design_input_9a).send_keys(
                    perd_select_value_text9)

            # 5.10 Recycling Efforts
            # 文本框输入内容 1.
            perd_input_txt10_1a = self.ele.get_div_describe(
                "Cite any and all efforts to increase the usage of recyclable materials used in this product.")
            perd_input_text10_1a = self.web.find_element(By.XPATH, perd_input_txt10_1a)
            perd_select_text10_1a = self.operate_excel.get_text_cols_data(perd_input_text10_1a.text)
            perd_select_value10_1a = self.operate_excel.get_value_cols_data(perd_input_text10_1a.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", perd_input_text10_1a)
            if perd_select_text10_1a in perd_input_text10_1a.text:
                if perd_select_value10_1a:
                    self.web.find_element(By.XPATH, self.ele.section5_design_input1_10a).click()
                    self.web.find_element(By.XPATH, self.ele.section5_design_input1_10a).send_keys(
                        perd_select_value10_1a)
            # 文本框输入内容 2.
            perd_input_txt10_2a = self.ele.get_div_describe(
                "Cite all effort to design this product for recycling and provide future plans for improving the design for recycling.")
            perd_input_text10_2a = self.web.find_element(By.XPATH, perd_input_txt10_2a)
            perd_select_text10_2a = self.operate_excel.get_text_cols_data(perd_input_text10_2a.text)
            perd_select_value10_2a = self.operate_excel.get_value_cols_data(perd_input_text10_2a.text)
            if perd_select_text10_2a in perd_input_text10_2a.text:
                if perd_select_value10_2a:
                    self.web.find_element(By.XPATH, self.ele.section5_design_input2_10a).click()
                    self.web.find_element(By.XPATH, self.ele.section5_design_input2_10a).send_keys(
                        perd_select_value10_2a)

            # 5.11 Printer Features
            perd_txt_radio11 = self.ele.get_div_describe(
                "For printer(s), select any environmental design features to reduce consumables.")
            perd_text_radio11 = self.web.find_element(By.XPATH, perd_txt_radio11)
            perd_select_text11 = self.operate_excel.get_text_cols_data(perd_text_radio11.text)
            perd_select_value11 = self.operate_excel.get_value_cols_data(perd_text_radio11.text)
            if perd_select_text11 in perd_text_radio11.text:
                perd_list = perd_select_value11.split(',')
                for i in perd_list:
                    if self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_4b).is_selected() == True:
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_4b).click()

                    if i == "a":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_1b).click()
                    elif i == "b":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_2b).click()
                        # 输入文本
                        self.section_input("Describe design features:",
                                           self.ele.section5_textarea_11a_1b)
                    elif i == "c":
                        self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_3b).click()
                        # 输入文本
                        self.section_input("Other, please describe:",
                                           self.ele.section5_textarea_11a_2c)
                    else:
                        if self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_4b).is_selected() == False:
                            self.web.find_element(By.XPATH, self.ele.section5_checkbox_11a_4b).click()

            if self.web.find_element(By.XPATH, self.ele.submit_completed_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()
                time.sleep(15)
                self.web.driver.close()
                print("填写完成，提交！")


    def perd_section6(self):
        # 读取excel文档，根据选中的section6，读取section6内容
        self.operate_excel = OperateExcel(self.file_path, 'Section 6')
        # self.operate_excel.get_sheet("Section6")
        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section6状态
        time.sleep(10)
        section6_status = self.web.driver.find_element(By.XPATH, self.ele.setion6_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section6_status)
        if section6_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section6_status.get_attribute("value"):
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section6执行用例
            self.web.driver.find_element(By.XPATH, self.ele.section6_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 6.1 Chemical Emissions
            emiss_txt_radio1 = self.ele.get_emc_describe(
                "Has the product or product family been tested to determine chemical emissions per the requirements of National Bulletin N-B 3-0527-050?")
            emiss_text_radio1 = self.web.find_element(By.XPATH, emiss_txt_radio1)
            emiss_select_text1 = self.operate_excel.get_text_cols_data(emiss_text_radio1.text)
            emiss_select_value1 = self.operate_excel.get_value_cols_data(emiss_text_radio1.text)
            if emiss_select_text1 in emiss_text_radio1.text:
                if emiss_select_value1 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section6_option_1a_yes).click()
                    # 上传文件
                    self.updata_file("Attach the Test Report",self.ele.section6_updata_1a_a)

                elif emiss_select_value1 == "No":
                    self.web.find_element(By.XPATH, self.ele.section6_option_1a_no).click()
                    # 单选按钮
                    emiss_txt_radio1a = self.ele.get_emc_describe(
                        "If No, has a letter of substantial equivalency been issued for this product indicating that testing is not required?")
                    emiss_text_radio1a = self.web.find_element(By.XPATH, emiss_txt_radio1a)
                    emiss_select_text1a = self.operate_excel.get_text_cols_data(emiss_text_radio1a.text)
                    emiss_select_value1a = self.operate_excel.get_value_cols_data(emiss_text_radio1a.text)
                    if emiss_select_text1a in emiss_text_radio1a.text:
                        if emiss_select_value1a == "Yes":
                            self.web.find_element(By.XPATH, self.ele.section6_option_1a_letter_yes).click()
                            # 上传附加文件
                            self.updata_file("Attach the substantial equivalency letter",self.ele.section6_letter_updata_1a)
                        else:
                            self.web.find_element(By.XPATH, self.ele.section6_option_1a_letter_no).click()

                else:
                    self.web.find_element(By.XPATH, self.ele.section6_option_1a_not).click()
            # 文本框输入内容
            perd_input_txt1 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            perd_input_text1 = self.web.find_element(By.XPATH, perd_input_txt1)
            perd_select_value_text1 = self.operate_excel.get_value_cols_list(perd_input_text1.text)[0]
            if perd_select_value_text1:
                self.web.find_element(By.XPATH, self.ele.section6_emiss_input_1a).send_keys(
                    perd_select_value_text1)

            # 6.2 Acoustical Standards
            emiss_txt_radio2 = self.ele.get_emc_describe(
                'Does this product comply with the Lenovo acoustical standards as listed in C-S 1-1710-006')
            emiss_text_radio2 = self.web.find_element(By.XPATH, emiss_txt_radio2)
            emiss_select_text2 = self.operate_excel.get_text_cols_data(emiss_text_radio2.text)
            emiss_select_value2 = self.operate_excel.get_value_cols_data(emiss_text_radio2.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", emiss_text_radio2)
            if emiss_select_text2 and emiss_select_value2:
                if emiss_select_value2 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section6_option_2a_yes).click()
                    # 6.2.1 Attach Acoustic Test Report.
                    self.updata_file("Attach Acoustic Test Report.", self.ele.section6_option_2a_updata_a)
                    # 文本框输入内容
                    perd_input_txt2a = self.ele.get_div_describe(
                        "Please comment on your selected answer")
                    perd_input_text2a = self.web.find_element(By.XPATH, perd_input_txt2a)
                    perd_select_value_text2a = self.operate_excel.get_value_cols_list(perd_input_text2a.text)[1]
                    if perd_select_value_text2a:
                        self.web.find_element(By.XPATH, self.ele.section6_emiss_input_2a).send_keys(
                            perd_select_value_text2a)
                elif emiss_select_value1 == "No":
                    self.web.find_element(By.XPATH, self.ele.section6_option_2a_no).click()
                    self.web.find_element(By.XPATH, self.ele.section6_option_2a_yes).click()
                    # 6.2.1 Attach Acoustic Test Report.
                    self.updata_file("Attach Acoustic Test Report.", self.ele.section6_option_2a_updata_a)
                    # 文本框输入内容
                    perd_input_txt2a = self.ele.get_div_describe(
                        "Please comment on your selected answer")
                    perd_input_text2a = self.web.find_element(By.XPATH, perd_input_txt2a)
                    perd_select_value_text2a = self.operate_excel.get_value_cols_list(perd_input_text2a.text)[1]
                    if perd_select_value_text2a:
                        self.web.find_element(By.XPATH, self.ele.section6_emiss_input_2a).send_keys(
                            perd_select_value_text2a)
                else:
                    self.web.find_element(By.XPATH, self.ele.section6_option_2a_not).click()

            # 6.2.2
            emiss_txt_radio22 = self.ele.get_emc_describe(
                "Is there measureable noise generated by this product?")
            emiss_text_radio22 = self.web.find_element(By.XPATH, emiss_txt_radio22)
            emiss_select_text22 = self.operate_excel.get_text_cols_data(emiss_text_radio22.text)
            emiss_select_value22 = self.operate_excel.get_value_cols_data(emiss_text_radio22.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", emiss_text_radio22)
            if emiss_select_text22 in emiss_text_radio22.text:
                print("emiss_select_value1:::", emiss_select_value1)
                if emiss_select_value22 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section6_option_3a_yes).click()
                    # 表格 Acoustic Product Levels
                    self.section_input_num("Operating Mode",self.ele.section6_levels_input_1a,2)
                    self.section_input_num("Operating Mode", self.ele.section6_levels_input_2a,3)
                    self.section_input_num("Idle Mode", self.ele.section6_levels_input_3a,2)
                    self.section_input_num("Idle Mode", self.ele.section6_levels_input_4a,3)

                elif emiss_select_value22 == "No":
                    self.web.find_element(By.XPATH, self.ele.section6_option_3a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section6_option_3a_not).click()

            # 文本框输入内容
            perd_input_txt2 = self.ele.get_div_describe(
                "Please comment on your selected answer")
            perd_input_text2 = self.web.find_element(By.XPATH, perd_input_txt2)
            perd_select_value_text2 = self.operate_excel.get_value_cols_list(perd_input_text2.text)[1]
            if perd_select_value_text2:
                self.web.find_element(By.XPATH, self.ele.section6_emiss_input_3a).send_keys(
                    perd_select_value_text2)

            if self.web.find_element(By.XPATH, self.ele.submit_completed_but):
                # 填写完后，点击提交按钮
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()
                time.sleep(15)
                self.web.driver.close()
                print("填写完成，提交！")

    def perd_section7(self):
        # 读取excel文档，根据选中的section7，读取section7内容
        self.operate_excel = OperateExcel(self.file_path, 'Section 7')
        # self.operate_excel.get_sheet("Section7")
        # 启动浏览器
        # self.web.open_web(self.read_conf.web_url)
        all_handles = self.web.driver.window_handles
        self.web.driver.switch_to.window(all_handles[-1])
        # 检查项目的section6状态
        time.sleep(10)
        section7_status = self.web.driver.find_element(By.XPATH, self.ele.setion7_status)
        self.web.driver.execute_script("arguments[0].scrollIntoView(false);", section7_status)
        if section7_status.get_attribute("value") == "In Progress" or "Rejected by PERD" in section7_status.get_attribute("value"):
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 进入section7执行用例
            self.web.driver.find_element(By.XPATH, self.ele.section7_click_but).click()
            self.web.driver.implicitly_wait(5)
            # 切换到最后一个标签页刷新界面
            win = self.web.driver.current_window_handle
            print(win)
            all_handles = self.web.driver.window_handles
            self.web.driver.switch_to.window(all_handles[-1])
            # 刷新当前页面
            self.web.driver.refresh()
            # 7.1 Environmentally Conscious Design
            conscious_txt_radio1 = self.ele.get_emc_describe(
                '"Environmentally Conscious Design", and all of the applicable Lenovo Standards and Bulletins detailed in the standards?')
            conscious_text_radio1 = self.web.find_element(By.XPATH, conscious_txt_radio1)
            conscious_select_text1 = self.operate_excel.get_text_cols_data(conscious_text_radio1.text)
            conscious_select_value1 = self.operate_excel.get_value_cols_data(conscious_text_radio1.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", conscious_text_radio1)
            if conscious_select_text1 and conscious_select_value1:
                if conscious_select_value1 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section7_option_1a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section7_option_1a_no).click()
            # 文本框输入内容
            conscious_input_txt1 = self.ele.get_div_describe(
                "Please comment on your selected answer")
            conscious_input_text1 = self.web.find_element(By.XPATH, conscious_input_txt1)
            conscious_select_value_text1 = self.operate_excel.get_value_cols_list(conscious_input_text1.text)[0]
            if conscious_select_value_text1:
                self.web.find_element(By.XPATH, self.ele.section7_conscious_input_1a).send_keys(
                    conscious_select_value_text1)

            # 7.2 Prohibited Substances
            conscious_txt_radio2 = self.ele.get_emc_describe(
                'The substances listed below are prohibited from use in any Lenovo Product. Please check any of these substances if they are present in this product. If none of '
                'these substances are present, please select "None" and then provide the method(s) used to verify absence of these substances.')
            conscious_text_radio2 = self.web.find_element(By.XPATH, conscious_txt_radio2)
            conscious_select_text2 = self.operate_excel.get_text_cols_data(conscious_text_radio2.text)
            conscious_select_value2 = self.operate_excel.get_value_cols_data(conscious_text_radio2.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", conscious_text_radio2)
            if conscious_select_value2:

                perd_list = conscious_select_value2.split(',')
                for i in perd_list:
                    if self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_15b).is_selected() == True:
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_15b).click()

                    if i == "a":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_1b).click()
                    elif i == "b":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_2b).click()
                    elif i == "c":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_3b).click()
                    elif i == "d":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_4b).click()
                    elif i == "e":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_5b).click()
                    elif i == "f":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_6b).click()
                    elif i == "g":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_7b).click()
                    elif i == "h":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_8b).click()
                    elif i == "i":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_9b).click()
                    elif i == "j":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_10b).click()
                    elif i == "k":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_11b).click()
                    elif i == "l":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_12b).click()
                    elif i == "m":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_13b).click()
                    elif i == "n":
                        self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_14b).click()
                    else:
                        if self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_15b).is_selected() == False:
                            self.web.find_element(By.XPATH, self.ele.section7_checkbox_2a_15b).click()
                            # 7.2.0 Provide the method used to verify absence of these substances.
                            conscious_txt_radio3 = self.ele.get_emc_describe(
                                'Provide the method used to verify absence of these substances.')
                            conscious_text_radio3 = self.web.find_element(By.XPATH, conscious_txt_radio3)
                            conscious_select_text3 = self.operate_excel.get_value_cols_list(conscious_text_radio3.text)[1]
                            conscious_select_value3 = self.operate_excel.get_value_cols_list(conscious_text_radio3.text)[1]
                            self.web.driver.execute_script("arguments[0].scrollIntoView();", conscious_text_radio3)
                            if conscious_select_text3 and conscious_select_value3:
                                self.web.find_element(By.XPATH, self.ele.section7_select_2a).click()
                                conscious_text_radio3.click()
                                section1_select = self.web.find_element(By.XPATH, self.ele.section7_select_2a)

                                Select(section1_select).select_by_value(conscious_select_value3)
            # 文本框输入内容
            conscious_input_txt3 = self.ele.get_emc_describe(
                "Please provide part number(s) and location(s) of where any of the substances may reside in the product.")
            conscious_input_text3 = self.web.find_element(By.XPATH, conscious_input_txt3)
            conscious_select_value_text3 = self.operate_excel.get_value_cols_data(conscious_input_text3.text)
            if conscious_select_value_text3:
                self.web.find_element(By.XPATH, self.ele.section7_conscious_input_2a).send_keys(
                    conscious_select_value_text3)
            # 7.2.0 Systems?
            conscious_txt_radio4 = self.ele.get_emc_describe(
                'Does the product contain ODM Systems?')
            conscious_text_radio4 = self.web.find_element(By.XPATH, conscious_txt_radio4)
            conscious_select_text4 = self.operate_excel.get_text_cols_data(conscious_text_radio4.text)
            conscious_select_value4 = self.operate_excel.get_value_cols_data(conscious_text_radio4.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", conscious_text_radio4)
            if conscious_select_text4 and conscious_select_value4:
                self.web.find_element(By.XPATH, self.ele.section7_option_2a_no).click()
                if conscious_select_value4 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section7_option_2a_yes).click()
                    # 7.2.2
                    conscious_input_2a = self.ele.get_emc_describe(
                        "Attach 1752 supplier material declarations (ODM Systems).")
                    conscious_input_2a = self.web.find_element(By.XPATH, conscious_input_2a)
                    conscious_input_text2 = self.operate_excel.get_text_cols_data(conscious_input_2a.text)
                    conscious_input_value2 = self.operate_excel.get_value_cols_data(conscious_input_2a.text)
                    if conscious_input_text2 and conscious_input_value2:
                        if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_1a).text.find(
                                conscious_input_value2) != -1:
                            print("已上传过了！")
                        else:
                            # 点击附件文件按钮
                            conscious_buttom_2a = self.web.find_element(By.XPATH, self.ele.section7_conscious_click_1a)
                            conscious_buttom_2a.click()
                            # 选择文件
                            xuan_file = self.web.find_element(By.XPATH, self.ele.select_file)
                            ActionChains(self.web.driver).move_to_element(xuan_file).click().perform()

                            time.sleep(5)
                            edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                                    ClassName="Edit")
                            print(edit)
                            # 获取当前文件的根目录
                            current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                            file_path = os.path.join(self.application_path + "\\filedata", conscious_input_value2)
                            # 输入文件的路径加名称
                            edit.SendKeys(file_path)
                            # 点击打开按钮，确定选中的文件
                            auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                            # 附加按钮
                            fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                            ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()

                            # 上传成功后验证是否成功
                            if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_1a).text.find(
                                    conscious_input_value2) != -1:
                                print("上传成功了！")
                            else:
                                print("上传失败了")
                else:
                    self.web.find_element(By.XPATH, self.ele.section7_option_2a_no).click()
            # 7.2.2
            conscious_input_1a = self.ele.get_emc_describe(
                "Attach supplier certification ( a file containing a document or image) for purchased parts/assemblies (disk drives, power supplies, cables, card assemblies, etc.) that do not have their own PERD.")
            conscious_input_1a = self.web.find_element(By.XPATH, conscious_input_1a)
            conscious_input_text1 = self.operate_excel.get_text_cols_data(conscious_input_1a.text)
            conscious_input_value1 = self.operate_excel.get_value_cols_data(conscious_input_1a.text)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", conscious_input_1a)
            if conscious_input_text1 and conscious_input_value1:
                if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_2a).text.find(
                    conscious_input_value1) != -1:
                    print("已上传过了！")
                else:
                    # 点击附件文件按钮
                    conscious_buttom_1a = self.web.find_element(By.XPATH, self.ele.section7_conscious_click_2a)
                    conscious_buttom_1a.click()
                    # 选择文件
                    xuan_file = self.web.find_element(By.XPATH, self.ele.select_file)
                    ActionChains(self.web.driver).move_to_element(xuan_file).click().perform()

                    time.sleep(5)
                    edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32", ClassName="Edit")
                    print(edit)
                    # 获取当前文件的根目录
                    current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                    file_path = os.path.join(self.application_path + "\\filedata", conscious_input_value1)
                    # 输入文件的路径加名称
                    edit.SendKeys(file_path)
                    # 点击打开按钮，确定选中的文件
                    auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                    # 附加按钮
                    fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                    ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()

                    # 上传成功后验证是否成功
                    if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_2a).text.find(conscious_input_value1) != -1:
                        print("上传成功了！")
                    else:
                        print("上传失败了")


            # 7.3.1
            file_title = "Download a copy of the completed GDX entry for at least one representative machine type"
            conscious_input_3a = self.ele.get_div_describe(
                "All part data must be complete")
            conscious_input_3a = self.web.find_element(By.XPATH, conscious_input_3a)
            conscious_input_text3 = self.operate_excel.get_text_cols_data(file_title)
            conscious_input_value3 = self.operate_excel.get_value_cols_data(file_title)
            if conscious_input_3a and conscious_input_value3:
                if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_3a).text.find(
                    conscious_input_value3) != -1:
                    print("已上传过了！")
                else:
                    # 点击附件文件按钮
                    conscious_buttom_3a = self.web.find_element(By.XPATH, self.ele.section7_conscious_click_3a)
                    conscious_buttom_3a.click()
                    # 选择文件
                    xuan_file = self.web.find_element(By.XPATH, self.ele.select_file)
                    ActionChains(self.web.driver).move_to_element(xuan_file).click().perform()

                    time.sleep(5)
                    edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                            ClassName="Edit")
                    print(edit)
                    # 获取当前文件的根目录
                    current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                    file_path = os.path.join(self.application_path + "\\filedata", conscious_input_value3)
                    # 输入文件的路径加名称
                    edit.SendKeys(file_path)
                    # 点击打开按钮，确定选中的文件
                    auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                    # 附加按钮
                    fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                    ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()

                    # 上传成功后验证是否成功
                    if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_3a).text.find(conscious_input_value3) != -1:
                        print("上传成功了！")
                    else:
                        print("上传失败了")

            # 7.3.2
            file_title1 = "Use the link above to access the BOM Scrub Verification File"
            conscious_input_4a = self.ele.get_emc_describe(
                "Save a local copy of the template.")
            conscious_input_4a = self.web.find_element(By.XPATH, conscious_input_4a)
            conscious_input_text4 = self.operate_excel.get_text_cols_data(file_title1)
            conscious_input_value4 = self.operate_excel.get_value_cols_data(file_title1)
            if conscious_input_text4 and conscious_input_value4:
                if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_4a).text.find(
                    conscious_input_value4) != -1:
                    print("已上传过了！")
                else:
                    # 点击附件文件按钮
                    conscious_buttom_4a = self.web.find_element(By.XPATH, self.ele.section7_conscious_click_4a)
                    conscious_buttom_4a.click()
                    # 选择文件
                    xuan_file = self.web.find_element(By.XPATH, self.ele.select_file)
                    ActionChains(self.web.driver).move_to_element(xuan_file).click().perform()

                    time.sleep(5)
                    edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                            ClassName="Edit")
                    print(edit)
                    # 获取当前文件的根目录
                    current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                    file_path = os.path.join(self.application_path + "\\filedata", conscious_input_value4)
                    # 输入文件的路径加名称
                    edit.SendKeys(file_path)
                    # 点击打开按钮，确定选中的文件
                    auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                    # 附加按钮
                    fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                    ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()

                    # 上传成功后验证是否成功
                    if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_4a).text.find(conscious_input_value4) != -1:
                        print("上传成功了！")
                    else:
                        print("上传失败了")
            # 7.3.3 SCIP Data Upload
            conscious_txt_radio5 = self.ele.get_emc_describe(
                'Has SCIP submission occurred?')
            conscious_text_radio5 = self.web.find_element(By.XPATH, conscious_txt_radio5)
            conscious_select_text5 = self.operate_excel.get_text_cols_data(conscious_text_radio5.text)
            conscious_select_value5 = self.operate_excel.get_value_cols_data(conscious_text_radio5.text)
            if conscious_text_radio5.text and conscious_select_value5:
                if conscious_select_value5 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section7_option_3a_yes).click()
                    # 文本框有内容时，输入内容
                    conscious_input_txt5 = self.ele.get_emc_describe(
                        "Please enter the SCIP submission number in the proper format:")
                    conscious_input_text5 = self.web.find_element(By.XPATH, conscious_input_txt5)
                    conscious_select_input_text5 = self.operate_excel.get_text_cols_data(conscious_input_text5.text)
                    conscious_select_value_text5 = self.operate_excel.get_value_cols_data(conscious_input_text5.text)
                    if conscious_select_input_text5 and conscious_select_value_text5:
                        self.web.find_element(By.XPATH, self.ele.section7_conscious_input_3a).clear()
                        self.web.find_element(By.XPATH, self.ele.section7_conscious_input_3a).send_keys(
                            conscious_select_value_text5)
                else:
                    self.web.find_element(By.XPATH, self.ele.section7_option_3a_no).click()
                    # 选择选项
                    conscious_txt_radio6 = self.ele.get_emc_describe(
                        'Please select the reason for your response')
                    conscious_text_radio6 = self.web.find_element(By.XPATH, conscious_txt_radio6)
                    conscious_select_text6 = self.operate_excel.get_text_cols_data(conscious_text_radio6.text)
                    conscious_select_value6 = self.operate_excel.get_value_cols_data(conscious_text_radio6.text)
                    if conscious_text_radio6.text and conscious_select_value6:
                        self.web.find_element(By.XPATH, self.ele.section7_conscious_select_3a).click()
                        conscious_text_radio6.click()
                        section1_select = self.web.find_element(By.XPATH, self.ele.section7_conscious_select_3a)

                        Select(section1_select).select_by_visible_text(conscious_select_value6)

            # 7.4 Plastic Standard
            conscious_txt_radio7 = self.ele.get_emc_describe(
                'Are all plastic parts weighing 25 grams or more marked with full identification in accordance with ISO 11469 ?')
            conscious_text_radio7 = self.web.find_element(By.XPATH, conscious_txt_radio7)
            conscious_select_text7 = self.operate_excel.get_text_cols_data(conscious_text_radio7.text)
            conscious_select_value7 = self.operate_excel.get_value_cols_data(conscious_text_radio7.text)

            if conscious_text_radio7.text and conscious_select_value7:
                if conscious_select_value7 == "Yes - Plastic parts > 25 gram have full ID":
                    self.web.find_element(By.XPATH, self.ele.section7_option_4a_yes).click()
                elif conscious_select_value7 == "No - Plastic parts > 25 gram do not have full ID":
                    self.web.find_element(By.XPATH, self.ele.section7_option_4a_no).click()
                elif conscious_select_value7 == "Not Applicable - No plastic parts > 25 grams":
                    self.web.find_element(By.XPATH, self.ele.section7_option_4a_not).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.section7_option_4a_to).click()
            # 文本框输入内容
            conscious_input_txt7 = self.ele.get_emc_describe(
                "Please comment on your selected answer")
            conscious_input_text7 = self.web.find_element(By.XPATH, conscious_input_txt7)
            conscious_select_value_text7 = self.operate_excel.get_value_cols_list(conscious_input_text7.text)[1]
            if conscious_select_value_text7:
                self.web.find_element(By.XPATH, self.ele.section7_conscious_input_4a).send_keys(
                    conscious_select_value_text7)

            # 7.5 Polyvinyl Chloride Cables and Cords
            conscious_txt_radio8 = self.ele.get_div_describe(
                'Does the product contain polyvinyl cables or cords subject to the requirements of')
            conscious_text_radio8 = self.web.find_element(By.XPATH, conscious_txt_radio8)
            conscious_select_text8 = self.operate_excel.get_text_cols_data(conscious_text_radio8.text)
            conscious_select_value8 = self.operate_excel.get_value_cols_data(conscious_text_radio8.text)

            if conscious_select_text8 and conscious_select_value8:
                if conscious_select_value8 == "Yes":
                    self.web.find_element(By.XPATH, self.ele.section7_option_5a_yes).click()
                    # 选择yes时，隐藏项目
                    conscious_txt_radio81 = self.ele.get_emc_describe(
                        'Does the product contain polyvinyl cables or cords which require warning statements be provided as identified in')
                    conscious_text_radio81 = self.web.find_element(By.XPATH, conscious_txt_radio81)
                    conscious_select_text81 = self.operate_excel.get_text_cols_data(conscious_text_radio81.text)
                    conscious_select_value81 = self.operate_excel.get_value_cols_data(conscious_text_radio81.text)

                    if conscious_select_text81 and conscious_select_value81:
                        if conscious_select_value81 == "Yes":
                            self.web.find_element(By.XPATH, self.ele.section7_option_5a_yes_2a).click()
                            # 选择yes时，隐藏项目
                            # 文本框输入内容
                            conscious_input_txt8_1a = self.ele.get_emc_describe(
                                "Describe how the warning statements have been provided?")
                            conscious_input_text8_1a = self.web.find_element(By.XPATH, conscious_input_txt8_1a)
                            conscious_select_text8_1a = self.operate_excel.get_text_cols_data(conscious_input_text8_1a.text)
                            conscious_select_value_text8_1a = \
                            self.operate_excel.get_value_cols_data(conscious_input_text8_1a.text)
                            if conscious_select_text8_1a and conscious_select_value_text8_1a:
                                self.web.find_element(By.XPATH, self.ele.section7_cords_input_1a).send_keys(
                                    conscious_select_value_text8_1a)

                        else:
                            self.web.find_element(By.XPATH, self.ele.section7_option_5a_no_2a).click()
                        # 文本框输入内容 List part number of cables
                        conscious_input_txt8_2a = self.ele.get_emc_describe(
                            "List part number of cables")
                        conscious_input_text8_2a = self.web.find_element(By.XPATH, conscious_input_txt8_2a)
                        conscious_select_text8_2a = self.operate_excel.get_text_cols_data(
                            conscious_input_text8_2a.text)
                        conscious_select_value_text8_2a = \
                            self.operate_excel.get_value_cols_data(conscious_input_text8_2a.text)
                        if conscious_select_text8_2a and conscious_select_value_text8_2a:
                            self.web.find_element(By.XPATH, self.ele.section7_cords_input_2a).send_keys(
                                conscious_select_value_text8_2a)
                        # 文本框输入内容 List part number of cables
                        # List FRU number of cables
                        conscious_input_txt8_3a = self.ele.get_emc_describe(
                            "List FRU number of cables")
                        conscious_input_text8_3a = self.web.find_element(By.XPATH, conscious_input_txt8_3a)
                        conscious_select_text8_3a = self.operate_excel.get_text_cols_data(
                            conscious_input_text8_3a.text)
                        conscious_select_value_text8_3a = \
                            self.operate_excel.get_value_cols_data(conscious_input_text8_3a.text)
                        if conscious_select_text8_3a and conscious_select_value_text8_3a:
                            self.web.find_element(By.XPATH, self.ele.section7_cords_input_3a).send_keys(
                                conscious_select_value_text8_3a)

                else:
                    self.web.find_element(By.XPATH, self.ele.section7_option_5a_no).click()
            # 7.6 The ECO Declaration
            conscious_input_9a = self.ele.get_emc_describe(
                "Attach the ECO (TED) Declaration")
            conscious_input_9a = self.web.find_elements(By.XPATH, conscious_input_9a)[1]
            conscious_input_text9 = self.operate_excel.get_text_cols_data(conscious_input_9a.text)
            conscious_input_value9 = self.operate_excel.get_value_cols_data(conscious_input_9a.text)
            if conscious_input_text9 and conscious_input_value9:
                if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_6a).text.find(
                    conscious_input_value9) != -1:
                    print("已上传过了！")
                else:
                    # 点击附件文件按钮
                    conscious_buttom_9a = self.web.find_element(By.XPATH, self.ele.section7_conscious_click_6a)
                    conscious_buttom_9a.click()
                    # 选择文件
                    xuan_file = self.web.find_element(By.XPATH, self.ele.select_file)
                    ActionChains(self.web.driver).move_to_element(xuan_file).click().perform()

                    time.sleep(5)
                    edit = auto.EditControl(foundIndex=1, AutomationId="1148", FrameworkId="Win32",
                                            ClassName="Edit")
                    print(edit)
                    # 获取当前文件的根目录
                    current_path = os.path.abspath(os.path.dirname((os.getcwd())))
                    file_path = os.path.join(self.application_path + "\\filedata", conscious_input_value9)
                    # 输入文件的路径加名称
                    edit.SendKeys(file_path)
                    # 点击打开按钮，确定选中的文件
                    auto.ButtonControl(foundIndex=1, AutomationId="1", ClassName="Button").Click()  # 打开
                    # 附加按钮
                    fujia_file = self.web.find_element(By.XPATH, "//input[@id='DialogButton0']")
                    ActionChains(self.web.driver).move_to_element(fujia_file).click().perform()

                    # 上传成功后验证是否成功
                    if self.web.find_element(By.XPATH, self.ele.section7_conscious_click_6a).text.find(conscious_input_value9) != -1:
                        print("上传成功了！")
                    else:
                        print("上传失败了")

            # 填写完后，点击提交按钮
            completed_true = self.web.find(By.XPATH, self.ele.submit_completed_but)
            if completed_true:
                self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()
                time.sleep(15)
                self.web.driver.close()

    def main_PERD(self):

        try:
            print("开始执行")
            try:

                print("当前执行 section1")
                self.current = "当前执行 section1"
                self.perd_section1()
                self.cases_end = True
                self.results = True
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = False
            try:
                time.sleep(2)
                self.cases_end = False
                self.results = None
                print("当前执行 section2")
                self.current = "当前执行 section2"

                self.perd_section2()
                self.cases_end = True
                self.results = True
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = False
            try:
                time.sleep(2)
                print("当前执行 section3")
                self.cases_end = False
                self.results = None
                self.current = "当前执行 section3"

                self.perd_section3()
                self.cases_end = True
                self.results = True
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = False
            try:
                time.sleep(2)
                print("当前执行 section4")
                self.cases_end = False
                self.results = None
                self.current = "当前执行 section4"

                self.perd_section4()
                self.cases_end = True
                self.results = True
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = False
            try:
                time.sleep(2)
                print("当前执行 section5")
                self.cases_end = False
                self.results = None
                self.current = "当前执行 section5"
                self.perd_section5()
                self.cases_end = True
                self.results = True
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = False
            try:
                time.sleep(2)
                print("当前执行 section6")
                self.cases_end = False
                self.results = None
                self.current = "当前执行 section6"

                self.perd_section6()
                self.cases_end = True
                self.results = True
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = False
            try:
                time.sleep(2)
                print("当前执行 section7")
                self.cases_end = False
                self.results = None
                self.current = "当前执行 section7"

                self.perd_section7()
                self.cases_end = True
                self.results = True
                time.sleep(5)
                self.end = True
                # 关闭浏览器
                self.web.driver.close()
                print("关闭浏览器")
                self.web.driver.quit()
            except Exception as e:
                # 将错误信息打印到控制台
                print(f"程序执行出错：{e}")
                self.web.driver.close()
                self.cases_end = True
                self.results = True
                time.sleep(3)
                self.end = True
                print("关闭浏览器")
                self.web.driver.quit()
        except Exception as e:
            time.sleep(2)
            self.end = True
            print("关闭浏览器")
            self.web.driver.quit()
            print("程序异常退出！", e)
            self.web.driver.close()


    def test(self):
        print("self.web.find_element(By.XPATH, self.ele.packaging_record_input_2a).text:",
              self.web.find_element(By.XPATH, self.ele.packaging_record_input_2a).get_attribute("value"))


if __name__ == "__main__":
    perd = PERD("../data/PERD EOS Gen2 combo.xlsx","../data/Packaging collection-Lenovo KM203W(选件)-20231116.xlsx","https://cowork.lenovo.com/departments/quality/_layouts/15/FormServer.aspx?XmlLocation=https%3a//cowork.lenovo.com/departments/quality/PERD%20Records/LOPT-2023-0220.xml&Source=https%3a//cowork.lenovo.com/departments/quality/PERD%20Records/Forms/Default%20View.aspx&DefaultItemOpen=1")
    
    # perd.perd_section1()
    # perd.test_section()
    # perd.perd_section3()
    # perd.perd_section4()
    # perd.perd_section5()
    # perd.perd_section6()
    perd.perd_section7()
    # perd.perd_section4()
    # perd.section4_packaging("1200x1000mm栈板", perd.ele.section4_option_4a_1a)

    # perd.test()





















