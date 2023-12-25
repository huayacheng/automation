#_*_encoding:GBK*_
# android ���Ͷ˻�����������
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
    # ��ʼ����ֵ����
    def __init__(self,devices,version,appPackage,appActivity):
        # devices �豸���к�
        # version �豸�汾��
        # appPackage �豸���ӵİ���
        # appActivity �豸���ӵĽӿ�
        self.devices = devices
        self.path = os.path.abspath(os.path.join(os.getcwd(), ".."))# ���ϼ�Ŀ¼��devices_sdk
        self.adb=adb(device=self.devices)
        self.log_path=self.path+'\\logs'
        self.log = self.path + '\\log'
        self.picture_path = self.path + '\\pictures\\'
        self.screencap = Screencap(path=self.picture_path, device=self.devices)
        # self.run_path = self.path + '\\run_info'
        # self.logO=run_log(logger='log',logging_path=self.run_path).getlog()
        # �豸��APPium����
        self.driver = Basepage(device=devices,driver='driver',version=version,appPackage=appPackage,appActivity=appActivity,port=8200,url='http://127.0.0.1:4723/wd/hub')
        # ��λ��ַ
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
    # ����app���ֵķ��˵ĵ�����ʱ
    def pop_box(self):
        pop_but = self.positionFind(self.element.sdk_but_allow)
        if pop_but == True:
            self.positionXpath(self.element.sdk_but_allow).click()
        else:
            pass
        self.driver.swipeUp(0.38)
        time.sleep(15)
    def test1(self):
        # ��������
        self.driver.Open()
        self.pop_box()
        search = self.positionXpath(self.element.sdk_btn_browse)
        search.click()

    def test2(self):
        # ������Ƶ����
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
        # ������������
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
        # ����ͼƬ����
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
        # ���籾����Ƶ����
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
        # ���籾����������
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
        # ���籾��ͼƬ����
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
        # ������Ƶ����,��ͣ�����ųɹ�
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
        # ������Ƶ����,��������
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
        # ������Ƶ����,��������
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
        # ������Ƶ����,�����ֶ�����
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
        # ������Ƶ����,�����ֶ���������
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
        # ������Ƶ����,�����ֶ�����
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
        # �״μ����ж�
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
        # ������Ƶ����,�������ţ��ٴ�����
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
        # ��Ƶ�����У���������
        self.positionXpath(self.element.sdk_but_stop).click()
        # �ȼ��������������
        time.sleep(3)
        play.click()

# if __name__ == '__main__':
#     test = android_sd_example(devices="76d92268",version="6",appPackage="com.hpplay.sdk.source.test",appActivity='.MainActivity')
#     test.test13()










