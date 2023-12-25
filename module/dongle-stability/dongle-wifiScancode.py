#_*_encoding:GBK*_
import time,os,subprocess
from lib.common.Log import Log
from lib.common.Screencap import Screencap
from lib.common.ADB import adb
from lib.common.Logging import run_log
from lib.common.BasePage import Basepage
from appium.webdriver.common.mobileby import MobileBy
from lib.customlib import Perfor_show
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
adb=adb(device=device)
log_path=path()+'logs\\log'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()

# 开启日志抓取
#log.Open('app_link_tv')

driver = Basepage(device=device,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='8')
driver.Open()


# time.sleep(2)
# allow_find = driver.find(MobileBy.XPATH,"//*[@resource-id='android:id/button1']")
# # 刚打开app是需要权限
# if allow_find == True:
#     allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
#     allow.click()
#     time.sleep(1)
#     allow_find = driver.find(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
#     if allow_find == True:
#         allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
#         allow.click()
#         allow_find = driver.find(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
#         if allow_find == True:
#             allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
#             allow.click()
#             time.sleep(5)
#             for i in range(3):
#                 driver.swipLeft(0.2)
#             driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/enter_tv']").click()
#             time.sleep(1)
#         else:
#             pass
#     else:
#         pass
# else:
#     pass


# time.sleep(3)
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']").click()

# 点击扫码进行镜像投屏
# saoma = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]")
# saoma.click()
# # 账号登录
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/pwd_ib']").click()
# # 输入用户名，密码
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/mobile_et']").set_text("15820407637")
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/password_et']").set_text("123456")
# time.sleep(4)
# #点击登录
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/btn_login']").click()
# time.sleep(10)
while num < 3001:
    #先清理日志
    try:
        conetnum = '开始执行第' + str(num) + '次'
        logO.info(conetnum)
        os.system('adb -s ' + device + ' logcat -c')
        os.system('adb -s ' + device + ' logcat -c')
        # 点击扫码进行镜像投屏
        saoma = driver.find_element(MobileBy.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]")
        saoma.click()
        # quan_but = driver.find(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        # if quan_but == True:
        #     # 立即开始
        #     allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        #     allow.click()
        # else:
        #     pass
        time.sleep(10)
        #等待扫码完成
        # adb.back()
        # start_but = driver.find(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        # if start_but == True:
        #     # 立即开始
        #     allow_start = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        #     allow_start.click()
        # else:
        #     pass

        # 投屏成功后抓取logcat，拦截 镜像成功和失败的关键字

        lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logpath = log_path + '\\' + device + '-' + lt + '.log'
        op = open(logpath, 'w', encoding='utf-8')
        command2 = 'adb -s ' + device + ' logcat '
        log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)

        time.sleep(10)

        devNull = open(os.devnull, 'w')
        a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
        log.terminate()
        a.wait()
        a.terminate()
        time.sleep(1)

        pass_num = Perfor_show.Intercept_mirror_switch(logpath, "ScreenCastService:onStart",
                                                       "MainActivity: onError what")
        print(pass_num)
        if pass_num[0] == True:
            pas = "成功扫码镜像"
            print(pas)
            count+=1
            # 结束投屏
            driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/cast_stop_tv']").click()
            # 定位点击确定
            time.sleep(2)
            driver.Tap([(750, 1168)])
        else:
            fail = "扫码镜像失败"
            print(fail)
            logO.info(fail)
            logO.info(logpath)
            count+=0

        pass_img = "成功投屏第：" + str(count) + "次"
        logO.info(pass_img)

        time.sleep(5)

        Number = '已执行完第' + str(num) + '次'  # 次数
        logO.info(Number)
        num += 1
    except Exception as e:
        print(e)
        adb.back(2)
        Number = '已执行完第' + str(num) + '次'  # 次数
        logO.info(Number)
        num += 1
        logO.info(e)
        #出错之后不能确定位置，退出APP重新进入
        driver = Basepage(device=device, driver='driver', appPackage='com.hpplay.happycast',
                          appActivity='com.hpplay.advertisement.SplashActivity', port=8200,
                          url='http://127.0.0.1:4723/wd/hub')
        driver.Open()
        # time.sleep(10)
        # driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']").click()
