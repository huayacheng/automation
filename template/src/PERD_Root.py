# -*- coding: utf-8 -*-
# Auther : SHL
# Date : 2022/12/8 16:33
# File : languagesRoot.py
import threading
import time

import tkinter
import os,sys
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
print(BASE_DIR)
rootPath = os.path.split(BASE_DIR)[0]
print(rootPath)
sys.path.append(rootPath)
from tkinter import *
from tkinter import filedialog, ttk,messagebox
from functools import partial
from module.PERD_Form import PERD
from config.operation_url_config import read_write_setting
from selenium.webdriver import ActionChains
import uiautomation as auto
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import xlrd
import openpyxl
import re
from fuzzywuzzy import fuzz
import configparser
import comtypes.client
core = comtypes.client.GetModule("UIAutomationCore.dll")
print(core)
class PERD_UI_run:
    def __init__(self,path_file=None,packaging_file=None,APP_link=None):
        self.path_file = path_file
        self.packaging_file = packaging_file
        self.APP_link = APP_link
        self.operation_app = read_write_setting()
        self.initializer = auto.UIAutomationInitializerInThread()

        if getattr(sys, 'frozen', False):
            self.application_path = os.path.dirname(sys.executable)  # 打包EXE后的运行路径
        elif __file__:
            self.application_path = os.path.abspath(
                os.path.dirname(os.path.dirname(os.getcwd())))  # 未打包时的运行路径 获取到template

    # 上传数据表格
    def upload_file(self,txt):
        '''
        上传文件并显示
        :return:
        '''

        selectFile = filedialog.askopenfilename(title='请选择你要执行的数据表格（section1-7)')  # askopenfilename 1次上传1个；askopenfilenames1次上传多个

        txt.config(font=("宋体", 10), state="normal")
        if txt.get() != None:
            txt.delete(0,tkinter.END)
        txt.insert(0, selectFile)
        txt.config(font=("宋体", 10), state="readonly")
        print(selectFile)
        return selectFile

    # 上传包装数据表格
    def upload_package_file(self, txt):
        '''
        上传文件并显示
        :return:
        '''

        selectFile = filedialog.askopenfilename(
            title='请选择你要执行的包装数据表！')  # askopenfilename 1次上传1个；askopenfilenames1次上传多个

        txt.config(font=("宋体", 10), state="normal")
        if txt.get() != None:
            txt.delete(0, tkinter.END)
        txt.insert(0, selectFile)
        txt.config(font=("宋体", 10), state="readonly")
        print(selectFile)
        return selectFile

    # 写入到前台日志
    def write_log(self,insert_txt,message):
        insert_txt.config(font=("宋体", 10), state="normal", foreground='green')
        insert_txt.insert(END,"【"+message+"】")
        insert_txt.insert(END,"\t")

    # 创建一个线程去执行多语言脚本
    # upload_txt,upload_packging_txt,PERD_url_txt,text_remark
    def create_thread(self,upload_txt,upload_packging_txt,PERD_url_txt,insert_txt):
        run = threading.Thread(target=self.create_upload,args=(upload_txt,upload_packging_txt,PERD_url_txt,insert_txt))
        run.daemon = True
        run.start()

    # 执行自动化
    def create_upload(self,upload_txt,upload_packging_txt,PERD_url_txt,insert_txt):
        self.path_file = upload_txt.get()  # 获取文件目录
        self.packging_file = upload_packging_txt.get()
        self.PERD_URL = PERD_url_txt.get()
        print(self.PERD_URL)

        # module_flag = var.get()
        if not self.path_file:
            messagebox.showinfo("提示","请上传要执行自动化的数据表（section1-7）")
        elif not self.packging_file:
            messagebox.showinfo("提示", "请上传要执行自动化的包装数据表！")
        elif not self.PERD_URL:
            messagebox.showinfo("提示", "请输入执行自动化PERD—APP入口URL！")
        if self.path_file and self.packging_file and self.PERD_URL:
            # self.operation_app.write_set_url(self.PERD_URL)
            self.perd = PERD(self.path_file, self.packging_file,self.PERD_URL)
            # 重新写入软件的名称到配置文件里



            # 开始测试run
            # self.test_languages.run_language()
            # 创建一个新的进程加载执行run_language
            run_lang = threading.Thread(target=self.perd.main_PERD)
            run_lang.daemon = True
            insert_txt.config(font=("宋体", 10), state="normal", foreground='green')
            insert_txt.insert(END, "【PERD】 -- 认证自动化正在执行中...")
            insert_txt.insert(END, "\n")
            insert_txt.see(END)

            run_lang.start()
            danq_txt = "第一"
            while True:
                print("self.perd.cases_end  ",self.perd.cases_end)
                if danq_txt != self.perd.current and self.perd.cases_end == True:
                    print(self.perd.current)
                    danq_txt = self.perd.current
                    insert_txt.config(font=("宋体", 10), state="normal", foreground='green')
                    insert_txt.insert(END, "【PERD】 -- "+self.perd.current+"")
                    insert_txt.see(END)
                    print("self.perd.cases_end  ",self.perd.cases_end)
                    if self.perd.cases_end == True:
                        print("self.perd.results  ",self.perd.results)
                        if self.perd.results == True:
                            insert_txt.tag_config(font=("宋体", 10),tagName='green', foreground='green')
                            insert_txt.insert(END, "  ------ 执行完成！ ")
                            insert_txt.insert(END, "\n")
                            insert_txt.see(END)
                        else:
                            insert_txt.tag_config(font=("宋体", 10),tagName='red', foreground='red')
                            insert_txt.insert(END, "  ------ 执行失败！ ")
                            insert_txt.insert(END, "\n")
                            insert_txt.see(END)

                else:
                    time.sleep(1)
                    print("self.perd.end",self.perd.end)
                    if self.perd.end == True:
                        break
            insert_txt.insert(END, "【PERD】 -- 认证自动化执行完成！！")
            insert_txt.insert(END, "\n")
            insert_txt.see(END)
        # else:
        #     messagebox.showinfo("提示", "输入的表名不存在")

        self.initializer.Uninitialize()

    def Multilingual(self):
        # lang_frame
        langpage = Tk()
        langpage.title("PERD认证自动化工具 V.1.0.0")

        langpage.geometry("%dx%d"%(1300,650))
        genFrame = Frame(langpage, width=1240, height=630)
        # MyFrame=Frame(root,width=700,height=500)
        genFrame.pack_propagate(0)  # 设置为0可使组件大小不变
        genFrame.pack()

        #头部 frame_head ,父窗口大框
        frame_head = Frame(genFrame,width=1300,height=100)
        frame_head.pack(side=TOP,anchor=W,fill=BOTH,expand=YES)

        MyFrame = Frame(genFrame,width=1300,height=350,padx=10)
        MyFrame.pack_propagate(0)  # 设置为0可使组件大小不变
        MyFrame.pack(anchor=SW,fill=BOTH,side=TOP,expand=YES)



        # frame_image 父窗口再frame_head
        frame_image = Frame(frame_head)
        frame_image.grid(row=0,column=1,columnspan=2,sticky='NS',)
        # logo = PhotoImage(file="../libs/logo.png")
        logo = PhotoImage(file=self.application_path+"\\template\public\CompPort2.png")
        label_image = Label(frame_image,image=logo,width=1200)
        label_image.logo = logo
        label_image.grid(row=0,column=1,padx=10,pady=15,columnspan=2,sticky='EW')


        upload = Label(MyFrame, text="上传要执行自动化的数据表：",width=30,border=1,)
        upload.grid(row=1,column=0,padx=10,pady=10,sticky='W')

        upload.config(font=("宋体",12))

        upload_txt = Entry(MyFrame, foreground='red', width=45,border=1,relief="sunken")
        upload_txt.grid(row=1, column=1, padx=10, pady=10,ipadx=10,ipady=5,sticky='NW')
        upload_txt.config(font=("宋体", 10),state="readonly")

        upload_but = Button(MyFrame,foreground='#000',text="上传",width=12,relief=RIDGE,command=partial(self.upload_file,upload_txt))
        upload_but.grid(row=1, column=2, padx=10, pady=10,sticky='W')
        upload_but.config(font=("宋体", 10))

        # 请上传要执行的包装数据表
        upload_packging = Label(MyFrame, text="上传Packaging包装数据表：", width=30, border=1, )
        upload_packging.grid(row=2, column=0, padx=10, pady=5, sticky='W')

        upload_packging.config(font=("宋体", 12))

        upload_packging_txt = Entry(MyFrame, foreground='red', width=35, border=1, relief="sunken")
        upload_packging_txt.grid(row=2, column=1, padx=10, pady=10, ipadx=10, ipady=5, sticky='W')
        upload_packging_txt.config(font=("宋体", 10), state="readonly")

        upload_packging_but = Button(MyFrame, foreground='#000', text="上传", width=8, relief=RIDGE,
                            command=partial(self.upload_file, upload_packging_txt))
        upload_packging_but.grid(row=2, column=2, padx=10, pady=5, sticky='W')
        upload_packging_but.config(font=("宋体", 10))
        # upload_but.bind("<Button-1>",self.upload_file(upload_txt))
        # 输入表名称sheet
        PERD_url = Label(MyFrame,text="输入PERD主路口URL地址：",width=30)
        PERD_url.grid(row=3,column=0,padx=10,pady=10,sticky='W')
        PERD_url.config(font=("宋体", 12))
        spec = StringVar()
        PERD_url_txt = Entry(MyFrame,width=60,relief="sunken",textvariable=spec)
        PERD_url_txt.grid(row=3,column=1,padx=10,pady=5,ipadx=10,columnspan=2,sticky='W',ipady=5)
        PERD_url_txt.config(font=("宋体", 10))
        # spec.set(self.operation_app.web_url)

        # # 下拉多语言选择--语言
        # langs_name = Label(MyFrame,text="选择要测试的多语言语种：",width=25)
        # langs_name.grid(row=3,column=0,padx=10,pady=10,sticky='E')
        # langs_name.config(font=("宋体", 12))
        # education = StringVar()
        # comb_education = ttk.Combobox(MyFrame,
        #                               textvariable=education, width=30)
        # comb_education.grid(row=3, column=1, padx=10, pady=10,sticky='W',ipady=5,ipadx=5)
        # comb_education['value'] = ['English draft', 'S-Chinese', 'T-Chinese', 'French','German','Italian']
        # comb_education.current(1)

        # 文本区域
        frame_remark = Frame(genFrame, width=800, height=100, padx=40)
        frame_remark.pack_propagate(0)  # 设置为0可使组件大小不变
        frame_remark.pack(anchor=W, fill=BOTH, side=TOP, expand=YES)


        scroll_texty = Scrollbar(frame_remark)
        scroll_texty.pack(side=RIGHT,fill=Y)
        # 定义一个显示的多行文本框，显示
        text_remark = Text(frame_remark, width=100,
                           height=15, foreground='green')

        text_remark.tag_add("print", "1.13", "1.15")
        text_remark.config(yscrollcommand=scroll_texty.set) # text绑定垂直滚动条
        text_remark.pack(expand=YES, fill=BOTH)

        scroll_texty.config(command=text_remark.yview)  # 垂直滚动条绑定text



        langu_run = Button(MyFrame,text="执行自动化",width=15,relief=RIDGE,command=partial(self.create_thread,upload_txt,upload_packging_txt,PERD_url_txt,text_remark))
        langu_run.grid(row=3,column=3,padx=3,pady=5,sticky='W',ipadx=1,ipady=1)
        langu_run.config(font=("宋体", 12))







        langpage.mainloop()


if __name__ == '__main__':

    lan = PERD_UI_run()
    lan.Multilingual()