#_*_encoding:GBK*_
# �豸����
# ��ǰ��С���ֻ�  76d92268

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
    device = '76d92268'
    return device

device = device()
# �����ɹ�����
count = 0
# ִ�д���
num = 1
#ʵ����
Perfor_show = Perfor_show()
element = app_element_position()
adb=adb(device=device)
log_path=path()+'logs\\log'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()

# ������־ץȡ
#log.Open('app_link_tv')

driver = Basepage(device=device,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='6')
driver.Open()

time.sleep(3)
display_but = driver.find(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']")
if  display_but == True:
    driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']").click()
else:
    pass

while num < 3001:
    #��������־
    try:
        conetnum = '��ʼִ�е�' + str(num) + '��'
        logO.info(conetnum)
        locat_c = 'adb -s ' + device + ' logcat -c'
        # print(locat_c)
        os.system(locat_c)
        os.system(locat_c)
        find_device = driver.find(MobileBy.XPATH,
                            "//*[@resource-id='com.hpplay.happycast:id/device_name_tv'][contains(@text,'�Ҽҵ��ֲ�Ͷ��')]")
        if find_device == True:
            # �ҵ��豸�󣬵���豸��������
            driver.find_element(MobileBy.XPATH,
                                "//*[@resource-id='com.hpplay.happycast:id/device_name_tv'][contains(@text,'�Ҽҵ��ֲ�Ͷ��')]").click()
        else:
            # com.hpplay.happycast:id/dialog_connect_cancel_btn
            dialog_but = driver.find(MobileBy.XPATH,"//*[@resource-id='com.hpplay.happycast:id/dialog_connect_cancel_btn']")
            if dialog_but == True:
                driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/dialog_connect_cancel_btn']").click()
            else:
                pass
        time.sleep(5)
        # �ж��Ƿ�����Ҫ���صİ�ť  //android.widget.ImageView[@content-desc="����"]
        brack_fan = driver.find(MobileBy.XPATH,
                                 "//android.widget.ImageView[@content-desc='����']")
        if brack_fan == True:
            driver.find_element(MobileBy.XPATH,
                        "//android.widget.ImageView[@content-desc='����']").click()
        else:
            pass
        # ���������ʼ
        start_but = driver.find(MobileBy.XPATH,
                                 "//*[@resource-id='android:id/button1'][contains(@text,'������ʼ')]")
        if start_but == True:
            driver.find_element(MobileBy.XPATH,
                                "//*[@resource-id='android:id/button1'][contains(@text,'������ʼ')]").click()
        else:
            pass
        time.sleep(5)
        # ���ӳɹ��� ץȡlogcat
        lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logpath = log_path + '\\' + device + '-' + lt + '.log'
        op = open(logpath, 'w', encoding='utf-8')
        command2 = 'adb -s ' + device + ' logcat '
        log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)

        time.sleep(15)

        devNull = open(os.devnull, 'w')
        a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
        log.terminate()
        a.wait()
        a.terminate()
        time.sleep(1)

        pass_num = Perfor_show.Intercept_mirror_switch(logpath, "ScreenCastService:onStart",
                                                       "MainActivity: onError")
        print(pass_num)
        if pass_num[0] == True:
            pas = "�����豸����ɹ�"
            print(pas)
            logO.info(pas)
            count+=1
            # ����Ͷ��
            driver.find_element(MobileBy.XPATH, element.APP_disconnect_but).click()
            # ��λ���ȷ��
            time.sleep(2)
            driver.Tap([(750, 1168)])
        else:
            fail = "�����豸����ʧ��"
            print(fail)
            count+=0
            logO.info(fail)
            logO.info(logpath)

        pass_img = "�ɹ�Ͷ���ڣ�" + str(count) + "��"
        logO.info(pass_img)

        time.sleep(15)

        Number = '��ִ�����' + str(num) + '��'  # ����
        logO.info(Number)
        num += 1
    except Exception as e:
        print(e)
        adb.back(2)

        logO.info(e)
        #����֮����ȷ��λ�ã��˳�APP���½���
        driver = Basepage(device=device,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='8')
        driver.Open()
        time.sleep(3)
        display_but = driver.find(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']")
        if display_but == True:
            driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']").click()
        else:
            pass