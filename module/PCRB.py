import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, re, sys, os
from selenium.webdriver.support.ui import Select


def Get_Hardware():
    url = 'https://cowork.lenovo.com/departments/quality/Lists/PCRBHardwareTest/Item/displayifs.aspx?ID=2037&Source=/departments/quality/SitePages/My%20PCRB.aspx'
    c = webdriver.Chrome()
    c.get(url)
    c.implicitly_wait(10)
    time.sleep(5)
    ss = c.find_element(By.ID, 'Ribbon.Tabs.InfoPathListDisplayTab.Manage.Controls.btnEdit-Large')
    ss.click()
    time.sleep(5)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O10']").click()
    time.sleep(1)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O14']").click()
    time.sleep(1)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O16']").click()
    # for i in c.find_elements(By.XPATH,"//*/input[@type='radio']"):  # 实现遍历点击所有的radio
    #     print(i.get_attribute('text'))
    #     time.sleep(3)
    #     #i.click()
    time.sleep(1)
    c.save_screenshot(c.title + '_' + str(time.time()) + '.png')
    time.sleep(2)
    c.find_element(By.XPATH, "//input[@value='Complete']").click()
    time.sleep(10)


def Get_EMC():
    url = 'https://cowork.lenovo.com/departments/quality/Lists/PCRBEMC/Item/displayifs.aspx?ID=3481&Source=/departments/quality/SitePages/My%20PCRB.aspx'
    c = webdriver.Chrome()
    c.get(url)
    c.implicitly_wait(10)
    time.sleep(5)
    ss = c.find_element(By.ID, 'Ribbon.Tabs.InfoPathListDisplayTab.Manage.Controls.btnEdit-Large')
    ss.click()
    time.sleep(5)
    ss = c.find_element(By.XPATH, "//input[@originalid='V1_I1_T7']").get_attribute('value')
    print('EMC status:', ss)
    time.sleep(5)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O13']").click()
    time.sleep(1)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O16']").click()
    time.sleep(1)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O19']").click()
    time.sleep(1)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O23']").click()
    time.sleep(1)
    c.find_element(By.XPATH, "//input[@originalid='V1_I1_O25']").click()
    time.sleep(1)
    c.save_screenshot(c.title + '_' + str(time.time()) + '.png')


