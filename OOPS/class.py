from abc import ABC,abstractclassmethod
# class A(ABC):
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     @abstractclassmethod
#     def notice(self):
#         pass
#     def p(self):
#         print(self.name)
#         print(self.age + 10)
class A(ABC):
    @abstractclassmethod
    def notice(self):
        pass
class B(A):
    def notice(self):
        print('Abstract')

# obj = A('Shubhanshu',11)
obj1 = B()
# obj.p()
obj1.notice()