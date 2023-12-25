#_*_encoding:GBK*_
# android 发送端基本功能用例
import time,os,subprocess
from lib.common.Log import Log
from lib.common.Screencap import Screencap
from lib.common.ADB import adb
from lib.common.Logging import run_log
from lib.common.BasePage import Basepage
from devices_sdk.element.android_po import element_position
from appium.webdriver.common.mobileby import MobileBy
from lib.customlib.Perfor_show import Perfor_show

class android_sd_example(object):
    # 初始化传值参数
    def __init__(self,devices,version,appPackage,appActivity):
        # devices 设备序列号
        # version 设备版本号
        # appPackage 设备连接的包名
        # appActivity 设备连接的接口
        self.devices = devices
        self.path = os.path.abspath(os.path.join(os.getcwd(), ".."))# 上上级目录：devices_sdk
        self.adb=adb(device=self.devices)
        self.log_path=self.path+'\\logs'
        self.log = self.path + '\\log'
        self.picture_path = self.path + '\\pictures\\'
        self.screencap = Screencap(path=self.picture_path, device=self.devices)
        # self.run_path = self.path + '\\run_info'
        # self.logO=run_log(logger='log',logging_path=self.run_path).getlog()
        # 设备端APPium配置
        self.driver = Basepage(device=devices,driver='driver',version=version,appPackage=appPackage,appActivity=appActivity,port=8200,url='http://127.0.0.1:4723/wd/hub')
        # 定位地址
        self.element = element_position()
    def positionXpath(self,pt):
        em_pt = self.driver.find_element(MobileBy.XPATH,pt)
        return em_pt
    def positionFind(self,pt):
        em_fd = self.driver.find(MobileBy.XPATH,pt)
        return em_fd
    def logcat_Intercept(self):
        lt = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        logpath = self.log_path + '\\' + self.devices + '-' + lt + '.log'
        op = open(logpath, 'w', encoding='utf-8')
        command2 = 'adb -s ' + self.devices + ' logcat '
        log = subprocess.Popen(command2, stdout=op, stderr=subprocess.PIPE)

        time.sleep(25)

        devNull = open(os.devnull, 'w')
        a = subprocess.Popen('taskkill /t/f/pid %s' % log.pid, stdout=devNull, stderr=subprocess.PIPE)
        log.terminate()
        a.wait()
        a.terminate()
        time.sleep(1)
        return logpath
    # 当打开app出现的烦人的弹出框时
    def pop_box(self):
        pop_but = self.positionFind(self.element.sdk_but_allow)
        if pop_but == True:
            self.positionXpath(self.element.sdk_but_allow).click()
        else:
            pass
        self.driver.swipeUp(0.38)
        time.sleep(15)
    def test1(self):
        # 操作步骤
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()

    def test2(self):
        # 网络视频推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()

    def test3(self):
        # 网络音乐推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        inmusic = self.positionXpath(self.element.sdk_rbtn_inmusic)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        inmusic.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()

    def test4(self):
        # 网络图片推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        inpicture = self.positionXpath(self.element.sdk_rbtn_inpicture)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        inpicture.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()

    def test5(self):
        # 网络本地视频推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        localvideo = self.positionXpath(self.element.sdk_rbtn_localvideo)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        localvideo.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        but_dsy = self.positionFind(self.element.sdk_btn_autho)
        but_autho = self.positionXpath(self.element.sdk_btn_autho)
        if but_dsy == True:
            but_autho.click()
        else:
            pass
    def test6(self):
        # 网络本地音乐推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        localmusic = self.positionXpath(self.element.sdk_rbtn_localmusic)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        localmusic.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        but_dsy = self.positionFind(self.element.sdk_btn_autho)
        but_autho = self.positionXpath(self.element.sdk_btn_autho)
        if but_dsy == True:
            but_autho.click()
        else:
            pass

    def test7(self):
        # 网络本地图片推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        localpicture = self.positionXpath(self.element.sdk_rbtn_localpicture)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        localpicture.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        but_dsy = self.positionFind(self.element.sdk_btn_autho)
        but_autho = self.positionXpath(self.element.sdk_btn_autho)
        if but_dsy == True:
            but_autho.click()
        else:
            pass

    def test8(self):
        # 网络视频推送,暂停，播放成功
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)

        self.click = video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        time.sleep(15)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(5)

    def test9(self):
        # 网络视频推送,增加音量
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)

        self.click = video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        time.sleep(15)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(5)

    def test10(self):
        # 网络视频推送,减少音量
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)

        self.click = video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        time.sleep(15)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(5)

    def test11(self):
        # 网络视频推送,进度手动调节
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)

        self.click = video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        time.sleep(15)
        self.driver.swipeUp(0.3)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(1)
        seekbar_progress = self.positionXpath(self.element.sdk_seekbar_progress)
        self.driver.move_seekbar(seekbar_progress,0.6)

    def test12(self):
        # 网络视频推送,进度手动调节声音
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)

        self.click = video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        time.sleep(15)
        self.driver.swipeUp(0.3)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(1)
        seekbar_volume = self.positionXpath(self.element.sdk_seekbar_volume)
        self.driver.move_seekbar(seekbar_volume,0.2)



    def test13(self):
        # 网络视频推送,进度手动调节
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        self.driver.swipeUp(0.1)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(2)
        self.positionXpath(self.element.sdk_mirror_switch).click()
        time.sleep(4)
        # 首次加载判断
        allow_but_find = self.positionFind(self.element.sdk_but_allow)
        allow_but = self.positionXpath(self.element.sdk_but_allow)
        if allow_but_find == True:
            allow_but.click()
            time.sleep(2)
            allow_but_find = self.positionFind(self.element.sdk_but_allow)
            allow_but = self.positionXpath(self.element.sdk_but_allow)
            if allow_but_find == True:
                allow_but.click()
            else:
                pass
        else:
            pass


    def test14(self):
        # 网络视频推送,结束播放，再次推送
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()
        lebo_t = self.positionFind(self.element.sdk_text_lebo)
        while True:
            if lebo_t == True:
                lebo_text = self.positionXpath(self.element.sdk_text_lebo)
                lebo_text.click()
                break
            else:
                search = self.positionXpath(self.element.sdk_btn_browse)
                search.click()
                lebo_t = self.positionFind(self.element.sdk_text_lebo)
        video = self.positionXpath(self.element.sdk_rbtn_invideo)

        self.click = video.click()
        play = self.positionXpath(self.element.sdk_but_play)
        play.click()
        time.sleep(15)
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        os.system('adb -s ' + self.devices + ' shell logcat -c ')
        time.sleep(2)
        # 视频播放中，结束播放
        self.positionXpath(self.element.sdk_but_stop).click()
        # 等几秒后，再重新推送
        time.sleep(3)
        play.click()

# if __name__ == '__main__':
#     test = android_sd_example(devices="76d92268",version="6",appPackage="com.hpplay.sdk.source.test",appActivity='.MainActivity')
#     test.test13()










