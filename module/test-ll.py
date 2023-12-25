# coding:utf-8
import unittest
import requests
import os
from lib.common import HTMLTestRunner

class   Music(unittest.TestCase):
    def select(self,name):
        url = 'https://api.apiopen.top/searchMusic'
        data = {
             "name":name
        }
        r = requests.post(url,data=data)
        b = r.json()['result'][0]['title']
        return b

    def test01(self):
        '''
        歌名：断桥残雪
        '''
        b = '断桥残雪'
        a = self.select(b)
        self.assertEqual(b,a)
        print('这个是用例一')

    def test02(self):
        '''
        歌名：说好不哭
        '''
        a = '说好不哭'
        b = self.select(a)
        self.assertEqual(a,b)
        print('这个是用例二')

    def test03(self):
        '''
        歌名：芒种
        '''
        a = '芒种'
        b = self.select(a)
        self.assertEqual(a,b)
        print('这个是用例三')

if __name__ == '__main__':
    # 当前文件夹路径
    report_path = os.path.dirname(os.path.realpath(__file__))
    # 测试报告地址
    report_abspath = os.path.join(report_path, "result.html")
    fp = open(report_abspath, "wb")
     # 报告详情
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,
                                           title=u'自动化测试报告,测试结果如下：',
                                           description=u'用例执行情况：')
    # 实例化
    testunit  = unittest.TestSuite()
    # 加载用例
    testunit .addTests(unittest.TestLoader().loadTestsFromTestCase(Music))
    # 执行用例
    runner.run(testunit)
    # 关闭报告
    fp.close()