def Get_ENV():
    url = 'https://cowork.lenovo.com/departments/quality/Lists/PCRBEnvironmental/Item/displayifs.aspx?ID=2654&Source=/departments/quality//SitePages/My%20PCRB.aspx'
    c1 = webdriver.Chrome()
    c1.get(url)
    c1.implicitly_wait(10)
    time.sleep(5)
    ss = c1.find_element(By.XPATH, "//input[@originalid='V1_I1_T7']").get_attribute('value')
    print('ENV status:', ss)
    if ss == 'Completed':
        time.sleep(1)
        s1 = c1.find_element(By.ID, 'onetIDListForm')
        s2 = s1.find_element(By.TAG_NAME, 'td')
        c1.find_element(By.XPATH,
                        "//a[@title='https://cowork.lenovo.com/departments/quality/_layouts/15/FormServer.aspx?XmlLocation=https://cowork.lenovo.com/departments/quality/APPPCRBRecords/LOPT-2022-0203%20REV%202%20Wave%201.xml&DefaultItemOpen=1']").click()
        for handle in c1.window_handles:
            c1.switch_to.window(handle)
            # print(c1.title)
            time.sleep(1)
            if 'PCRB Records' in c1.title:
                # c1.find_element(By.ID,'Ribbon.Tabs.InfoPathHomeTab.FormActions.Controls.btnSave-Large').click() # 点击保存
                c1.find_element(By.ID, 'FormControl_V1_I1_S14_I35_H1').click()
        for handle in c1.window_handles:
            c1.switch_to.window(handle)
            print(c1.title)
            if 'Import Attachments - PCRB' in c1.title:
                c1.find_element(By.XPATH, "//input[@originalid='V1_I1_T1']").send_keys('Hello')  # 在title 填内容
                time.sleep(1)
                c1.find_element(By.XPATH, "//div[@role='textbox']").send_keys('denisliang')  # 在comments填内容
                select1 = c1.find_element(By.XPATH, "//select[@originalid='V1_I1_D5']")  # 下拉框选择
                time.sleep(2)
                select1.click()
                select1 = c1.find_element(By.XPATH, "//select[@originalid='V1_I1_D5']")  # 下拉框选择
                # print(len(Select(select1).options))
                # for i in Select(select1).options:
                #     print(i)
                Select(select1).select_by_value('3345')
                time.sleep(2)
                filelist = ['D:/PycharmProjects/patvsapi/2222.png', 'D:/PycharmProjects/patvsapi/baidu.png',
                            'D:/PycharmProjects/patvsapi/PCRB.png']
                for i in filelist:
                    c1.find_element(By.XPATH, "//a[@title='单击此处以附加文件']").click()
                    time.sleep(1)
                    s2 = c1.find_element(By.ID, 'FileAttachmentUpload')
                    s2.send_keys(i)
                    c1.find_element(By.ID, 'DialogButton0').click()

                time.sleep(10)
                c1.save_screenshot(c1.title + '_' + str(time.time()) + '.png')
                c1.find_element(By.XPATH, "//input[@value='Cancel']").click()
                # time.sleep(5)
                # c1.find_element(By.ID,'ctl00_ctl41_g_26119a49_d835_4b71_ab5d_3372973c3072_FormControl0_V1_I1_SPFAC4') # 上传附件
    else:
        time.sleep(5)
        ss = c1.find_element(By.ID, 'Ribbon.Tabs.InfoPathListDisplayTab.Manage.Controls.btnEdit-Large')
        ss.click()
        time.sleep(5)
        c1.find_element(By.XPATH, "//input[@originalid='V1_I1_O12']").click()
        time.sleep(1)
        c1.find_element(By.XPATH, "//input[@originalid='V1_I1_T15']").send_keys('REV 1 wave 1')
        time.sleep(1)
        c1.find_element(By.XPATH, "//input[@originalid='V1_I1_O18']").click()
        time.sleep(1)
        c1.find_element(By.XPATH, "//input[@originalid='V1_I1_O20']").click()
        time.sleep(1)
        c1.find_element(By.XPATH, "//input[@value='Complete']").click()
    c1.save_screenshot(c1.title + '_' + str(time.time()) + '.png')
    time.sleep(100)


def Get_Safety():
    url = 'https://cowork.lenovo.com/departments/quality/Lists/PCRBSafety/Item/displayifs.aspx?ID=3887&Source=/departments/quality//SitePages/My%20PCRB.aspx'
    c2 = webdriver.Chrome()
    c2.get(url)
    c2.implicitly_wait(10)
    time.sleep(5)
    ss = c2.find_element(By.ID, 'Ribbon.Tabs.InfoPathListDisplayTab.Manage.Controls.btnEdit-Large')
    ss.click()
    time.sleep(5)
    ss = c2.find_element(By.ID,
                         'ctl00_ctl41_g_9c3541a7_33b0_4c4c_a199_b6af3ce2e053_FormControl0_V1_I1_T4').get_attribute(
        'value')
    print('Safety status:', ss)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O8']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O11']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O15']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O19']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O23']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O27']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O31']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O35']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O39']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O43']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O47']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O53']").click()  # Lithium Battery Limitations
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O55']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O59']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O63']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O69']").click()  # Primary Power Isolation (control)
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O71']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O75']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O79']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O83']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O87']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O91']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O95']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O99']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O103']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O107']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O111']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O115']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O119']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O123']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O127']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O131']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O135']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O139']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O144']").click()
    time.sleep(1)
    c2.find_element(By.XPATH, "//input[@originalid='V1_I1_O146']").click()
    time.sleep(1)
    c2.save_screenshot(c2.title + '_' + str(time.time()) + '.png')


