#_*_encoding:GBK*_
# 扫码连接——debug版本
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
# 计数成功次数
count = 0
# 执行次数
num = 1
# sdk连接成功失败状态
pa = ""
#实例化
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

driver = Basepage(device=device,driver='driver',appPackage='com.hpplay.happycast',appActivity='com.hpplay.advertisement.SplashActivity',port=8200,url='http://127.0.0.1:4723/wd/hub',version='6')
driver.Open()



while num < 1001:
    #先清理日志
    try:
        conetnum = '开始执行第' + str(num) + '次'
        logO.info(conetnum)
        os.system('adb -s ' + device + ' logcat -c')
        os.system('adb -s ' + device + ' logcat -c')
        # 点击扫码进行镜像投屏
        saoma = driver.find_element(MobileBy.XPATH,element.APP_scanCode_but)
        saoma.click()
        time.sleep(10)
        # 判断是否有需要返回的按钮  //android.widget.ImageView[@content-desc="返回"]
        brack_fan = driver.find(MobileBy.XPATH,
                                "//android.widget.ImageView[@content-desc='返回']")
        if brack_fan == True:
            driver.find_element(MobileBy.XPATH,
                                "//android.widget.ImageView[@content-desc='返回']").click()
        else:
            pass
        # 点击立即开始
        start_but = driver.find(MobileBy.XPATH,
                                "//*[@resource-id='android:id/button1'][contains(@text,'立即开始')]")
        if start_but == True:
            driver.find_element(MobileBy.XPATH,
                                "//*[@resource-id='android:id/button1'][contains(@text,'立即开始')]").click()
        else:
            pass
        #等待扫码完成
        # 投屏成功后抓取logcat，拦截 镜像成功和失败的关键字

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

        # 统一在取到logcat日志之后进行判断
        # SDK层判断，sdk是否已连接成功connectSuccess，sdk连接成功之后是否有回调给APP层connectSuccess.callback，
        # onConnectFailed连接失败
        sdk_whether_pass = Perfor_show.Intercept_mirror_SDK(logpath,"connectSuccess","connectSuccess.callback","onConnectFailed")
        print(sdk_whether_pass)

        if sdk_whether_pass[0] == True:
            pa = "SDK连接成功"
            if sdk_whether_pass[1] == 2:
                call = "SKD连接成功且回调到APP"
            else:
                call = "SKD连接成功未回调给APP"
                logO.info(call+logpath)
            print(call)
        else:
            pa = "SDK连接失败"
            logO.info(pa + logpath)
        print(pa)
        # 再判断APP层，onStart镜像成功回调，onError what镜像失败回调，CaptureActivity:connect time out!!扫码连接超时
        pass_num = Perfor_show.Intercept_mirror_out(logpath, "ScreenCastService:onStart","HomePageActivity:connect time out!!","HomePageActivity:mirror onError")
        print(pass_num)
        if pass_num[0] == True:
            pas = "成功扫码镜像"
            print(pas)
            count+=1
            # 结束投屏
            driver.find_element(MobileBy.XPATH, element.APP_disconnect_but).click()
            # 定位点击确定
            time.sleep(2)
            driver.Tap([(750, 1168)])
        else:
            if pass_num[1] == 2:
                fail_out = "扫码连接超时"
                logO.info(fail_out)
                logO.info(fail_out+logpath)
                count += 0
            else:
                fail = "扫码镜像失败"
                print(fail)
                logO.info(fail)
                logO.info(logpath)
                count+=0

        pass_img = "成功投屏第：" + str(count) + "次"
        logO.info(pass_img)

        time.sleep(25)

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
