# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test1111',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')

# ####内建模块
# from datetime import datetime
# print(datetime.now())
# ##namedtuple
# from collections import namedtuple
# Point=namedtuple('Point',['x','y'])
# p=Point(1,2)
# print(p.x,p.y)
# print(isinstance(p,tuple))
# print(isinstance(p,Point))

# from PIL import Image, ImageFilter
# i1=Image.open('1.jpg')
# # i2=i1.save('123.jpg','jpeg')
# i2=i1.filter(ImageFilter.BLUR)
# i3=i2.save('3.jpg','jpeg')
# ##运维监控系统信息
# import psutil as psutil
# # a=psutil.cpu_count()
# a=psutil.cpu_count(logical=False)
# print(a)
#
# print(psutil.cpu_times())
# print(psutil.net_connections())
#
# ##图形界面的用法：
# from tkinter import *
# import tkinter.messagebox as messagebox
#
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()
#
#     def createWidgets(self):
#         self.nameInput = Entry(self)
#         self.nameInput.pack()
#         self.alertButton = Button(self, text='Hello', command=self.hello)
#         self.alertButton.pack()
#
#     def hello(self):
#         name = self.nameInput.get() or 'world'
#         messagebox.showinfo('Message', 'Hello, %s' % name)
#
# app = Application()
# # 设置窗口标题:
# app.master.title('Hello World')
# # 主消息循环:
# app.mainloop()
#
