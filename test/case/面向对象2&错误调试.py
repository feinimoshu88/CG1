# # class Student(object):
# #     @property
# #     def score(self):
# #         return self._score
# #     @score.setter
# #     def score(self, value):
# #         self._score = value
# # # s=Student("zhangsan",100)
# # # print(s.score)
# # # s.set_score(90)
# # # print(s.score)
# # s=Student()
# # s.score=99
# # print(s.score)
# #####简化类的set方法，和get属性方法
#
# # class Student(object):
# #     @property
# #     def score(self):
# #         return self._score
# #     @score.setter
# #     def score(self, value):
# #         # if not isinstance(value, int):
# #         #     raise ValueError('score must be an integer!')
# #         # if value < 0 or value > 100:
# #         #     raise ValueError('score must between 0 ~ 100!')
# #         self._score = value
# # s=Student()
# # s.score=100
# # print(s.score)
#
# # class Student(object):
# #     def __init__(self,name):
# #         self.name=name
# #     #添加__call__方法，可以直接调用类的实例 s()
# #     def __call__(self):
# #         print("My name is %s" %self.name)
# # s=Student("ZS")
# # s()
# # #通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
# # print(callable(s))
# # print(callable("abc"))
# ####异常
# # try:
# #     a=10/1
# #     # a=10/0
# #     # a=10/int('a')
# #     print(a)
# # except ZeroDivisionError as e:
# #     print("exception:",e)
# # except ValueError as e:
# #     print("exception:",e)
# # else:
# #     print('no error!')
# # finally:
# #     print('finally')
# # print('end')
#
# ## err.py:
#
# # ##用logging记录错误
# # import logging
# # def foo(s):
# #     return 10 / int(s)
# # def bar(s):
# #     return foo(s) * 2
# # def main():
# #     try:
# #         bar('0')
# #     except Exception as e:
# #         logging.exception(e)
# # main()
# # print("end")
#
# # ##抛自定义的错误
# # class Myerror(ValueError):
# #     pass
# # def foo(s):
# #     if s==0:
# #         raise Myerror(s)
# # foo(0)
# # print('end')
# #
# # #使用日志记录错误信息
# # import logging
# # # logging.basicConfig(level=logging.INFO)
# # s='0'
# # r=10/int(s)
# # # logging.exception(ValueError)
# # logging.info(r)
#
# ##文档测试doctest
# # mydict2.py
# class Dict(dict):
#     '''
#     Simple dict but also support access as x.y style.
#
#     >>> d1 = Dict()
#     >>> d1['x'] = 100
#     >>> d1.x
#     100
#     >>> d1.y = 200
#     >>> d1['y']
#     200
#     >>> d2 = Dict(a=1, b=2, c='3')
#     >>> d2.c
#     '3'
#     >>> d2['empty']
#     Traceback (most recent call last):
#         ...
#     KeyError: 'empty'
#     >>> d2.empty
#     Traceback (most recent call last):
#         ...
#     AttributeError: 'Dict' object has no attribute 'empty'
#     '''
#     def __init__(self, **kw):
#         super(Dict, self).__init__(**kw)
#
#     # def __getattr__(self, key):
#     #     try:
#     #         return self[key]
#     #     except KeyError:
#     #         raise AttributeError(r"'Dict' object has no attribute '%s'" % key)
#
#     def __setattr__(self, key, value):
#         self[key] = value
#
# if __name__=='__main__':
#     import doctest
#     doctest.testmod()

##第二个文档测试例子
def abs(n):
    '''
    Function to get absolute value of number.

    Example:

    >>> abs(1)
    1
    >>> abs(-1)
    1
    >>> abs(0)
    0
    '''
    return n if n >= 0 else (-n)
if __name__=='__main__':
    import doctest
    doctest.testmod()



