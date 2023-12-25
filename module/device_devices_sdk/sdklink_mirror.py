#_*_encoding:GBK*_

# Samsung 手机专用
# sdk 镜像

import time,os,subprocess
from lib.common.Log import Log
from lib.common.Screencap import Screencap
from lib.common.ADB import adb
from lib.common.Logging import run_log
from lib.common.BasePage import Basepage
from appium.webdriver.common.mobileby import MobileBy
from lib.customlib.Perfor_show import Perfor_show
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
Perfor_show = Perfor_show()
log_path=path()+'logs'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()

# 开启日志抓取
#log.Open('app_link_tv')


# samsung 手机配置
driver = Basepage(device=device,driver='driver',version='8',appPackage='com.hpplay.sdk.source.test',appActivity='.MainActivity',port=8200,url='http://127.0.0.1:4723/wd/hub')
driver.Open()
time.sleep(10)

sou = driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.hpplay.sdk.source.test:id/btn_browse']")
sou.click()
time.sleep(10)
tv_xiaomi = driver.find(MobileBy.XPATH,"//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'乐播投屏')]")


while True:
    if tv_xiaomi == True:

        tv_sem = driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'小米乐播投屏')]")
        tv_sem.click()
        break
    else:
        sou.click()
        tv_xiaomi = driver.find(MobileBy.XPATH,
                                "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'小米乐播投屏')]")

time.sleep(5)
# 向下滑动600像素
driver.swipeUp(0.3)
time.sleep(3)

# 镜像权限是否允许
# time.sleep(8)
# allow = driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/button1']")
# allow.click()
# 循环镜像开关
while num < 3001:
    #先清理日志
    try:
        os.system('adb -s ' + device + ' shell logcat -c ')
        os.system('adb -s ' + device + ' shell logcat -c ')
        # 镜像开关
        switch_imgages = driver.find_element(MobileBy.XPATH,
                                             "//*[@resource-id='com.hpplay.sdk.source.test:id/mirror_switch']")
        switch_imgages.click()
        # auto = driver.find(MobileBy.XPATH,"//*[contains(@text, '总是允许')]")
        # if auto == True:
        #     driver.find_element(MobileBy.XPATH, "//*[contains(@text, '总是允许')]").click()
        # else:
        #     pass
        conetnum = '开始执行第' + str(num) + '次'
        logO.info(conetnum)
        # tv_sem = driver.find_element(MobileBy.XPATH,"//*[contains(@text,'立即开始')]")
        # print(tv_sem)
        # tv_sem.click()
        #进入镜像模式，开始判断是否进入镜像成功
        # 操作镜像投屏时开始抓取日志
        time.sleep(1)
        # adb.right(1)
        # os.system('adb -s' + device + ' shell am start '+page+'')
        lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logpath = log_path + '\\' + device + '-' + lt + '.log'
        op = open(logpath, 'w', encoding='utf-8')
        command2 = 'adb -s ' + device + ' logcat '
        log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)

        time.sleep(7)

        devNull = open(os.devnull, 'w')
        a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
        log.terminate()
        a.wait()
        a.terminate()
        time.sleep(1)

        pass_num = Perfor_show.Intercept_mirror_switch(logpath,"ScreenCastService:onStart","MainActivity: onError what")
        print(pass_num)
        if pass_num[0] == True:
            count+=1
            # os.remove(logpath)
            # 判断是否返回的是1,是1的情况需要重新再抓一次logcat
            # if pass_num[1] == 1:
            #     print(pass_num[1])
            #     time.sleep(1)
            #     switch_imgages2 = driver.find_element(MobileBy.XPATH,
            #                                           "//*[@resource-id='com.hpplay.sdk.source.test:id/mirror_switch']")
            #     # 关闭一次镜像开关
            #     if "关闭" in switch_imgages2.text:
            #         os.system('adb -s ' + device + ' shell logcat -c ')
            #         os.system('adb -s ' + device + ' shell logcat -c ')
            #         switch_imgages2.click()
            #         time.sleep(2)
            #         # 立即开始
            #         allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
            #         allow.click()
            #     # 抓取logcat
            #     lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #     logpath1 = log_path + '\\' + device + '-' + lt + '.log'
            #     op = open(logpath1, 'w', encoding='utf-8')
            #     command2 = 'adb -s ' + device + ' logcat '
            #     log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)
            #
            #     time.sleep(20)
            #     print(switch_imgages2.text)
            #     # 当时关闭的时候，直接开启
            #     if "关闭" in switch_imgages2.text:
            #         switch_imgages2.click()
            #         time.sleep(2)
            #         # 立即开始
            #         allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
            #         allow.click()
            #         time.sleep(30)
            #     devNull = open(os.devnull, 'w')
            #     a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
            #     log.terminate()
            #     a.wait()
            #     a.terminate()
            #     time.sleep(1)
            #     pass2_num = Perfor_show.Intercept_mirror_switch(logpath1, "ScreenCastService:onStart",
            #                                                     "MainActivity:onError what")
            #     print(pass2_num)
            #     if pass2_num[0] == True:
            #         print(pass2_num[1])
            #         count += 1
        else:

            # 新增判断,投屏时失败，还是成功，还是未成功，也未失败,也许投屏正在加载中
            if pass_num[1] == 0:
                lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
                logpath2 = log_path + '\\' + device + '-' + lt + '.log'
                op = open(logpath2, 'w', encoding='utf-8')
                command2 = 'adb -s ' + device + ' logcat '
                log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)

                time.sleep(20)

                devNull = open(os.devnull, 'w')
                a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
                log.terminate()
                a.wait()
                a.terminate()
                logO.info(logpath2)
                # 再判断一次是否上屏成功
                pass_num1 = Perfor_show.Intercept_mirror_switch(logpath2, "ScreenCastService:onStart",
                                                               "MainActivity: onError what")
                print(pass_num1)
                if pass_num1[0] == True:
                    print("成功镜像")
                    count += 1
                else:
                    print("镜像失败")
                    screencap.cap("mirror")
                    count += 0
            else:
                count += 0
                logO.info(logpath)
        pass_img = "成功投屏第："+str(count)+"次"
        # print(pass_img)
        logO.info(pass_img)
        # while True:
        #     status = driver.find(MobileBy.XPATH, "//*[contains(@text,'乐播投屏：开始播放')]")
        #     if status == True:
        #         print("找到了")
        #         break
        #     else:
        #         print("查找中")
        #         status = driver.find(MobileBy.XPATH, "//*[contains(@text,'乐播投屏：开始播放')]")
        #
        # 关闭镜像
        switch_imgages.click()

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
        driver = Basepage(device=device,driver='driver',version='8',appPackage='com.hpplay.sdk.source.test',appActivity='.MainActivity',port=8200,url='http://127.0.0.1:4723/wd/hub')
        driver.Open()
        time.sleep(1)
        sou = driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.sdk.source.test:id/btn_browse']")
        sou.click()
        time.sleep(5)
        tv_xiaomi = driver.find(MobileBy.XPATH,
                                "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'小米乐播投屏')]")
        # 查找小米乐播投屏的设备
        while True:
            if tv_xiaomi == True:

                tv_sem = driver.find_element(MobileBy.XPATH,
                                             "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'小米乐播投屏')]")
                tv_sem.click()
                break
            else:
                sou.click()
                tv_xiaomi = driver.find(MobileBy.XPATH,
                                        "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'小米乐播投屏')]")

        time.sleep(1)
        # 向下滑动600像素
        driver.swipeUp(0.3)
        pass
