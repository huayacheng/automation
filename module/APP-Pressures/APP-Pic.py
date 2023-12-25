#_*_encoding:GBK*_
# 投票码镜像投屏
# 当前是小米手机  76d92268

import time,os,subprocess,random
from lib.common.Log import Log
from lib.common.Screencap import Screencap
from lib.common.ADB import adb
from lib.common.Logging import run_log
from lib.common.BasePage import Basepage
from appium.webdriver.common.mobileby import MobileBy
from lib.customlib.Perfor_show import Perfor_show
from devices_sdk.element.dongle_appem import app_element_position
def path():
    path='D:\\lebo_project\\devices_sdk\\'
    return path
def device():
    #  49
    device = '76d92268'
    return device

def device2():
    #  49
    device = '192.168.199.110:5555'
    return device

device1 = device()
device2 = device2()
# 计数成功次数
count = 0
# 执行次数
num = 1
#实例化
# 定位地址
Perfor_show = Perfor_show()
element = app_element_position()
adb=adb(device=device)
log_path=path()+'logs\\log'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()

# 开启日志抓取
#log.Open('app_link_tv')

driver = Basepage(device=device1,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='6')
driver.Open()
# 电视appium
driver_tv = Basepage(device=device2,driver='driver2',appPackage='com.hpplay.happyplay.aw',appActivity='com.hpplay.happyplay.aw.app.MainActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='5')

time.sleep(3)
display_but = driver.find(MobileBy.XPATH, element.APP_tips_but)
if  display_but == True:
    driver.find_element(MobileBy.XPATH, element.APP_tips_but).click()
else:
    pass

while num < 3001:
    #先清理日志
    try:
        conetnum = '开始执行第' + str(num) + '次'
        logO.info(conetnum)
        locat_c = 'adb -s ' + device1 + ' logcat -c'
        # print(locat_c)
        os.system(locat_c)
        os.system(locat_c)
        # 点击加号
        driver.find_element(MobileBy.XPATH,element.APP_castadd_but).click()
        # 点进手机相册投屏
        driver.find_element(MobileBy.XPATH,element.APP_photo_but).click()
        time.sleep(2)
        photo = driver.find_element(MobileBy.XPATH,element.APP_image_item)
        print(photo)
        ram = random.randint(10)
        print(ram)
        photo[ram].click()
        # 点进手机相册投屏
        driver.find_element(MobileBy.XPATH, element.APP_piccast_but).click()
        # 选择“我家的乐播投屏”
        lebo =  driver.find(MobileBy.XPATH, element.APP_devicename_txt)
        if lebo == True:
            driver.find_element(MobileBy.XPATH, element.APP_devicename_txt).click()
        else:
            pass
    except Exception as e:
        print(e)