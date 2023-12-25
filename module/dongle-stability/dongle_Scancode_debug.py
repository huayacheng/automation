#_*_encoding:GBK*_
# ɨ�����ӡ���debug�汾
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
# sdk���ӳɹ�ʧ��״̬
pa = ""
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



while num < 1001:
    #��������־
    try:
        conetnum = '��ʼִ�е�' + str(num) + '��'
        logO.info(conetnum)
        os.system('adb -s ' + device + ' logcat -c')
        os.system('adb -s ' + device + ' logcat -c')
        # ���ɨ����о���Ͷ��
        saoma = driver.find_element(MobileBy.XPATH,element.APP_scanCode_but)
        saoma.click()
        time.sleep(10)
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
        #�ȴ�ɨ�����
        # Ͷ���ɹ���ץȡlogcat������ ����ɹ���ʧ�ܵĹؼ���

        lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logpath = log_path + '\\' + device + '-' + lt + '.log'
        op = open(logpath, 'w', encoding='utf-8')
        command2 = 'adb -s ' + device + ' logcat '
        log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)

        time.sleep(20)

        devNull = open(os.devnull, 'w')
        a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
        log.terminate()
        a.wait()
        a.terminate()
        time.sleep(1)

        # ͳһ��ȡ��logcat��־֮������ж�
        # SDK���жϣ�sdk�Ƿ������ӳɹ�connectSuccess��sdk���ӳɹ�֮���Ƿ��лص���APP��connectSuccess.callback��
        # onConnectFailed����ʧ��
        sdk_whether_pass = Perfor_show.Intercept_mirror_SDK(logpath,"connectSuccess","connectSuccess.callback","onConnectFailed")
        print(sdk_whether_pass)

        if sdk_whether_pass[0] == True:
            pa = "SDK���ӳɹ�"
            if sdk_whether_pass[1] == 2:
                call = "SKD���ӳɹ��һص���APP"
            else:
                call = "SKD���ӳɹ�δ�ص���APP"
                logO.info(call+logpath)
            print(call)
        else:
            pa = "SDK����ʧ��"
            logO.info(pa + logpath)
        print(pa)
        # ���ж�APP�㣬onStart����ɹ��ص���onError what����ʧ�ܻص���CaptureActivity:connect time out!!ɨ�����ӳ�ʱ
        pass_num = Perfor_show.Intercept_mirror_out(logpath, "ScreenCastService:onStart","HomePageActivity:connect time out!!","HomePageActivity:mirror onError")
        print(pass_num)
        if pass_num[0] == True:
            pas = "�ɹ�ɨ�뾵��"
            print(pas)
            count+=1
            # ����Ͷ��
            driver.find_element(MobileBy.XPATH, element.APP_disconnect_but).click()
            # ��λ���ȷ��
            time.sleep(2)
            driver.Tap([(750, 1168)])
        else:
            if pass_num[1] == 2:
                fail_out = "ɨ�����ӳ�ʱ"
                logO.info(fail_out)
                logO.info(fail_out+logpath)
                count += 0
            else:
                fail = "ɨ�뾵��ʧ��"
                print(fail)
                logO.info(fail)
                logO.info(logpath)
                count+=0

        pass_img = "�ɹ�Ͷ���ڣ�" + str(count) + "��"
        logO.info(pass_img)

        time.sleep(25)

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
