#_*_encoding:GBK*_

# Samsung �ֻ�ר��
# sdk ����

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
# �����ɹ�����
count = 0
# ִ�д���
num = 1
#ʵ����
adb=adb(device=device)
Perfor_show = Perfor_show()
log_path=path()+'logs'
log=Log(log='log',log_path=log_path,device=device)
picture_path=path()+'pictures\\'
screencap=Screencap(path=picture_path,device=device)
run_path=path()+'run_info'
logO=run_log(logger='log',logging_path=run_path).getlog()

# ������־ץȡ
#log.Open('app_link_tv')


# samsung �ֻ�����
driver = Basepage(device=device,driver='driver',version='8',appPackage='com.hpplay.sdk.source.test',appActivity='.MainActivity',port=8200,url='http://127.0.0.1:4723/wd/hub')
driver.Open()
time.sleep(10)

sou = driver.find_element(MobileBy.XPATH,"//*[@resource-id='com.hpplay.sdk.source.test:id/btn_browse']")
sou.click()
time.sleep(10)
tv_xiaomi = driver.find(MobileBy.XPATH,"//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'�ֲ�Ͷ��')]")


while True:
    if tv_xiaomi == True:

        tv_sem = driver.find_element(MobileBy.XPATH,
                                     "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'С���ֲ�Ͷ��')]")
        tv_sem.click()
        break
    else:
        sou.click()
        tv_xiaomi = driver.find(MobileBy.XPATH,
                                "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'С���ֲ�Ͷ��')]")

time.sleep(5)
# ���»���600����
driver.swipeUp(0.3)
time.sleep(3)

# ����Ȩ���Ƿ�����
# time.sleep(8)
# allow = driver.find_element(MobileBy.XPATH,"//*[@resource-id='android:id/button1']")
# allow.click()
# ѭ�����񿪹�
while num < 3001:
    #��������־
    try:
        os.system('adb -s ' + device + ' shell logcat -c ')
        os.system('adb -s ' + device + ' shell logcat -c ')
        # ���񿪹�
        switch_imgages = driver.find_element(MobileBy.XPATH,
                                             "//*[@resource-id='com.hpplay.sdk.source.test:id/mirror_switch']")
        switch_imgages.click()
        # auto = driver.find(MobileBy.XPATH,"//*[contains(@text, '��������')]")
        # if auto == True:
        #     driver.find_element(MobileBy.XPATH, "//*[contains(@text, '��������')]").click()
        # else:
        #     pass
        conetnum = '��ʼִ�е�' + str(num) + '��'
        logO.info(conetnum)
        # tv_sem = driver.find_element(MobileBy.XPATH,"//*[contains(@text,'������ʼ')]")
        # print(tv_sem)
        # tv_sem.click()
        #���뾵��ģʽ����ʼ�ж��Ƿ���뾵��ɹ�
        # ��������Ͷ��ʱ��ʼץȡ��־
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
            # �ж��Ƿ񷵻ص���1,��1�������Ҫ������ץһ��logcat
            # if pass_num[1] == 1:
            #     print(pass_num[1])
            #     time.sleep(1)
            #     switch_imgages2 = driver.find_element(MobileBy.XPATH,
            #                                           "//*[@resource-id='com.hpplay.sdk.source.test:id/mirror_switch']")
            #     # �ر�һ�ξ��񿪹�
            #     if "�ر�" in switch_imgages2.text:
            #         os.system('adb -s ' + device + ' shell logcat -c ')
            #         os.system('adb -s ' + device + ' shell logcat -c ')
            #         switch_imgages2.click()
            #         time.sleep(2)
            #         # ������ʼ
            #         allow = driver.find_element(MobileBy.XPATH, "//*[@resource-id='android:id/button1']")
            #         allow.click()
            #     # ץȡlogcat
            #     lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            #     logpath1 = log_path + '\\' + device + '-' + lt + '.log'
            #     op = open(logpath1, 'w', encoding='utf-8')
            #     command2 = 'adb -s ' + device + ' logcat '
            #     log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)
            #
            #     time.sleep(20)
            #     print(switch_imgages2.text)
            #     # ��ʱ�رյ�ʱ��ֱ�ӿ���
            #     if "�ر�" in switch_imgages2.text:
            #         switch_imgages2.click()
            #         time.sleep(2)
            #         # ������ʼ
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

            # �����ж�,Ͷ��ʱʧ�ܣ����ǳɹ�������δ�ɹ���Ҳδʧ��,Ҳ��Ͷ�����ڼ�����
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
                # ���ж�һ���Ƿ������ɹ�
                pass_num1 = Perfor_show.Intercept_mirror_switch(logpath2, "ScreenCastService:onStart",
                                                               "MainActivity: onError what")
                print(pass_num1)
                if pass_num1[0] == True:
                    print("�ɹ�����")
                    count += 1
                else:
                    print("����ʧ��")
                    screencap.cap("mirror")
                    count += 0
            else:
                count += 0
                logO.info(logpath)
        pass_img = "�ɹ�Ͷ���ڣ�"+str(count)+"��"
        # print(pass_img)
        logO.info(pass_img)
        # while True:
        #     status = driver.find(MobileBy.XPATH, "//*[contains(@text,'�ֲ�Ͷ������ʼ����')]")
        #     if status == True:
        #         print("�ҵ���")
        #         break
        #     else:
        #         print("������")
        #         status = driver.find(MobileBy.XPATH, "//*[contains(@text,'�ֲ�Ͷ������ʼ����')]")
        #
        # �رվ���
        switch_imgages.click()

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
        driver = Basepage(device=device,driver='driver',version='8',appPackage='com.hpplay.sdk.source.test',appActivity='.MainActivity',port=8200,url='http://127.0.0.1:4723/wd/hub')
        driver.Open()
        time.sleep(1)
        sou = driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.hpplay.sdk.source.test:id/btn_browse']")
        sou.click()
        time.sleep(5)
        tv_xiaomi = driver.find(MobileBy.XPATH,
                                "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'С���ֲ�Ͷ��')]")
        # ����С���ֲ�Ͷ�����豸
        while True:
            if tv_xiaomi == True:

                tv_sem = driver.find_element(MobileBy.XPATH,
                                             "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'С���ֲ�Ͷ��')]")
                tv_sem.click()
                break
            else:
                sou.click()
                tv_xiaomi = driver.find(MobileBy.XPATH,
                                        "//*[@resource-id='com.hpplay.sdk.source.test:id/textview'][contains(@text,'С���ֲ�Ͷ��')]")

        time.sleep(1)
        # ���»���600����
        driver.swipeUp(0.3)
        pass
