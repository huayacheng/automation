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
# �����ɹ�����
count = 0
# ִ�д���
num = 1
#ʵ����
adb=adb(device=device)
log_path=path()+'logs\\log'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()

# ������־ץȡ
#log.Open('app_link_tv')

driver = Basepage(device=device,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='8')
driver.Open()


# time.sleep(2)
# allow_find = driver.find(MobileBy.XPATH,"//*[@resource-id='android:id/button1']")
# # �մ�app����ҪȨ��
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

# ���ɨ����о���Ͷ��
# saoma = driver.find_element(MobileBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]")
# saoma.click()
# # �˺ŵ�¼
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/pwd_ib']").click()
# # �����û���������
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/mobile_et']").set_text("15820407637")
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/password_et']").set_text("123456")
# time.sleep(4)
# #�����¼
# driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/btn_login']").click()
# time.sleep(10)
while num < 3001:
    #��������־
    try:
        conetnum = '��ʼִ�е�' + str(num) + '��'
        logO.info(conetnum)
        os.system('adb -s ' + device + ' logcat -c')
        os.system('adb -s ' + device + ' logcat -c')
        # ���ɨ����о���Ͷ��
        saoma = driver.find_element(MobileBy.XPATH,
                                    "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.support.v7.app.ActionBar.Tab[2]")
        saoma.click()
        # quan_but = driver.find(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        # if quan_but == True:
        #     # ������ʼ
        #     allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        #     allow.click()
        # else:
        #     pass
        time.sleep(10)
        #�ȴ�ɨ�����
        # adb.back()
        # start_but = driver.find(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        # if start_but == True:
        #     # ������ʼ
        #     allow_start = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
        #     allow_start.click()
        # else:
        #     pass

        # Ͷ���ɹ���ץȡlogcat������ ����ɹ���ʧ�ܵĹؼ���

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
            pas = "�ɹ�ɨ�뾵��"
            print(pas)
            count+=1
            # ����Ͷ��
            driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/cast_stop_tv']").click()
            # ��λ���ȷ��
            time.sleep(2)
            driver.Tap([(750, 1168)])
        else:
            fail = "ɨ�뾵��ʧ��"
            print(fail)
            logO.info(fail)
            logO.info(logpath)
            count+=0

        pass_img = "�ɹ�Ͷ���ڣ�" + str(count) + "��"
        logO.info(pass_img)

        time.sleep(5)

        Number = '��ִ�����' + str(num) + '��'  # ����
        logO.info(Number)
        num += 1
    except Exception as e:
        print(e)
        adb.back(2)
        Number = '��ִ�����' + str(num) + '��'  # ����
        logO.info(Number)
        num += 1
        logO.info(e)
        #����֮����ȷ��λ�ã��˳�APP���½���
        driver = Basepage(device=device, driver='driver', appPackage='com.hpplay.happycast',
                          appActivity='com.hpplay.advertisement.SplashActivity', port=8200,
                          url='http://127.0.0.1:4723/wd/hub')
        driver.Open()
        # time.sleep(10)
        # driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.happycast:id/tips_window_btn']").click()
