# #吧文件从磁盘读到内存，with自动关闭f，节省资源
# with  open('D:\\t金服重构\\test\\case\\baidu4.py','r')  as f:
#     t=f.read()
#
# # print(t)
# # print(type(t))
#     for line in f.readlines():
#         print(line.strip())

# ##写
# with  open('d:\\mhf.txt','a')  as f:
#     f.writelines("today is sunday")

import os
# # print(os.environ)
# # print(os.environ.get('path'))
# p1=os.path.abspath('.')
# p2=os.path.join('D:\\t金服重构\\test\\case','a.txt')
# print(p1)
# print(p2)

# #列出当前目录下的所有目录，只需要一行代码：
# l=[x for x in os.listdir('.')  if os.path.isdir(x)]
# print(l)
# #列出当前目录下所有包含py的文件
# l1=[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
# print(l1)
#

##序列化  把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling    所有的变量是存储在内存中的
##反序列化 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# import pickle
# d=dict(name='bob',score=99,age=20)
# # print(d)
# # d.__getitem__('name')
# # d['name']='mhf'
# # print(d)
# #pickle序列化为字节的内容
# r=pickle.dumps(d)
# print(r)
# #pickle把字节的内容写入磁盘文件中
# f=open('hongfei.txt','wb')
# pickle.dump(d,f)
# f.close()
# #读取磁盘文件到内存，打印出来
# f=open('hongfei.txt','rb')
# t=pickle.load(f)
# f.close()
# print(t)

# ##Json Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON
import json
# d=dict(name='Bob',age=20,score=100)
# s=json.dumps(d)
# print(s)
# print(type(s))
#
# d2=json.loads(s)
# print(d2)
# print(type(d2))

# obj = dict(name='小明', age=20)
# s = json.dumps(obj, ensure_ascii=True)
# print(s)
# class Student(object):
#     def  __init__(self,name,age,score):
#         self.name=name
#         self.age=age
#         self.score=score
#
#     def student2dict(std):
#         return {
#             'name': std.name,
#             'age': std.age,
#             'score': std.score
#         }
# s=Student('小明',20,100)
# #把类的实例序列化为字节内容
# s2=json.dumps(s,default=lambda obj:obj.__dict__)
# print(s2)
# print(type(s2))

