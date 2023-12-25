# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2023/8/25 10:00
# File : PCRB_Form.py
from lib.common.BasePage import *
from element.webelement_po import element_position
from config.read_url_config import *

class PCRB():

    def __init__(self):
        self.web = BasePage("../docker/chromedriver.exe")
        self.ele = element_position()
        pass

    def Set_EMC(self):
        # 启动浏览器
        self.web.open_web(emc_url)
        # 检查项目的emc状态
        emc_status = self.ele.emc_Status
        if emc_status != "Completed":
            #eSIS Tracking
            self.web.driver.implicitly_wait(10)
            eSIS_tracking = self.web.find_elements(By.XPATH,self.ele.emc_tracking_input)
            for i in range(len(eSIS_tracking)):
                if eSIS_tracking[i] == 'EMC - Canada':
                    click_view = self.web.find_elements(By.XPATH, self.ele.emc_view_a)[i]
                    click_view.click()
                    # 进入该国家后，执行该国家的表单创建

                if eSIS_tracking[i] == 'EMC - Canada':
                    click_view = self.web.find_elements(By.XPATH, self.ele.emc_view_a)[i]
                    click_view.click()
            # 描述单选 1a
            yes = "yes"
            get_1a_txt = self.ele.get_emc_describe("The EMC evaluation has been completed")
            get_1a_text = self.web.find_element(By.XPATH, get_1a_txt)
            if 'The EMC evaluation has been completed' in get_1a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH,self.ele.emc_option_1a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emc_option_1a_no).click()
            # 描述单选 2a
            yes = "yes"
            get_2a_txt = self.ele.get_emc_describe("reports have been posted on eSIS.")
            get_2a_text = self.web.find_element(By.XPATH, get_2a_txt)
            if 'reports have been posted on eSIS.' in get_2a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emc_option_2a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emc_option_2a_no).click()
            # 描述单选 3a
            yes = "yes"
            get_3a_txt = self.ele.get_emc_describe("The applicable EMC certificates have been completed and posted on eSIS.")
            get_3a_text = self.web.find_element(By.XPATH, get_3a_txt)
            if 'The applicable EMC certificates have been completed and posted on eSIS.' in get_3a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emc_option_3a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emc_option_3a_no).click()
            # 描述单选 4a
            yes = "yes"
            get_4a_txt = self.ele.get_emc_describe(
                "Please review the Country Shipment Plan for the product in the PCRB Record.")
            get_4a_text = self.web.find_element(By.XPATH, get_4a_txt)
            if 'Please review the Country Shipment Plan for the product in the PCRB Record. Based on your area of expertise, do you know of any ' \
               'compliance related issues that would restrict shipments to specific countries or geographic areas?' in get_4a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emc_option_4a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emc_option_4a_no).click()

            # 描述单选 5a
            yes = "yes"
            get_5a_txt = self.ele.get_emc_describe(
                "Do you recommend the PCRB support shipment of the product?")
            get_5a_text = self.web.find_element(By.XPATH, get_5a_txt)
            if 'Do you recommend the PCRB support shipment of the product?' in get_5a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emc_option_5a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emc_option_5a_no).click()

            # 填写完后，点击提交按钮
            self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()

    def Set_ENV(self):
        # 启动浏览器
        self.web.open_web(emc_url)
        # 检查项目的env状态
        emv_status = self.ele.emv_Status
        if emv_status != "Completed":
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            eSIS_tracking = self.web.find_elements(By.XPATH, self.ele.emc_tracking_input)
            # 描述单选 1a
            yes = "yes"
            get_1a_txt = self.ele.get_emc_describe("Has a Product Environmental Review Database (PERD) file")
            get_1a_text = self.web.find_element(By.XPATH, get_1a_txt)
            if 'Has a Product Environmental Review Database (PERD) file' in get_1a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emv_option_1a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emv_option_1a_no).click()

            # 描述单选 2a
            yes = "yes"
            get_2a_txt = self.ele.get_emc_describe("Please review the Country Shipment Plan for the product in the Product Profile.  Based on your area of expertise, do you know of "
                                                   "a problem related to safety that would restrict shipments to specific countries or geographic areas?")
            get_2a_text = self.web.find_element(By.XPATH, get_2a_txt)
            if 'Please review the Country Shipment Plan for the product in the Product Profile.' in get_2a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emv_option_2a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emv_option_2a_no).click()

            # 描述单选 3a
            yes = "yes"
            get_3a_txt = self.ele.get_emc_describe(
                "Do you recommend the PCRB support shipment of the product?")
            get_3a_text = self.web.find_element(By.XPATH, get_3a_txt)
            if 'Do you recommend the PCRB support shipment of the product?' in get_3a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.emv_option_3a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.emv_option_3a_no).click()

            # 填写完后，点击提交按钮
            self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()

    def Set_Safety(self):
        # 启动浏览器
        self.web.open_web(emc_url)
        # 检查项目的env状态
        safety_status = self.ele.safety_Status
        if safety_status != "Completed":
            # eSIS Tracking
            self.web.driver.implicitly_wait(10)
            # 描述单选 1a
            yes = "yes"
            get_1a_txt = self.ele.get_emc_describe(
                "The Certification schedule and the Certification plan have been entered in the Product Safety Schedule and Plans section of the Product Profile.")
            get_1a_text = self.web.find_element(By.XPATH, get_1a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_1a_text)
            if 'The Certification schedule and the Certification plan have been entered in the Product Safety Schedule and Plans section of the Product Profile.' in get_1a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_1a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_1a_no).click()

            # 描述单选 2a
            yes = "yes"
            get_2a_txt = self.ele.get_emc_describe(
                "General concept of product reviewed including hardware definition and product structure, including Customer Replaceable Unit (CRU) and Field Replaceable unit (FRU) plans.")
            get_2a_text = self.web.find_element(By.XPATH, get_2a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_2a_text)
            if 'General concept of product reviewed including hardware definition and product structure, including Customer Replaceable Unit (CRU) and Field Replaceable unit (FRU) plans.' in get_2a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_2a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_2a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_2a_na).click()

            # 描述单选 3a
            yes = "yes"
            get_3a_txt = self.ele.get_emc_describe(
                "Project Management Team notified of unique internal and external safety standards that must be met")
            get_3a_text = self.web.find_element(By.XPATH, get_3a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_3a_text)
            if 'Project Management Team notified of unique internal and external safety standards that must be met' in get_3a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_3a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_3a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_3a_na).click()
            # 描述单选 4a
            yes = "yes"
            get_4a_txt = self.ele.get_emc_describe(
                "All hazardous chemicals identified and plans in place to properly label/document")
            get_4a_text = self.web.find_element(By.XPATH, get_4a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_4a_text)
            if 'All hazardous chemicals identified and plans in place to properly label/document' in get_4a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_4a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_4a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_4a_na).click()
            # 描述单选 5a
            yes = "yes"
            get_5a_txt = self.ele.get_emc_describe(
                "Product Safety requirements for the rating/agency marking label have been provided to the Project Management Team")
            get_5a_text = self.web.find_element(By.XPATH, get_5a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_5a_text)
            if 'Product Safety requirements for the rating/agency marking label have been provided to the Project Management Team' in get_5a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_5a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_5a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_5a_na).click()
            # 描述单选 6a
            yes = "yes"
            get_6a_txt = self.ele.get_emc_describe(
                "Requirements for all safety labels (Danger, Caution, etc.) have been provided to the Project Management Team, including wording, symbols, and translation requirements")
            get_6a_text = self.web.find_element(By.XPATH, get_6a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_6a_text)
            if 'Requirements for all safety labels (Danger, Caution, etc.) have been provided to the Project Management Team, including wording, symbols, and translation requirements' in get_6a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_6a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_6a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_6a_na).click()

            # 描述单选 7a
            yes = "yes"
            get_7a_txt = self.ele.get_emc_describe(
                "A test machine has been provided for safety evaluation and testing (as needed)")
            get_7a_text = self.web.find_element(By.XPATH, get_7a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_7a_text)
            if 'A test machine has been provided for safety evaluation and testing (as needed)' in get_7a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_7a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_7a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_7a_na).click()
            # 描述单选 8a
            yes = "yes"
            get_8a_txt = self.ele.get_emc_describe(
                "Information is available on all plastic/foam parts identifying the material and flame rating")
            get_8a_text = self.web.find_element(By.XPATH, get_8a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_8a_text)
            if 'Information is available on all plastic/foam parts identifying the material and flame rating' in get_8a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_8a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_8a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_8a_na).click()

            # 描述单选 9a
            yes = "yes"
            get_9a_txt = self.ele.get_emc_describe(
                "Compliance & Power Rating and Danger & Caution safety labels (or reference drawings) are available for review")
            get_9a_text = self.web.find_element(By.XPATH, get_9a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_9a_text)
            if 'Compliance & Power Rating and Danger & Caution safety labels (or reference drawings) are available for review' in get_9a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_9a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_9a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_9a_na).click()
            # 描述单选 10a
            yes = "yes"
            get_10a_txt = self.ele.get_emc_describe(
                "All open safety issues have been closed")
            get_10a_text = self.web.find_element(By.XPATH, get_10a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_10a_text)
            if 'All open safety issues have been closed' in get_10a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_10a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_10a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_10a_na).click()
            # 描述单选 11a
            yes = "yes"
            get_11a_txt = self.ele.get_emc_describe(
                "are properly set up in safety agency reports")
            get_11a_text = self.web.find_element(By.XPATH, get_11a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_11a_text)
            if 'are properly set up in safety agency reports' in get_11a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_11a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_11a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_11a_na).click()
            # 描述单选 12a
            yes = "yes"
            get_12a_txt = self.ele.get_emc_describe(
                "Lithium Battery Limitations")
            get_12a_text = self.web.find_element(By.XPATH, get_12a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_12a_text)
            if 'Lithium Battery Limitations' in get_12a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_12a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_12a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_12a_na).click()
            # 描述单选 13a
            yes = "yes"
            get_13a_txt = self.ele.get_emc_describe(
                "Marking / Instructions")
            get_13a_text = self.web.find_element(By.XPATH, get_13a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_13a_text)
            if 'Marking / Instructions' in get_13a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_13a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_13a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_13a_na).click()
            # 描述单选 14a
            yes = "yes"
            get_14a_txt = self.ele.get_emc_describe(
                "Label Requirements")
            get_14a_text = self.web.find_element(By.XPATH, get_14a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_14a_text)
            if 'Label Requirements' in get_14a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_14a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_14a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_14a_na).click()
            # 描述单选 15a
            yes = "yes"
            get_15a_txt = self.ele.get_emc_describe(
                "Electrical Shock / Energy")
            get_15a_text = self.web.find_element(By.XPATH, get_15a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_15a_text)
            if 'Electrical Shock / Energy' in get_15a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_15a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_15a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_15a_na).click()
            # 描述单选 16a
            yes = "yes"
            get_16a_txt = self.ele.get_emc_describe(
                "Primary Power Isolation (control)")
            get_16a_text = self.web.find_element(By.XPATH, get_16a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_16a_text)
            if 'Primary Power Isolation (control)' in get_16a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_16a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_16a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_16a_na).click()
            # 描述单选 17a
            yes = "yes"
            get_17a_txt = self.ele.get_emc_describe(
                "Stability / Mechanical")
            get_17a_text = self.web.find_element(By.XPATH, get_17a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_17a_text)
            if 'Stability / Mechanical' in get_17a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_17a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_17a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_17a_na).click()
            # 描述单选 18a
            yes = "yes"
            get_18a_txt = self.ele.get_emc_describe(
                "Material Handling & Weight Restrictions")
            get_18a_text = self.web.find_element(By.XPATH, get_18a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_18a_text)
            if 'Material Handling & Weight Restrictions' in get_18a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_18a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_18a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_18a_na).click()
            # 描述单选 19a
            yes = "yes"
            get_19a_txt = self.ele.get_emc_describe(
                "Resistance to Fire")
            get_19a_text = self.web.find_element(By.XPATH, get_19a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_19a_text)
            if 'Resistance to Fire' in get_19a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_19a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_19a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_19a_na).click()
            # 描述单选 20a
            yes = "yes"
            get_20a_txt = self.ele.get_emc_describe(
                "Production Testing")
            get_20a_text = self.web.find_element(By.XPATH, get_20a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_20a_text)
            if 'Production Testing' in get_20a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_20a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_20a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_20a_na).click()
            # 描述单选 21a
            yes = "yes"
            get_21a_txt = self.ele.get_emc_describe(
                "All hardware changes made since evaluation testing have been reviewed for safety impact")
            get_21a_text = self.web.find_element(By.XPATH, get_21a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_21a_text)
            if 'All hardware changes made since evaluation testing have been reviewed for safety impact' in get_21a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_21a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_21a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_21a_na).click()
            # 描述单选 22a
            yes = "yes"
            get_22a_txt = self.ele.get_emc_describe(
                "If there have been any safety incidents with the product during development or manufacture, have they been satisfactorily evaluated and necessary design modifications implemented")
            get_22a_text = self.web.find_element(By.XPATH, get_22a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_22a_text)
            if 'If there have been any safety incidents with the product during development or manufacture, have they been satisfactorily evaluated and necessary design modifications implemented' in get_22a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_22a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_22a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_22a_na).click()
            # 描述单选 23a
            yes = "yes"
            get_23a_txt = self.ele.get_emc_describe(
                "There are no known conditions of foreseeable product misuse that could present a safety hazard")
            get_23a_text = self.web.find_element(By.XPATH, get_23a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_23a_text)
            if 'There are no known conditions of foreseeable product misuse that could present a safety hazard' in get_23a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_23a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_23a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_23a_na).click()
            # 描述单选 24a
            yes = "yes"
            get_24a_txt = self.ele.get_emc_describe(
                "Deviations to Lenovo Safety Standards have been properly documented, approved and filed by the Standards Authority(as required)")
            get_24a_text = self.web.find_element(By.XPATH, get_24a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_24a_text)
            if 'Deviations to Lenovo Safety Standards have been properly documented, approved and filed by the Standards Authority(as required)' in get_24a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_24a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_24a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_24a_na).click()
            # 描述单选 25a
            yes = "yes"
            get_25a_txt = self.ele.get_emc_describe(
                "Customer, Maintenance and Installation document reviews completed and approved")
            get_25a_text = self.web.find_element(By.XPATH, get_25a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_25a_text)
            if 'Customer, Maintenance and Installation document reviews completed and approved' in get_25a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_25a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_25a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_25a_na).click()
            # 描述单选 26a
            yes = "yes"
            get_26a_txt = self.ele.get_emc_describe(
                "Plan for documentation and distribution of hazardous materials approved")
            get_26a_text = self.web.find_element(By.XPATH, get_26a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_26a_text)
            if 'Plan for documentation and distribution of hazardous materials approved' in get_26a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_26a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_26a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_26a_na).click()
            # 描述单选 27a
            yes = "yes"
            get_27a_txt = self.ele.get_emc_describe(
                "All applicable languages supported for all safety labels and safety related notices in customer and service manuals")
            get_27a_text = self.web.find_element(By.XPATH, get_27a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_27a_text)
            if 'All applicable languages supported for all safety labels and safety related notices in customer and service manuals' in get_27a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_27a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_27a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_27a_na).click()
            # 描述单选 28a
            yes = "yes"
            get_28a_txt = self.ele.get_emc_describe(
                "Product label verified to include unique identifier")
            get_28a_text = self.web.find_element(By.XPATH, get_28a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_28a_text)
            if 'Product label verified to include unique identifier' in get_28a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_28a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_28a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_28a_na).click()
            # 描述单选 29a
            yes = "yes"
            get_29a_txt = self.ele.get_emc_describe(
                "EU Declaration of Conformity (DoC) or placed on the eSIS database")
            get_29a_text = self.web.find_element(By.XPATH, get_29a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_29a_text)
            if 'EU Declaration of Conformity (DoC) or placed on the eSIS database' in get_29a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_29a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_29a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_29a_na).click()
            # 描述单选 30a
            yes = "yes"
            get_30a_txt = self.ele.get_emc_describe(
                "All the necessary safety agency approvals have been obtained")
            get_30a_text = self.web.find_element(By.XPATH, get_30a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_30a_text)
            if 'All the necessary safety agency approvals have been obtained' in get_30a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_30a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_30a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_30a_na).click()
            # 描述单选 31a
            yes = "yes"
            get_31a_txt = self.ele.get_emc_describe(
                "All soft-copy documents (including the CB report) required to support safety certification markings on the product at the manufacturing sites have been")
            get_31a_text = self.web.find_element(By.XPATH, get_31a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_31a_text)
            if 'All soft-copy documents (including the CB report) required to support safety certification markings on the product at the manufacturing sites have been' in get_31a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_31a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_31a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_31a_na).click()
            # 描述单选 32a
            yes = "yes"
            get_32a_txt = self.ele.get_emc_describe(
                "If this product does not require (or have) a formal CB scheme report, an internal compliance report has been created")
            get_32a_text = self.web.find_element(By.XPATH, get_32a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_32a_text)
            if 'If this product does not require (or have) a formal CB scheme report, an internal compliance report has been created' in get_32a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_32a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_32a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_32a_na).click()
            # 描述单选 33a
            yes = "yes"
            get_33a_txt = self.ele.get_emc_describe(
                "There are no non-standard hi-pot or ground current tests required for the product or, if there are, they are documented and all manufacturing sites have been informed")
            get_33a_text = self.web.find_element(By.XPATH, get_33a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_33a_text)
            if 'There are no non-standard hi-pot or ground current tests required for the product or, if there are, they are documented and all manufacturing sites have been informed' in get_33a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_33a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_33a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_33a_na).click()
            # 描述单选 34a
            yes = "yes"
            get_34a_txt = self.ele.get_emc_describe(
                "A mechanism is in place to provide Product Safety with alerts to product updates and changes")
            get_34a_text = self.web.find_element(By.XPATH, get_34a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_34a_text)
            if 'A mechanism is in place to provide Product Safety with alerts to product updates and changes' in get_34a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_34a_yes).click()
                elif yes == "no":
                    self.web.find_element(By.XPATH, self.ele.safety_option_34a_no).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_34a_na).click()
            # 描述单选 35a
            yes = "no"
            get_35a_txt = self.ele.get_emc_describe(
                "Please review the Country Shipment Plan for the product in the PCRB Record.")
            get_35a_text = self.web.find_element(By.XPATH, get_35a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_35a_text)
            if 'Please review the Country Shipment Plan for the product in the PCRB Record.' in get_35a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_35a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_35a_no).click()
            # 描述单选 36a
            yes = "yes"
            get_36a_txt = self.ele.get_emc_describe(
                "Do you recommend the PCRB support shipment of the product?")
            get_36a_text = self.web.find_element(By.XPATH, get_36a_txt)
            self.web.driver.execute_script("arguments[0].scrollIntoView();", get_36a_text)
            if 'Do you recommend the PCRB support shipment of the product?' in get_36a_text.text:
                if yes == "yes":
                    self.web.find_element(By.XPATH, self.ele.safety_option_36a_yes).click()
                else:
                    self.web.find_element(By.XPATH, self.ele.safety_option_36a_no).click()
            # 填写完后，点击提交按钮
            self.web.find_element(By.XPATH, self.ele.submit_completed_but).click()













