# coding=utf-8
# x=input("x:")
# y=input("y:")
# print(int(x)*int(y))

# if 1==2:
#     print("one equals two")
# if 1==1:
#     print("one equals one")

# print(pow(2,3))
# print(abs(-10))
# print(round(1.0/2.0))
#模块.函数
# import math
# a=math.floor(32.9)
# print(a)
# print(type(a))
# from math import floor,ceil,sqrt
# b=floor(32.9)
# print(b)
# print(ceil(32.9))
# print(sqrt(9))
# foo=sqrt
# print(foo(16))
# print(foo(-1))

# print("hello world!")
# print("let's go!")

# name=input("what is your name?")
# print("hello,"+name+"!")
# #原始字符串
# print(r"F:\f盘\mhf_python\f0ksok\data")
# #Unicode字符串
# print(u"hello world")
# print("""this is a
# very long string,
# hello world
# """)

# print(round(3.9337373)) #四舍五入
# s="hello"
# print(s[0])

# l=list(range(10))
# print(l)
# print(type(l))
# print(l[1:3])
# print(l[-3:])
# print(l[:3])
# #步长
# print(l[0:10:2])
# print(l[10:0:-1])
# l2=list(range(5))
# print(l2)
# print(l+l2)
# s=[None]*10
# print(s)
#in  在列表中
# p="rw"
# print("r"in p)
# print("x" in p)

# print(max([3,5,6]))
# print(min([1,2,3]))
#
# li1=list("hello")
# print(li1)
# #将list转换为字符串
# s="".join(li1)
# print(s)
# print(type(s))

# #针对键是字符串的字典，的格式化
# p={'zhangsan':"张三","lisi":"李四"}
# # print("his name is %(zhangsan)s" % p)
# # print(p['name'])
# #访问不存在的key值时不会报错，使用index访问不存在时会报错
# print(p.get('name'))

# print(bool(111))
# print(bool())

# names=input("what is your name?") or "unkonwn"
# if names.endswith("san"):
#     print("hello ","san")
# else:
#     print("hello,",names)

#三元运算符 a if  b else c

# # age=-1
# age=10
# assert 0<age<100

# #循环
# i=0
# while i <100:
#     print(i)
#     i+=1

# l=["zhangsan","lisi","wangwu"]
# for i in  l:
#     print(i)
#能用for就不用while

d={"x":1,"y":2,"z":3}
# for key in d:
#     print(key)
#     # print(d[key])
# #获取字典的元素
# for key,value in d.items():
#     print(key,"=",value)
#

# # #压缩函数
# names=["zhangsan","lisi","wangwu"]
# ages=[18,19,20]
# # for i in range(len(names)):
# #     print(names[i],"is",ages[i])
# d=list(zip(names,ages))
# print(d)
# # #解包zip
# # for name,age in d:
# #     print(name,"is",age,"years old")

# #xrange 比 range效率高，是一个一个创建的
# print(list(zip(range(5),range(10))))

# old_string="a dadaldasdl ldfad  loiiu3ou  kkk kie3 33n t"
# # for index,string in enumerate(old_string):
# #    print(index,"is",string)
# # print(old_string)

