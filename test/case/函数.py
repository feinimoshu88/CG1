#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# def add_L(l=None):
#     if l is None:
#         l=[]
#         l.append("end")
#     return l
# print(add_L())
#
# def add_L(l=[]):
#     l.append("end")
#     return l
# print(add_L())
# print(add_L())
# #求1*1+2*2+3*3+。。。   函数的参数是可变的时  用*号  ok
# def r_sum(*l):
#     sum=0
#     for i in l:
#         sum=sum+i*i
#     return sum
# print(r_sum())
# print(r_sum(1))
# print(r_sum(1,2,3))
# l=[1,2,3,4]
# print(r_sum(*l))

#函数迭代
# #求list中的最大值最小值返回tuple
# list=[-2,-1,0,1,2,3,4,5,6,7,8,9,10]
# n=len(list)
# for i in list:
#     if i<list[n-1]:
#         i=list[n-1]
#         n=n-1
# max=i
# print(max)
# for i in list:
#     if i>=list[n-1]:
#         i=list[n-1]
#         n=n-1
# min=i
# print(min)
# l2=[]
# l2.append(max)
# l2.append(min)
# t=tuple(l2)
# print(t)

#封装成一个函数
# #求list中的最大值最小值返回tuple
# def max_min(list):
#     n=len(list)
#     for i in list:
#         if i<list[n-1]:
#             i=list[n-1]
#             n=n-1
#     max=i
#     for i in list:
#         if i>=list[n-1]:
#             i=list[n-1]
#             n=n-1
#     min=i
#     l2=[]
#     l2.append(max)
#     l2.append(min)
#     t=tuple(l2)
#     return t
# list1=[-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,23]
# print(max_min(list1))

# #list生成式
# l=list(range(1,10))
# print(l)
# l2=[x*x for x in range(1,5)]
# print(l2)
# #两层循环，排列组合
# l3=[x+y for x in"abc" for y in "xyz"]
# print(l3)

# #list生成器
# l=(x*x for x in range(1,5))
# print(l)
# #调用生成器里的值
# # print(next(l))
# for i in l:
#     print(i)

# #迭代器：
# from collections import Iterable, Iterator
#
# #判断一个对象是否是可迭代对象
# print(isinstance([],Iterable))
# print(isinstance([x for x in range(1,6)],Iterable))
# # list dic str是Iterable 不是Iterator
# print(isinstance([],Iterator))
# #iter()可以把Iterable 变成Iterator
# print(isinstance(iter([]),Iterator))
#高阶函数
# #变量可以指向函数
# print(abs)
# print(abs(-1))
# f=abs
# print(f)
# print(f(-9))
#函数名就是变量

# #参数传入函数
# f=abs
# def s(x,y,f):
#     return f(x)+f(y)
# a=s(-1,-2,f)
# print(a)

#map(f,list) 把f函数作用于list中的每个元素并返回一个iterrator
# def f(x):
#     return x*x
# l=map(f,[1,2,3,4,5])
# #l是惰性序列，list(l)可以把整个序列计算出来并返回一个list
# print(list(l))
####
# #把列表中所有的数字转换为字符串
# a=list(map(str,[1,2,3,4,5]))
# print(a)
# #求一个序列的和
# print(sum([1,2,3,4,5]))
#
# #排序
# list=[-3,9,0,5,6,4,-8,-19]
# print(sorted(list))
# #根据绝对值来排序
# print(sorted(list,key=abs))
# print('原来的序列是：',list)

##返回一个函数
#求几个数之和
# def sum1(*args):
#     s1=0
#     for i in args:
#         s1=s1+i
#     return s1
# print(sum1(1,2,3))

# ##返回一个函数   返回一个函数
# def lazy_sum(*args):
#     def sum2():
#         s2=0
#         for i in args:
#             s2=s2+i
#         return s2
#     return sum2
# print(lazy_sum())
# f=lazy_sum(1,2)
# print(f())

# #匿名函数
# a=list(map(lambda x:x*x,[1,2,3,4,5]))
# print(a)

# #装饰器
# def now():
#     print("2018-10")
# f=now
# f()
# #f._name_获取函数的名称
# print(f.__name__)
#####
# #装饰器，在函数运行期间动态增加功能  是一个返回函数的高阶函数
# def log(func):
#     def w(*args,**kw):
#         print("call :")
#         return func(*args,**kw)
#     return w
# @log
# def now():
#     print("2018-10")
# now()
# ####格式化输出
# print('%s'%('你好'))
# print('%s:'%('你好'))
# print('%s,%s'%('你好','today'))

# ##三层嵌套
# def log(text):
#     def derector(func):
#         def wrap(*args,**kwargs):
#             print('%s:%s'%(text,func.__name__))
#             return func(*args,**kwargs)
#         return wrap
#     return derector
# @log('exe')
# def now():
#     print("2018-10-25")
# now()

# ###偏函数
# print(int('123',8))

# ##format格式化函数
# print("qq")
# a="{}:{}".format("hello","world")
# print(a)

# ###模块
# import sys
# def test():
#     argv=sys.argv
#     if len(argv==1):
#         print("one argv!")
#     elif len(argv==2):
#         print("two argvs!")
#     else:
#         print("too many argvs!")
# if __name__ == '__main__':
#     test()
from test1.case.hello import test
test()