def Get_Homologation():
    url = 'https://cowork.lenovo.com/departments/quality/Lists/PCRB%20%20Homologation%20Evaluations/Item/displayifs.aspx?ID=3038&Source=/departments/quality/SitePages/My%20PCRB.aspx'
    c3 = webdriver.Chrome()
    c3.get(url)
    c3.implicitly_wait(10)
    time.sleep(5)
    ss = c3.find_element(By.ID, 'Ribbon.Tabs.InfoPathListDisplayTab.Manage.Controls.btnEdit-Large')
    ss.click()
    time.sleep(5)
    currentHandle = c3.current_window_handle
    ss = c3.find_element(By.ID,
                         'ctl00_ctl41_g_0cca8769_710e_4ef9_950d_ab90d60bf77c_FormControl0_V1_I1_T8').get_attribute(
        'value')
    print('Homologation status:', ss)
    c3.find_element(By.ID, 'Ribbon.Tabs.InfoPathListDisplayTab.Manage.Controls.btnEdit-Large').click()
    time.sleep(5)
    c3.find_element(By.XPATH, "//input[@originalid='V1_I1_O17']").click()
    time.sleep(1)
    c3.find_element(By.XPATH, "//input[@originalid='V1_I1_O20']").click()
    time.sleep(1)
    c3.find_element(By.XPATH, "//input[@originalid='V1_I1_O23']").click()
    time.sleep(1)
    c3.find_element(By.XPATH, "//input[@originalid='V1_I1_O27']").click()
    time.sleep(1)
    c3.find_element(By.XPATH, "//input[@originalid='V1_I1_O31']").click()
    time.sleep(1)
    c3.find_element(By.XPATH, "//input[@originalid='V1_I1_O33']").click()
    c3.save_screenshot(c3.title + '_' + str(time.time()) + '.png')


def PERD_Section1():
    url = 'https://cowork.lenovo.com/departments/quality/_layouts/15/FormServer.aspx?XmlLocation=https%3a//cowork.lenovo.com/departments/quality/Product%20Description%20%20Section%201/TOPT-2020-0036.xml&Source=https%3a//cowork.lenovo.com/departments/quality/PERD%20Records/Forms/Default%20View.aspx&DefaultItemOpen=1'
    c = webdriver.Chrome()
    c.get(url)
    c.implicitly_wait(10)
    print(c.title)
    s = c.find_element(By.XPATH,"//input[@originalid='V1_I1_S1_I1_S1_I2_R2_I3_T1']").get_attribute('value')  # 获取项目ID, 用于获取目录里存放的附件
    select1 = c.find_element(By.XPATH, "//select[@originalid='V1_I1_S1_I1_S5_I9_D1']")
    Select(select1).select_by_value('Dock & Port Replicator')
    time.sleep(200)


if __name__ == "__main__":
    Get_EMC()
    # time.sleep(10)
    # Get_Safety()
    # time.sleep(10)
    # Get_Homologation()
    # time.sleep(10)
    #Get_ENV()
    #Get_Hardware()
    #PERD_Section1()

Hardware_test = {
    'Have all safety related issues (opened by hardware test) been resolved?': 'Yes',
    'Please review the Country Shipment Plan for the product in the Product Profile.  Based on your area of expertise, do you know of a problem related to safety that would restrict shipments to specific countries or geographic areas?': 'No',
    'Do you recommend the PCRB support shipment of the product?': 'Yes'
}

EMC = {
    'The EMC evaluation has been completed': 'Yes',
    'The EMC reports have been posted on eSIS': 'Yes',
    'The EMC reports have been posted on eSIS': 'Yes',
    'Please review the Country Shipment Plan for the product in the PCRB Record.  Based on your area of expertise, do you know of any compliance related issues that would restrict shipments to specific countries or geographic areas?': 'No',
    'Do you recommend the PCRB support shipment of the product?': 'Yes'}

Homologation = {
    'The Homologation evaluation has been completed, and input has been provided to the DoC coordinator to support shipments to EU countries (R&TTE Directive)': 'Yes',
    'The Homologation certificates for wireless and telecom devices have been posted to the Homologation ThinkSpace database when complete.': 'Yes',
    'The Regulatory Notice information has been posted to eSIS when complete': 'Yes',
    'The product has no known safety related problems with radiation caused by wireless transmissions': 'Yes',
    'Please review the Country Shipment Plan for the product in the PCRB Record.  Based on your area of expertise, do you know of any compliance related issues that would restrict shipments to specific countries or geographic areas': 'No',
    'Do you recommend the PCRB support shipment of the product?': 'Yes'}

Environmental = {
    'Has a Product Environmental Review Database (PERD) file been processed and approved': 'Yes',
    'Please review the Country Shipment Plan for the product in the PCRB Record.  Based on your area of expertise, do you know of any compliance related issues that would restrict shipments to specific countries or geographic areas': 'No',
    'Do you recommend the PCRB support shipment of the product?': 'Yes'}

