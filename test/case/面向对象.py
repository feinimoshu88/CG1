# class Student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score
#         # #限制访问属性，用'__'
#         # self.__name=name
#         # self.__score=score
#     def getScore(self):
#         print(self.name)
#         print(self.score)
#     def getGrade(self):
#         if int(self.score)>=90:
#             return "A"
#         if 80<int(self.score)<90:
#             return "B"
#         else:
#             return "C"
#     #设置score
#     def set_score(self,score):
#         if 0<=score<=100:
#             self.__score=score
#         else:
#             raise ValueError ("bad score")
#
#
# s=Student('zhangsan',100)
# # s.getScore()
# # print(s)
# # print(Student)
# #s.name='nihao'
# #'__name'是类的私有变量，外部不能访问，不能修改，so使代码更强大
# #s.__name="nnn"
# # s.getScore()
# # print(s.getGrade())
# s=Student('zhangsan',1)
# s.set_score('12a')

#练习请把下面的Student对象的gender字段对外隐藏起来，用get_gender()和set_gender()代替，并检查参数有效性：
class Student(object):
    # __slots__ = ("name","gender")
    gender=None
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def set_gender(self,gender):
        if gender=='男':
            self.gender=gender
        elif gender=='女':
            self.gender()==gender
        else:
            raise ValueError('bad gender')
    @property
    def get_gender(self):
        return self.gender
s=Student('zhangsan','男')
print(type(s))

#判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
   pass
print(type(fn)==types.FunctionType)
type(abs)==types.BuiltinFunctionType
type(lambda x: x)==types.LambdaType
type((x for x in range(10)))==types.GeneratorType
#要判断class的类型，可以使用isinstance()函数。
# print(isinstance(s,Student))
# print(isinstance(s,object))
#判断是否是两个类型中的一种
print(isinstance([1,2,3],(list,tuple)))
#判断一个对象是否有某个属性
print(hasattr(s,'x'))

##只允许对Student实例添加name和age属性。
# s.x="x"
# print(s.x)
#@property可以把一个方法变成一个属性来调用
#@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值
print(s.gender)





