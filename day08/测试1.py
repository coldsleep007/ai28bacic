"""
class ObjSet(object):
    gattr = "init"
    def __init__(self, attr):
        self.attr = attr
    @classmethod
    def setg(cls,gattr):
        cls.gattr = gattr
    def tryGattr(self,gattr):
        self.gattr = gattr

obj = ObjSet(10)
# 第一次打印
print(obj.gattr,ObjSet.gattr)
obj.tryGattr("python")
# 第二次打印
print(obj.gattr,ObjSet.gattr)
obj.setg("golang")
# 第三次打印
print(obj.gattr,ObjSet.gattr)
"""
class Person(object):
   def job(self):
      print('每个人都需要工作')

class Teacher(Person):
   def job(self):
      print('老师的工作是教书育人')

class Dog(object):
   def job(self):
      print('狗子的工作是卖萌和守大门')

class Student(object):
   def study(self):
      print('学生的工作是学习')

def worker(obj):
   obj.job()


#p = Person().worker(p)


#t = Teacher().worker(t)


#d = Dog().worker(d)


s = Student().worker(s)

