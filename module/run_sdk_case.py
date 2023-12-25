# coding:utf-8
from lib.common.slide_class import slide
from android_Basic import *
from lib.common.HTMLTestRunner import *

class test_Sdk_Dome(unittest.TestCase):


    def setUp(self):
        self.test = android_sd_example(devices="76d92268",version="6",appPackage="com.hpplay.sdk.source.test",appActivity='.MainActivity')

    def tearDown(self):
        self.test.driver.Quit()
    def test_01(self):
        ''' SDK搜索到TV接收端信号 '''
        self.test.test1()
        lebo_text = self.test.positionXpath(self.test.element.sdk_text_lebo)
        try:
            result = self.assertIn("乐播投屏", lebo_text.text)
            if result == None:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息："+msg)

    def test_02(self):
        ''' SDK推送在线视频到TV接收端播放 '''
        #推送结果判断
        self.test.test2()
        logpath = self.test.logcat_Intercept()
        pass_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertTrue(pass_num)
        try:
            if pass_num[0] == True:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息："+msg)
        # 推送完成后关掉，推送的视频
        self.test.positionXpath(self.test.element.sdk_but_stop).click()
    def test_03(self):
        ''' SDK推送在线音乐到TV接收端播放 '''
        #推送结果判断
        self.test.test3()
        logpath = self.test.logcat_Intercept()
        pass_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertFalse(pass_num)
        try:
            if pass_num[0] == True:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息："+msg)
        # 推送完成后关掉，推送的视频
        self.test.positionXpath(self.test.element.sdk_but_stop).click()
    def test_04(self):
        ''' SDK推送网络图片到TV接收端播放 '''
        self.test.test4()
        logpath = self.test.logcat_Intercept()
        pass_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertTrue(pass_num)
        try:
            if pass_num[0] == True:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息：" + msg)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()
    def test_05(self):
        ''' SDK推送本地视频到TV接收端播放 '''
        self.test.test5()
        logpath = self.test.logcat_Intercept()
        pass_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertTrue(pass_num)
        try:
            if pass_num[0] == True:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息：" + msg)

        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_06(self):
        ''' SDK推送本地音乐到TV接收端播放 '''
        self.test.test6()
        logpath = self.test.logcat_Intercept()
        pass_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertTrue(pass_num)
        try:
            if pass_num[0] == True:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息：" + msg)

    def test_07(self):
        ''' SDK推送本地图片到TV接收端播放 '''
        self.test.test7()
        logpath = self.test.logcat_Intercept()
        pass_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertFalse(pass_num)
        self.a
        try:
            if pass_num[0] == True:
                print("用例成功")
            else:
                print("用例失败")
        except Exception as msg:
            print("错误信息：" + msg)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_08(self):
        ''' SDK推送视频到TV端播放，点击暂停，之后再点击播放'''
        self.test.test8()

        # 开启暂停
        self.test.positionXpath(self.test.element.sdk_but_pause).click()
        time.sleep(5)
        # 在开启播放
        self.test.positionXpath(self.test.element.sdk_but_play).click()
        logpath = self.test.logcat_Intercept()
        # 暂停返回值
        screenshot_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:pause result")
        # 重新播放返回值
        pass_num = Perfor_show.Intercept_mirror_switch_play(logpath, "NewLelinkPlayerControl:resume result")
        self.assertTrue(pass_num)
        try:
            if screenshot_num[0] == True and pass_num[0] == True:
                print('暂停成功,重新播放成功')
            else:
                print('暂停失败')
        except Exception as e:
            print(e)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_09(self):
        ''' SDK推送视频到TV端播放，播放后点击增加音量控制 '''
        self.test.test9()
        time.sleep(4)
        # 增加音量
        volume_up = self.test.positionXpath(self.test.element.sdk_but_volume_up)
        volume_up.click()
        volume_up.click()
        time.sleep(1)
        logpath = self.test.logcat_Intercept()
        # 根据logcat关键判断音量增加成功  返回值
        volume_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:addVolume result")
        self.assertTrue(volume_num)
        try:
            if volume_num[0] == True:
                print('增加音量成功')
            else:
                print('增加音量失败')
        except Exception as e:
            print(e)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_10(self):
        ''' SDK推送视频到TV端播放，播放后点击减少音量控制 '''
        self.test.test10()
        time.sleep(4)
        # 增加音量
        volume_down = self.test.positionXpath(self.test.element.sdk_but_volume_down)
        volume_down.click()
        volume_down.click()
        time.sleep(1)
        logpath = self.test.logcat_Intercept()
        # 根据logcat关键判断音量减少成功  返回值
        volume_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:subVolume result")
        self.assertFalse(volume_num)
        try:
            if volume_num[0] == True:
                print('减少音量成功')
            else:
                print('减少音量失败')
        except Exception as e:
            print(e)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_11(self):
        ''' SDK推送视频到TV端播放，播放后手动调节进度条 '''
        self.test.test11()
        time.sleep(2)
        # 打印logcat文件
        logpath = self.test.logcat_Intercept()
        # 根据logcat关键判断进度条滑动  返回值
        seekbar_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:seek callback result")
        self.assertTrue(seekbar_num)
        try:
            if seekbar_num[0] == True:
                print('手动调节进度条成功')
            else:
                print('手动调节进度条失败')
        except Exception as e:
            print(e)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_12(self):
        ''' SDK推送视频到TV端播放，播放后手动调节声音进度条控制 '''
        self.test.test12()
        time.sleep(2)
        # 打印logcat文件
        logpath = self.test.logcat_Intercept()
        # 根据logcat关键判断进度条滑动  返回值
        seekbar_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:result")
        self.assertTrue(seekbar_num)
        try:
            if seekbar_num[0] == True:
                print('手动调节声音进度条成功')
            else:
                print('手动调节声音进度条失败')
        except Exception as e:
            print(e)
        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

    def test_13(self):
        ''' SDK 开启镜像投屏 '''
        self.test.test13()
        time.sleep(5)
        # 打印logcat文件
        logpath = self.test.logcat_Intercept()
        # 根据logcat关键判断进度条滑动  返回值
        pass_num = Perfor_show.Intercept_mirror_switch(logpath,"ScreenCastService:onStart","MainActivity: onError what")
        self.assertTrue(pass_num)
        try:
            if pass_num[0] == True:
                print('镜像成功')
            else:
                print('镜像失败')
        except Exception as e:
            print(e)
        # 推送完成后关掉镜像
        self.test.positionXpath(self.test.element.sdk_mirror_switch).click()

    def test_14(self):
        ''' SDK推送视频到TV端播放，停止播放后，再重新开始播放 '''
        self.test.test14()
        time.sleep(2)
        # 打印logcat文件
        logpath = self.test.logcat_Intercept()
        # 根据logcat关键判断视频是否结束播放  返回值
        seekbar_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:stop result")
        self.assertTrue(seekbar_num)
        try:
            if seekbar_num[0] == True:
                print('结束播放成功')
            else:
                print('结束播放失败')
        except Exception as e:
            print(e)

        # 根据logcat关键判断是否重新播放  返回值
        paly_num = Perfor_show.Intercept_mirror_switch_code(logpath, "NewLelinkPlayerControl:send play order result")
        self.assertTrue(paly_num)
        try:
            if paly_num[0] == True:
                print('播放成功')
            else:
                print('播放失败')
        except Exception as e:
            print(e)

        # 推送完成后关掉
        self.test.positionXpath(self.test.element.sdk_but_stop).click()

if __name__ == '__main__':
    # unittest.main()
    # suite = unittest.TestSuite()
    # suite.addTest(test_Sdk_Dome('test_14'))
    # # 执行测试
    #
    # runner = unittest.TextTestRunner()
    #
    # runner.run(suite)
    # 指定文件生产的目录
    log_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    print(log_path)
    # 测试报告的路径
    report_path = os.path.join(log_path+"\\log", "result.html")
    fp = open(report_path, "wb")
    # 报告详情
    runner = HTMLTestRunner(stream=fp,verbosity=2,title='自动化测试报告,测试结果如下：',description='用例执行情况：')

    # 实例化
    testunit = unittest.TestSuite()
    # 加载用例
    testunit.addTests(unittest.TestLoader().loadTestsFromTestCase(test_Sdk_Dome))
    # 执行用例
    runner.run(testunit)
    # 关闭报告
    fp.close()