Safety_table_id = 'onetIDListForm'
Safety = {
    'The Certification schedule and the Certification plan have been entered in the Product Safety Schedule and Plans section of the Product Profile': 'Yes',
    'General concept of product reviewed including hardware definition and product structure, including Customer Replaceable Unit (CRU) and Field Replaceable unit (FRU) plans': 'Yes',
    'Project Management Team notified of unique internal and external safety standards that must be met': 'Yes',
    'All hazardous chemicals identified and plans in place to properly label/document': 'Yes',
    'Product Safety requirements for the rating/agency marking label have been provided to the Project Management Team': 'Yes',
    'Requirements for all safety labels (Danger, Caution, etc.) have been provided to the Project Management Team, including wording, symbols, and translation requirements': 'Yes',
    'A test machine has been provided for safety evaluation and testing (as needed).  The machine must include safety sensitive feature power units, sub-assemblies and maximum logic card configurations (and/or dummy loads) and all alternate source power units and fans (if needed for test agency certification tests).  The machine must be representative of ship level hardware and include properly mounted decorative and airflow covers': 'Yes',
    'Information is available on all plastic/foam parts identifying the material and flame rating.   Note: flammability ratings less than V-1 for decorative parts must be approved via Approval letter from Brand Executive or equivalent. Letter to be attached to PCRB': 'Yes',
    'Information is available on all plastic/foam parts identifying the material and flame rating.   Note: flammability ratings less than V-1 for decorative parts must be approved via Approval letter from Brand Executive or equivalent. Letter to be attached to PCRB': 'Yes',
    'All open safety issues have been closed': 'Yes',
    'Manufacturing site locations and marking of final product are properly set up in safety agency reports': 'Yes',
    'Lithium Battery Limitations': 'NA',
    'Marking / Instructions': 'Yes',
    'Label Requirements': 'Yes',
    'Electrical Shock / Energy': 'Yes',
    'Primary Power Isolation (control)': 'NA',
    'Stability / Mechanical': 'Yes',
    'Material Handling & Weight Restrictions': 'Yes',
    'Resistance to Fire': 'Yes',
    'Production Testing': 'Yes',
    'All hardware changes made since evaluation testing have been reviewed for safety impact': 'Yes',
    'If there have been any safety incidents with the product during development or manufacture, have they been satisfactorily evaluated and necessary design modifications implemented': 'Yes',
    'There are no known conditions of foreseeable product misuse that could present a safety hazard': 'Yes',
    'Deviations to Lenovo Safety Standards have been properly documented, approved and filed by the Standards Authority(as required).  Note: the only safety standard that could possibly be deviated from is C-S 3-0501-070': 'Yes',
    'Customer, Maintenance and Installation document reviews completed and approved.  A safety inspection procedure in support of field services must be included in the maintenance documentation': 'Yes',
    'Plan for documentation and distribution of hazardous materials approved': 'Yes',
    'All applicable languages supported for all safety labels and safety related notices in customer and service manuals': 'Yes',
    'Product label verified to include unique identifier referenced in the certification reports, ratings, and safety agency logos.': 'Yes',
    'The CB report, if required, has been provided to the creator of the EU Declaration of Conformity (DoC) or placed on the eSIS database': 'Yes',
    'All the necessary safety agency approvals have been obtained.': 'Yes',
    'All soft-copy documents (including the CB report) required to support safety certification markings on the product at the manufacturing sites have been filed on the eSIS database': 'Yes',
    'If this product does not require (or have) a formal CB scheme report, an internal compliance report has been created': 'Yes',
    'There are no non-standard hi-pot or ground current tests required for the product or, if there are, they are documented and all manufacturing sites have been informed': 'Yes',
    'A mechanism is in place to provide Product Safety with alerts to product updates and changes (Review of all hardware ECs and Offspecs are sufficient': 'Yes',
    'Please review the Country Shipment Plan for the product in the PCRB Record.  Do you know of a problem related to safety or safety certification that would restrict shipments to specific countries or geographic areas': 'No',
    'Do you recommend the PCRB support shipment of the product': 'Yes'}
