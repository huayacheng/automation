#_*_encoding:GBK*_
import time,os,subprocess
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
    device = '0566d069'
    return device

device = device()
# 计数成功次数
count = 0
# 执行次数
num = 1
#实例化
Perfor_show = Perfor_show()
adb=adb(device=device)
log_path=path()+'logs\\log'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()
element = app_element_position()
# 开启日志抓取
#log.Open('app_link_tv')
# 开启appium
driver = Basepage(device=device,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='8')
driver.Open()

gonggao = driver.find(MobileBy.XPATH,element.APP_cement_but)
if gonggao == True:
    driver.find_element(MobileBy.XPATH, element.APP_cement_but).click()
else:
    pass
# 测试服专有
time.sleep(2)
driver.Tap([(517,1281)])
time.sleep(5)
# 我的  [752,1804][1048,1906]
driver.Tap([(890,1850)])
time.sleep(3)
# 开始循环的位置
while True:
    try:
        conetnum = '开始执行第' + str(num) + '次'
        logO.info(conetnum)

        # 进入登录界面
        driver.Tap([(630,201)])
        #点击密码icon图标 切换密码登录
        driver.find_element(MobileBy.XPATH,element.APP_pwd_icon).click()
        # 输入用户名，密码
        driver.find_element(MobileBy.XPATH, element.APP_mobile_input).set_text("15820407637")
        driver.find_element(MobileBy.XPATH, element.APP_pwdword_input).set_text("123456")
        time.sleep(4)
        #点击登录
        driver.find_element(MobileBy.XPATH, element.APP_loging_but).click()
        time.sleep(2)
        denglu = driver.find(MobileBy.XPATH, element.APP_loging_but)
        if denglu == True:
            driver.find_element(MobileBy.XPATH, element.APP_loging_but).click()
        else:
            pass
        time.sleep(8)
        # 登录之后用户状态验证
        vip_member = driver.find_element(MobileBy.XPATH, element.APP_content_user).get_attribute("text")
        print(vip_member)
        if str(vip_member) == "乐播会员":
            logO.info("登录成功")
        else:
            logO.info("登录失败")
        driver.swipeUp(0.3)
        # 点击设置按钮
        driver.find_element(MobileBy.XPATH,element.APP_setting_but).click()
        # 点击退出登录
        driver.find_element(MobileBy.XPATH,element.APP_logout_but).click()
        # 确定退出
        driver.find_element(MobileBy.XPATH,element.APP_quit_but).click()
        time.sleep(2)
        driver.swipeDown(0.5)
        Number = '已执行完第' + str(num) + '次'  # 次数
        logO.info(Number)
        num += 1
    except Exception as e:
        print(e)
        driver = Basepage(device=device, driver='driver', appPackage='com.hpplay.happycast',
                          appActivity='com.hpplay.advertisement.SplashActivity', port=8200,
                          url='http://127.0.0.1:4723/wd/hub', version='6')
        driver.Open()

        gonggao = driver.find(MobileBy.XPATH, element.APP_cement_but)
        if gonggao == True:
            driver.find_element(MobileBy.XPATH, element.APP_cement_but).click()
        else:
            pass
        # 测试服专有
        time.sleep(2)
        driver.Tap([(517, 1281)])
        time.sleep(5)
        # 我的  [752,1804][1048,1906]
        driver.Tap([(890, 1850)])
        time.sleep(3)
        # 验证一下，会员是否有登录，如果还是有登录，退出再执行
        # 登录之后用户状态验证
        vip = driver.find(MobileBy.XPATH,element.APP_content_user)
        if vip == True:
            vip_member = driver.find_element(MobileBy.XPATH, element.APP_content_user).get_attribute("text")
            print(vip_member)
            if str(vip_member) == "乐播会员":
                logO.info("登录成功")
            else:
                logO.info("登录失败")
            driver.swipeUp(0.3)
            # 点击设置按钮
            driver.find_element(MobileBy.XPATH, element.APP_setting_but).click()
            # 点击退出登录
            driver.find_element(MobileBy.XPATH, element.APP_logout_but).click()
            # 确定退出
            driver.find_element(MobileBy.XPATH, element.APP_quit_but).click()
            time.sleep(2)
            driver.swipeDown(0.5)
        else:
            pass


